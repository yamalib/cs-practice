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

def count_levels(lines: list[str]) -> dict:
    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
        else:
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1

    return counts

def top_errors(lines: list[str], n: int) -> list[list]:
    if n <= 0:
        return []

    errors = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]
            errors[message] = errors.get(message, 0) + 1

    sorted_errors = sorted(
        errors.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return [[message, count] for message, count in sorted_errors[:n]]
