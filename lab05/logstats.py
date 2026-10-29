def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)

    if len(parts) < 3:
        raise ValueError("Некорректный формат строки журнала")

    if parts[1] not in ["DEBUG", "INFO", "WARNING", "ERROR"]:
        raise ValueError("Неизвестный уровень ошибки")

    return {
        "time": parts[0],
        "level": parts[1],
        "message": parts[2]
    }

def count_levels(lines: list[str]) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1

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
            if event["level"] == "ERROR":
                msg = event["message"]
                errors[msg] = errors.get(msg, 0) + 1
        except ValueError:
            continue

    sorted_errors = sorted(errors.items(), key=lambda x: x[1], reverse=True)
    return [[msg, count] for msg, count in sorted_errors[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]

    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("Частые ошибки:")

    for message, count in errors:
        lines.append(f"- {message} – {count}")

    return "\n".join(lines) + "\n"
