import logging
from multiprocessing import Queue
import sys
from time import sleep
from typing import no_type_check

from upciti.messages.models import Message


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
logger.addHandler(stdout_handler)


class Publisher:
    """Publisher class to wrap our exchanges."""

    def __init__(self, channel_to_broadcast: list[Queue]) -> None:
        self.channel_to_broadcast = channel_to_broadcast

    def broadcast(self, data: Message) -> None:
        """Broacast some data to all connected clients on the channels."""
        for queue in self.channel_to_broadcast:
            queue.put(data)

    def run_forever(self, data: Message) -> None:
        """Use this funciton to run the publisher whithout stopping."""
        logger.info("Creating data and putting it on the queue")
        while True:
            self.broadcast(data)
            sleep(1)  # This is to fake some data sent, every seconds.


class Subscriber:
    def __init__(self, channel_to_listen: list[Queue]) -> None:
        self.channel_to_listen = channel_to_listen

    def on_receive(self, data: Message) -> None:
        raise NotImplementedError

    def run(self) -> list[Message]:
        results = []

        for queue in self.channel_to_listen:
            data = queue.get()
            results.append(data)
            self.on_receive(data)
        # This could be a tuple to with in/out data.
        return results

    def run_forever(self) -> None:
        while True:
            self.run()


class MotionDetector(Publisher):
    pass


class SingleShotDetector(Subscriber, Publisher):
    def __init__(
        self, channel_to_broadcast: list[Queue], channel_to_listen: list[Queue]
    ) -> None:
        self.channel_to_broadcast = channel_to_broadcast
        self.channel_to_listen = channel_to_listen

    def on_receive(self, data: Message) -> None:
        # TODO(ouradze): process actual data :D
        logger.debug(f"Heavy computation in progess from: {data}")

    def run(self) -> list[Message]:
        results = super().run()
        for data in results:
            self.broadcast(data)
        return results

    # TODO(ouradze): ugly but I will look into it later
    @no_type_check
    def run_forever(self) -> None:
        return super().run_forever()


class Logger(Subscriber):
    def on_receive(self, message: Message) -> None:
        logger.info(f"{message.timestamp}: {message}")
