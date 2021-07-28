import logging
from multiprocessing import Manager, Process
import sys

from upciti.messages.factories import MotionVectorMessageFactory
from upciti.pub_sub.models import Logger, MotionDetector, SingleShotDetector


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
logger.addHandler(stdout_handler)


def run_worker(workers: int = 2) -> None:
    manager = Manager()
    default_queue = manager.Queue()
    logging_queue = manager.Queue()

    processes = []

    motion_detect_publisher = MotionDetector([default_queue])  # type: ignore
    processes.append(
        Process(
            target=motion_detect_publisher.run_forever,
            args=(MotionVectorMessageFactory(),),
        )
    )
    logger_sub = Logger([logging_queue])  # type: ignore
    processes.append(Process(target=logger_sub.run_forever))

    for _ in range(workers):
        single_shot_detector = SingleShotDetector([logging_queue], [default_queue])  # type: ignore
        processes.append(Process(target=single_shot_detector.run_forever))

    try:
        for process in processes:
            process.start()

        for process in processes:
            process.join()
    except KeyboardInterrupt:
        logger.info("Received exit, killing processes.")
        for process in processes:
            process.terminate()


if __name__ == "__main__":
    run_worker()
