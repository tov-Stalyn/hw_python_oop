class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance,
                 speed, calories) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def show_training_info(self):
        return (f'Тип тренировки: {self.training_type};'
                f' Длительность: {self.duration} ч.;'
                f' Дистанция: {self.distance} км;'
                f' Ср. скорость: {self.speed} км/ч;'
                f' Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""
    CALORIES_MEAN_SPEED_MULTIPLIER: float = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79
    M_IN_KM: int = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self, LEN_STEP) -> float:
        """Получить дистанцию в км."""
        user_distance = (self.action * LEN_STEP) / self.M_IN_KM
        return user_distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        avg_speed = self.get_distance() / self.duration
        return avg_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        user_callories = (
            (self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed() +
             self.CALORIES_MEAN_SPEED_SHIFT) * self.weight / self.M_IN_KM *
             self.duration
        )
        return user_callories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.training_type, self.duration,
                           self.distance, self.speed, self.calories)


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER: float = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79
    LEN_STEP = 0.65
    M_IN_KM = 1000

    def __init__(self, action: int, duration: float, weight: float):
        super().__init__(action, duration, weight)

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self) -> float:
        run_callories = (
            (self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed() +
            self.CALORIES_MEAN_SPEED_SHIFT) * self.weight / self.M_IN_KM *
            self.duration
        )
        return run_callories

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    FIRST_WALKING_CALORIES_COEFF = 0.035
    SECOND_WALKING_CALORIES_COEFF = 2
    THIRD_WALKING_CALORIES_COEFF = 0.029

    def __init__(self, action: int, duration: float,
                 weight: float, height: float):
        super().__init__(action, duration, weight)
        self.height = height

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        return super().get_mean_speed()

    def get_spent_calories(self) -> float:
        walk_callories = (
            (self.FIRST_WALKING_CALORIES_COEFF * self.weight +
            (self.get_mean_speed()**self.SECOND_WALKING_CALORIES_COEFF /
            self.height) * self.THIRD_WALKING_CALORIES_COEFF *
            self.weight) * self.duration
        )
        return walk_callories

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()


class Swimming(Training):
    """Тренировка: плавание."""
    M_IN_KM = 1000
    FIRST_SWIM_CALORIES_COEFF = 1.1
    SECOND_SWIM_CALORIES_COEFF = 2
    LEN_STEP = 0.65

    def __init__(self, action: int, duration: float,
                 weight: float, length_pool: float, count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        return super().get_distance()

    def get_mean_speed(self) -> float:
        avg_swim_speed = (
            (self.length_pool * self.count_pool) / self.M_IN_KM / self.duration
        )
        return avg_swim_speed

    def get_spent_calories(self) -> float:
        swim_callories = (
            (self.FIRST_WALKING_CALORIES_COEFF * self.weight +
            (self.get_mean_speed()**self.SECOND_WALKING_CALORIES_COEFF /
            self.height) * self.THIRD_WALKING_CALORIES_COEFF *
            self.weight) * self.duration
        )
        return swim_callories

    def show_training_info(self) -> InfoMessage:
        return super().show_training_info()


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    trainings = {'RUN': Running, 'SWM':
                  Swimming, 'WLK': SportsWalking}
    class_type = trainings[workout_type](data)
    return class_type


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
