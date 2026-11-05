def count_by_extension(paths: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}

    for path in paths:
        filename = path.rsplit("/", 1)[-1]

        last_dot = filename.rfind(".")
        # Если точки нет или она стоит в самом начале (файл начинается с точки),
        # то расширение пустое.
        if last_dot == -1 or last_dot == 0:
            extension = ""
        else:
            extension = filename[last_dot + 1:].lower()

        result[extension] = result.get(extension, 0) + 1

    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""

    return min(paths, key=lambda path: (-path.count("/"), path))


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]

    if n_bytes < 1024:
        return f"{n_bytes} Б"

    size = float(n_bytes)
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    return f"{size:.1f} {units[unit_index]}"
