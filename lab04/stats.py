def parse_record(line: str) -> dict:
    parts = [p.strip() for p in line.split(";")]
    if len(parts) != 3:
        raise ValueError(f"Неверный формат строки. Ожидалось 3 поля, получено {len(parts)}.")

    city, temp_str, date = parts

    if not city or not date:
        raise ValueError("Название города и дата не могут быть пустыми.")

    try:
        temperature = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура должна быть числом, получено: '{temp_str}'.")

    return {"city": city, "temperature": temperature, "date": date}
