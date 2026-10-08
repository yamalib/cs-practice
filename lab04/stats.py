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

def read_valid(lines):
    total = {}
    count = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            city = record["city"]
            temp = record["temperature"]

            total[city] = total.get(city, 0) + temp
            count[city] = count.get(city, 0) + 1
        except ValueError:
            continue

def average_by_city(records: list[dict]) -> dict:
    """Средняя температура по каждому городу, округлённая до десятых."""
    sums = {}
    counts = {}
    for r in records:
        city = r["city"]
        sums[city] = sums.get(city, 0.0) + r["temperature"]
        counts[city] = counts.get(city, 0) + 1

    average_cities = {}
    for city in sums:
        average = round(sums[city] / counts[city], 1)
        average_cities[city] = average
    return average_cities
