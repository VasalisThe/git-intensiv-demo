from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TextIO

from src.math import get_random_number, check_guess, GuessResult


@dataclass
class GuessNumberConfig:
    min_value: int = 1
    max_value: int = 100
    max_attempts: Optional[int] = None  # None = бесконечно


class GuessNumberGame:
    """
    Текстовая игра 'Угадай число'.

    Использует конфигурацию GuessNumberConfig и функции из math.py.
    Весь ввод/вывод вынесен в метод run(), чтобы логику было
    легко переиспользовать или тестировать.
    """

    def __init__(
        self,
        config: Optional[GuessNumberConfig] = None,
        input_stream: TextIO = None,
        output_stream: TextIO = None,
    ) -> None:
        self.config = config or GuessNumberConfig()
        self.secret_number: int = get_random_number(
            self.config.min_value, self.config.max_value
        )

        # Позволяет подменять input/output при тестировании
        import sys

        self._input = input_stream or sys.stdin
        self._output = output_stream or sys.stdout

    # ----- Служебные методы работы с вводом/выводом -----

    def _print(self, text: str) -> None:
        self._output.write(text + "\n")
        self._output.flush()

    def _input_line(self, prompt: str = "") -> str:
        if prompt:
            self._print(prompt)
        return self._input.readline().strip()

    # ----- Игровая логика -----

    def run(self) -> None:
        """
        Главный игровой цикл. Спрашивает числа у пользователя,
        подсказывает 'меньше/больше' и завершает игру при победе
        или при исчерпании попыток.
        """
        self._print(
            f"Привет! Я загадал число от {self.config.min_value} до "
            f"{self.config.max_value}."
        )

        if self.config.max_attempts is None:
            self._print("Попробуй угадать! Попыток неограниченно.")
        else:
            self._print(f"Попробуй угадать! У тебя {self.config.max_attempts} попыток.")

        attempts_used = 0

        while True:
            if self.config.max_attempts is not None and attempts_used >= self.config.max_attempts:
                self._print(
                    f"Попытки закончились! Загаданное число было: {self.secret_number}."
                )
                break

            raw = self._input_line("Введи число и нажми Enter:")

            # Обработка пустой строки — даём возможность выйти
            if raw == "":
                self._print("Пустой ввод. Если хочешь выйти, набери 'exit'.")
                continue

            if raw.lower() in {"exit", "quit", "q"}:
                self._print("Выход из игры. До встречи!")
                break

            try:
                guess = int(raw)
            except ValueError:
                self._print("Это не похоже на число. Попробуй ещё раз.")
                continue

            if not (self.config.min_value <= guess <= self.config.max_value):
                self._print(
                    f"Число должно быть в диапазоне "
                    f"от {self.config.min_value} до {self.config.max_value}."
                )
                continue

            attempts_used += 1
            result: GuessResult = check_guess(self.secret_number, guess)

            if result == "correct":
                self._print(
                    f"Поздравляю! Ты угадал число {self.secret_number} "
                    f"за {attempts_used} попыток."
                )
                break
            elif result == "low":
                self._print("Моё число больше.")
            elif result == "high":
                self._print("Моё число меньше.")
