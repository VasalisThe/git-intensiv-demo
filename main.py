from src.game import GuessNumberGame, GuessNumberConfig


def main() -> None:
    # Базовая конфигурация: число от 1 до 100, попыток бесконечно
    config = GuessNumberConfig(min_value=1, max_value=100, max_attempts=None)
    game = GuessNumberGame(config=config)
    game.run()


if __name__ == "__main__":
    # Запуск как модуля: python -m src.main
    main()
