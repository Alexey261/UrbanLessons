class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

'''Главный недостаток этой модели соревнований в том, что бегуны стартуют и продолжают движение не одновременно,
а с разницей в одну итерацию цикла, т.е. бегун даже с самой низкой скоростью, но стартующий первым может получить решающее
преимущество, если его однократное приращение пройденного расстояния соизмеримо со всей дистанцией, а разница со скоростями
конкурентов не велика. Можно подобрать такой набор входных данных и порядок передачи параметров, что самый быстрый бегун
"придет" последним. В этой модели можно получать предсказуемый результат, если первым всегда будет стартовать бегун с самой
высокой скоростью, за ним тот, кто помедленней, и т.д. Для этого предлагается отсортировать список бегунов по убыванию
скорости, а итерацию с удалением элементов списка выполнять по его копии, чтобы порядок бегунов не нарушался.
Изменения в классе Tournament помечены комментариями.'''

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        self.participants.sort(key=lambda x: x.speed, reverse=True) # сортировка списка бегунов по скорости
        while self.participants:
            for participant in self.participants.copy(): # итерация по копии списка
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name  # записать в словарь имя, а не сам объект
                    place += 1
                    self.participants.remove(participant)

        return finishers



