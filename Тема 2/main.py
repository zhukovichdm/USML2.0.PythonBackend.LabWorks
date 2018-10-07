from random import randint


class Car:
    CAR_SPECS = {
        'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
        'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
        'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
        'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
        'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
    }
    competitors = CAR_SPECS.keys()


class Weather:
    def __init__(self):
        self.wind_speed = randint(0, 20)


class Competition:
    def __init__(self, distance):
        self.distance = distance

    def start(self):
        start(Car.competitors, self.distance, Weather().wind_speed)


def start(competitors, distance, wind_speed):
    for competitor_name in competitors:
        competitor_time = 0
        competitor_speed = 0
        car = Car.CAR_SPECS[competitor_name]

        for distance in range(distance):
            _wind_speed = randint(0, wind_speed)

            if competitor_time == 0:
                _speed = 1
            else:
                _speed = (competitor_time / car["time_to_max"]) * car['max_speed']
                if _speed > _wind_speed:
                    _speed -= (car["drag_coef"] * _wind_speed)

            competitor_time += float(1) / _speed

        print("Car <%s> result: %f" % (competitor_name, competitor_time))


Competition(10000).start()
