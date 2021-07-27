from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime

import desert
from marshmallow import fields


@dataclass
class BoundingBox:
    """Represents a boundig bow for a detected motion in an image."""

    x: int
    y: int
    width: int
    height: int


@dataclass
class Vector:
    """Represents a simple spatial vector, (x, y)"""

    x: int
    y: int


@dataclass
class VelocityVector:
    """Represents a simple velocity vector, (speed, (x, y))"""

    speed: int
    direction: Vector = field(
        metadata=desert.metadata(fields.Nested(desert.schema(Vector)))
    )


@dataclass
class ClassPredictionVector:
    """Represents a class prediction vector with a label and the percent of confidence."""

    label: str
    prediction: int  # in percent


@dataclass
class Message(ABC):
    """Base abstract class to represent our messages."""

    timestamp: datetime
    frame_id: str
    bounding_box: BoundingBox = field(
        metadata=desert.metadata(fields.Nested(desert.schema(BoundingBox)))
    )

    def to_dict(self) -> dict:
        """Convert the message to a dictionary"""
        return desert.schema(self.__class__).dump(self)

    @classmethod
    def from_dict(cls, data: dict) -> Message:
        """
        Loads a message object from a dictionary.
        """
        return desert.schema(cls).load(data)


@dataclass
class MotionVectorMessage(Message):
    """Motion vector message representation."""

    velocity_vector: VelocityVector = field(
        metadata=desert.metadata(fields.Nested(desert.schema(VelocityVector)))
    )


@dataclass
class DetectionVectorMessage(Message):
    """
    Detection vector message representation.

    A message contains a list of class prediction with their label and
    percent of confidence.

    For instance: [(car, 98), (bike, 5)]
    """

    class_prediction_vectors: list[ClassPredictionVector] = field(
        default_factory=list,
        metadata=desert.metadata(
            fields.List(
                fields.Nested(
                    desert.schema(
                        ClassPredictionVector,
                    ),
                )
            )
        ),
    )
