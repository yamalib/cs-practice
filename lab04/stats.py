def parse_record(line: str) -> dict:
    parts = [p.strip() for p in line.split(";")]

    if not line.strip():
        raise ValueError("Пустая строка")

    if len(parts) != 3:
        raise ValueError(f"Неверный формат строки. Ожидалось 3 поля, получено {len(parts)}.")

    city, temp_str, date = parts

    if not city or not date:
        raise ValueError("Название города и дата не могут быть пустыми.")

    if city[0] == ' ':
        raise ValueError("Неверно задано название города")

    try:
        temperature = temp_str.split('.')

        if len(temperature[1]) == 1:
            temperature = float(temp_str)
        else:
            raise ValueError("Температура введена некорректным форматом")

    except ValueError:
        raise ValueError(f"Неверный формат температуры")

    return {"city": city, "temperature": temperature, "date": date}
    # return city, temperature, date

def read_valid(lines: list[str]) -> list[dict]:
    valid_total = []
    skipped_total = 0
    total_temp = {}
    count = {}
    #print(lines)
    for line in lines:
        #print(line)
        try:
            record = parse_record(line)
            city = record["city"]
            temp = record["temperature"]
            #print(city, temp)

            total_temp[city] = total_temp.get(city, 0) + temp
            count[city] = count.get(city, 0) + 1

            valid_total.append(record)
        except ValueError:
            continue
    return valid_total

def average_by_city(records: list[dict]) -> dict:
    """Средняя температура по каждому городу, округлённая до десятых."""
    sums = {}
    counts = {}
    for i in records:
        city = i["city"]
        sums[city] = sums.get(city, 0.0) + i["temperature"]
        counts[city] = counts.get(city, 0) + 1

    average_cities = {}
    for city in sums:
        average = round(sums[city] / counts[city], 1)
        average_cities[city] = average
    return average_cities

def warmest_city(records: list[dict]) -> str:
    """Город с наибольшей средней температурой. При равенстве — первый по алфавиту."""

    averages = average_by_city(records)
    best_city = None
    max_temp = -float('inf')

    for city, temp in averages.items():
        if temp > max_temp:
            max_temp = temp
            best_city = city
        elif temp == max_temp:
            if best_city is None or city < best_city:
                best_city = city
    return best_city
