import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    # return JSONRenderer().render(serializer.data)
    return json.dumps(serializer.data).encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    # stream = io.BytesIO(json)
    # data = JSONParser().parse(stream)
    data = json.loads(json_data.decode("utf-8"))
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return Car(**serializer.validated_data)
    else:
        raise ValueError(
            "Invalid data for Car instance: {}".format(serializer.errors)
        )
