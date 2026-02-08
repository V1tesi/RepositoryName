import doctest


class Bag:
    def __init__(self, max_mass_bag: (float,int), things_mass_in_bag: (float,int)):
        """
        Создание и подготовка к работе объекта "Сумка"

        :param max_mass_bag: Максимальный вес сумки
        :param things_mass_in_bag: Вес, занимаемый вещами в сумке

        Примеры:
        >>> bag = Bag(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(max_mass_bag, (int, float)):
            raise TypeError("Макс. масса сумки должна быть int или float")
        if max_mass_bag <= 0:
            raise ValueError("Макс. масса сумки должна быть положительным числом")
        self.max_mass_bag = max_mass_bag

        if not isinstance(things_mass_in_bag, (int, float)):
            raise TypeError("Масса должна быть int или float")
        if things_mass_in_bag < 0:
            raise ValueError("Масса не может быть отрицательным числом")
        self.things_mass_in_bag = things_mass_in_bag

    def is_empty_bag(self) -> bool:
        """
        Функция которая проверяет является ли сумка пустой

        :return: Является ли сумка пустой

        Примеры:
        >>> bag = Bag(500, 0)
        >>> bag.is_empty_bag()
        """
        ...

    def add_mass_to_bag(self, mass: float) -> None:
        """
        Добавление воды в стакан.
        :param mass: Объем добавляемой массы

        :raise ValueError: Если количество добавляемой массы превышает свободное место в сумке, то вызываем ошибку

        Примеры:
        >>> bag = Bag(500, 0)
        >>> bag.add_mass_to_bag(200)
        """
        if not isinstance(mass, (int, float)):
            raise TypeError("Добавляемая масса должна быть типа int или float")
        if mass < 0:
            raise ValueError("Добавляемая масса должна быть положительным числом")
        ...

    def remove_mass_from_bag(self, delete_mass: float) -> None:
        """
        Извлечение массы из сумки.

        :param delete_mass: количество извлекаемой массы
        :raise ValueError: Если количество извлекаемой массы превышает текушей массы в сумке,
        то появляется ошибка.

        :return: количество реально извлеченной массы

        Примеры:
        >>> bag = Bag(500, 500)
        >>> bag.remove_mass_from_bag(200)
        """
        if not isinstance(delete_mass, (int, float)):
            raise TypeError("Убираемая масса должна быть типа int или float")
        if delete_mass < 0:
            raise ValueError("Убираемая масса должна быть положительным числом")
        ...
        ...
class Train:
    def __init__(self,max_speed:float, speed: float, road: str):
        """
        Создание и подготовка к работе объекта "Поезд"
        :param max_speed: Максимальная скорость
        :param speed: Текущая скорость
        :param road: Текущее направление поезда

        Примеры:
        >>> train = Train(500,0, "Санкт-Петербург - Москва")  # инициализация экземпляра класса
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Максимальная Скорость поезда должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Максимальная Скорость поезда должна быть положительным числом")
        self.max_speed = max_speed
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость поезда должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Скорость поезда должна быть положительным числом")
        self.speed = speed

        if not isinstance(road, str):
            raise TypeError("направление должно быть типа str")
        self.road = road

    def add_speed_to_train(self, add_speed: (int, float)) -> None:
        """
        Добавление скорости поезду.
        :param add_speed: добавляемая скорость

        :raise ValueError: Если количество добавляемой скорости превышает макс скорость, то вызываем ошибку

        Примеры:
        >>> train = Train(320, 0,"Novosibirsk-Moscow")
        >>> train.add_speed_to_train(200)
        """
        if not isinstance(add_speed, (int, float)):
            raise TypeError("Добавляемая скорость должна быть типа int или float")
        if add_speed < 0:
            raise ValueError("Добавляемая скорость должна положительным числом")
        ...
    def change_road(self, new_road: str) -> None:
        """
        Смена направления поезда
        :param new_road: Новое направление
        Примеры:
        >>> train = Train(500,0, "Санкт-Петербург - Москва")
        >>> train.change_road("Санкт-Петербург - Владивосток")
        """
        if not isinstance(new_road, str):
            raise TypeError("Новое направление должно быть типа str")
        ...
class Video_player:
    def __init__(self, chanel: str, video_name: str, is_playing: bool):
        """
        Создание и подготовка к работе объекта "Видеоплеер"

        :param chanel: Канал
        :param video_name: Название видео
        :param is_playing: Идет ли видео

        Примеры:
        >>> video_player = Video_player("Андрей Шавва","Дом на две семьи", True)  # инициализация экземпляра класса
        """
        if not isinstance(chanel, str):
            raise TypeError("Канал должен быть типа str")
        self.chanel = chanel

        if not isinstance(video_name, str):
            raise TypeError("Название видео должно быть типа str")
        self.video_name = video_name

        if not isinstance(is_playing, bool):
            raise TypeError("Включено ли видео должно быть типа bool")
        self.is_playing = is_playing

    def play_stop(self, new_is_playing: bool) -> None:
        """
        Остановить или продолжить просмторт
        Примеры:
        >>> video_player = Video_player("Андрей Шавва", "revit", False)
        >>> video_player.play_stop(True)
        """
        ...

    def change_video(self, new_chanel: str, new_video_name: str) -> None:
        """
        Смена видео
        :param new_chanel: Новый канал

        :param new_video_name: Новое название видео

        Примеры:
        >>> video_player = Video_player("Андрей Шавва", "Autocad", True)  # инициализация экземпляра класса
        >>> video_player.change_video("Митин А.А.", "Autocad")
        """
        if not isinstance(new_chanel, str):
            raise TypeError("Новое название канала должно быть типа str")
        if not isinstance(new_video_name, str):
            raise TypeError("Новое название видео должно быть типа str")
        ...


if __name__ == "__main__":
    doctest.testmod()