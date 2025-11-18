import random
from typing import Literal, Optional

GuessResult = Literal["low", "high", "correct"]


def get_random_number(
    min_value: int = 1,
    max_value: int = 100,
    rng: Optional[random.Random] = None,
) -> int:
    """
    Возвращает случайное число в диапазоне [min_value, max_value].

    :param min_value: нижняя граница диапазона (включительно)
    :param max_value: верхняя граница диапазона (включительно)
    :param rng: опционально, экземпляр random.Random для тестов
    """
    if min_value > max_value:
        raise ValueError("min_value не может быть больше max_value")

    rng = rng or random.Random()
    return rng.randint(min_value, max_value)


def check_guess(secret: int, guess: int) -> GuessResult:
    """
    Сравнивает загаданное число и попытку игрока.

    :param secret: загаданное число
    :param guess: число, введённое пользователем
    :return: "low", если попытка меньше секрета,
             "high", если больше,
             "correct", если совпало.
    """
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    return "correct"
