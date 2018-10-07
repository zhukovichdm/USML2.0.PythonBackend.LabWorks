from abc import ABC, abstractmethod
from random import randint


class Creature(ABC):
    @abstractmethod
    def specs(self):
        pass


class BaseCompetitor(Creature):
    def specs(self):
        print("BaseCompetitors")


class AbstractDecorator(Creature):
    def __init__(self, obj):
        self.obj = obj

    def specs(self):
        self.obj.specs()


class Ferrary(AbstractDecorator):
    def mark(self):
        return self.__class__.__name__

    def specs(self):
        return {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26}


class Bugatti(AbstractDecorator):
    def mark(self):
        return self.__class__.__name__

    def specs(self):
        return {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32}


class Toyota(AbstractDecorator):
    def mark(self):
        return self.__class__.__name__

    def specs(self):
        return {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40}


class Lada(AbstractDecorator):
    def mark(self):
        return self.__class__.__name__

    def specs(self):
        return {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56}


class Sx4(AbstractDecorator):
    def mark(self):
        return self.__class__.__name__

    def specs(self):
        return {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44}


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class MessageNotifier(AbstractObserver):
    def __init__(self, name):
        self.__name = name

    def update(self, message):
        print(f'{self.__name} recieved message!')


class MessagePrinter(AbstractObserver):
    def __init__(self, name):
        self.__name = name

    def update(self, message):
        print(f'{self.__name} recieved message: {message}')


class CompetitionFactory:
    @classmethod
    def create_competition(Class, distance):
        return Class.Competition(distance)

    @classmethod
    def create_competitor(Class, competitors):
        return Class.Competitors(competitors)

    @classmethod
    def create_weather(Class):
        return Class.Weather()


class Type1CompetitionFactory(CompetitionFactory):
    class Competition:
        def __init__(self, distance):
            self.__subscribers = set()
            self.distance = distance
            self.competitors = None
            self.weather = None

        def add_competitor(self, competitor):
            self.competitors = competitor

        def add_weather(self, weather):
            self.weather = weather

        def start(self):
            self.notify("Заезд начинается!")
            start(self.competitors.get(), self.distance, self.weather.get())
            self.notify("Заезд завершен!")

        def subscribe(self, subscriber):
            self.__subscribers.add(subscriber)

        def unsubscribe(self, subscriber):
            self.__subscribers.remove(subscriber)

        def notify(self, message):
            for subscriber in self.__subscribers:
                subscriber.update(message)

    class Weather:
        def get(self):
            return randint(0, 20)

    class Competitors:
        def __init__(self, competitors):
            self.competitors = competitors

        def get(self):
            return self.competitors


def create_competition(factory, listCompetitors):
    competition = factory.create_competition(1000)

    competitors = factory.create_competitor(listCompetitors)
    competition.add_competitor(competitors)

    weather = factory.create_weather()
    competition.add_weather(weather)

    return competition


def start(competitors, distance, wind_speed):
    for competitor in competitors:
        competitor_time = 0
        competitor_speed = 0
        car = competitor.specs()

        for distance in range(distance):
            _wind_speed = randint(0, wind_speed)

            if competitor_time == 0:
                _speed = 1
            else:
                _speed = (competitor_time / car["time_to_max"]) * car['max_speed']
                if _speed > _wind_speed:
                    _speed -= (car["drag_coef"] * _wind_speed)

            competitor_time += float(1) / _speed

        print("Car <%s> result: %f" % (competitor.mark(), competitor_time))


# Создаем участников.
baseCompetitor = BaseCompetitor()
competitor1 = Ferrary(baseCompetitor)
competitor2 = Bugatti(baseCompetitor)
competitor3 = Toyota(baseCompetitor)
competitor4 = Lada(baseCompetitor)
competitor5 = Sx4(baseCompetitor)
listCompetitors = [competitor1, competitor2, competitor3, competitor4, competitor5]

# Создаем наблюдателей.
notifier1 = MessageNotifier("Notifier1")
printer1 = MessagePrinter("Printer1")

# Создаем экзэмпляр заезда и подписываем на него наблюдателей
competition = create_competition(Type1CompetitionFactory, listCompetitors)
competition.subscribe(notifier1)
competition.subscribe(printer1)

competition.start()
