import factory

from upciti.messages.models import (
    BoundingBox,
    ClassPredictionVector,
    DetectionVectorMessage,
    Message,
    MotionVectorMessage,
    Vector,
    VelocityVector,
)


class BoundingBoxFactory(factory.Factory):
    class Meta:
        model = BoundingBox

    x = factory.Faker("random_int")
    y = factory.Faker("random_int")
    width = factory.Faker("random_int")
    height = factory.Faker("random_int")


class VectorFactory(factory.Factory):
    class Meta:
        model = Vector

    x = factory.Faker("random_int")
    y = factory.Faker("random_int")


class VelocityVectorFactory(factory.Factory):
    class Meta:
        model = VelocityVector

    speed = factory.Faker("random_int")
    direction = factory.SubFactory(VectorFactory)


class ClassPredictionVectorFactory(factory.Factory):
    class Meta:
        model = ClassPredictionVector

    label = factory.Faker("word")
    prediction = factory.Faker("random_int", min=0, max=100)


class MessageFactory(factory.Factory):
    class Meta:
        model = Message

    timestamp = factory.Faker("date_time")
    frame_id = factory.Faker("uuid4")
    bounding_box = factory.SubFactory(BoundingBoxFactory)


class MotionVectorMessageFactory(MessageFactory):
    class Meta:
        model = MotionVectorMessage

    velocity_vector = factory.SubFactory(VelocityVectorFactory)


class DetectionVectorMessageFactory(MessageFactory):
    class Meta:
        model = DetectionVectorMessage

    # TODO(ouradze): fix this one day with RelatedFactoryList...
    class_prediction_vectors = factory.List(
        [factory.SubFactory(ClassPredictionVectorFactory) for _ in range(2)]
    )
