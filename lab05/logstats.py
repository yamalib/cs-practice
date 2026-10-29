LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)

    if len(parts) < 3:
        raise ValueError("Некорректный формат строки журнала")

    time, level, message = parts

    if level not in LEVELS:
        raise ValueError("Неизвестный уровень")

    return {
        "time": time,
        "level": level,
        "message": message,
    }