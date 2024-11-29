import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json_data: bytes) -> Car:
    stream = io.BytesIO(json_data)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise ValueError(
            "Invalid data for Car instance: {serializer.errors}")
