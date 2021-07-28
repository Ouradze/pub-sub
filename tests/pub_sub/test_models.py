from upciti.messages.factories import MotionVectorMessageFactory
from upciti.pub_sub.models import Logger, MotionDetector, SingleShotDetector

from tests.utils import MockQueue


def test_motion_detector():
    queue = MockQueue()
    motion_vector = MotionVectorMessageFactory()

    motion_detector = MotionDetector([queue])  # type: ignore
    motion_detector.broadcast(motion_vector)  # type: ignore
    assert queue.queue == [motion_vector]


def test_single_shot_detector():
    queue = MockQueue()
    logging_queue = MockQueue()
    motion_vector = MotionVectorMessageFactory()
    queue.put(motion_vector)

    motion_detector = SingleShotDetector([logging_queue], [queue])  # type: ignore
    motion_detector.run()  # type: ignore
    assert queue.queue == []
    assert logging_queue.queue == [motion_vector]


def test_logger():
    logging_queue = MockQueue()
    motion_vector = MotionVectorMessageFactory()
    logging_queue.put(motion_vector)

    logger = Logger([logging_queue])  # type: ignore
    logger.run()  # type: ignore
    assert logging_queue.queue == []
