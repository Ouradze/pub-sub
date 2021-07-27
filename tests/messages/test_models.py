from upciti.messages.factories import (
    DetectionVectorMessageFactory,
    MotionVectorMessageFactory,
)
from upciti.messages.models import DetectionVectorMessage, MotionVectorMessage


def test_dump_message(snapshot):
    detection_vector_message: DetectionVectorMessage = DetectionVectorMessageFactory()  # type: ignore
    motion_vector_message: MotionVectorMessage = MotionVectorMessageFactory()  # type: ignore

    snapshot.assert_match(
        detection_vector_message.to_dict(), "detection_vector_message"
    )
    snapshot.assert_match(motion_vector_message.to_dict(), "motion_vector_message")


def test_load_message():
    detection_vector_message: DetectionVectorMessage = DetectionVectorMessageFactory()  # type: ignore
    motion_vector_message: MotionVectorMessage = MotionVectorMessageFactory()  # type: ignore

    assert (
        DetectionVectorMessage.from_dict(detection_vector_message.to_dict())
        == detection_vector_message
    )
    assert (
        MotionVectorMessage.from_dict(motion_vector_message.to_dict())
        == motion_vector_message
    )
