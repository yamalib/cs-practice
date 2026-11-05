def csv_to_records(text: str) -> list[dict]:
    if not text or not text.strip():
        return []

    lines = text.strip().split('\n')
    headers = [h.strip() for h in lines[0].split(',')]
    records = []

    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(',')]
        record = {}
        for i in range(min(len(headers), len(values))):
            record[headers[i]] = values[i]
        records.append(record)

    return records


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list = None

    for line in lines:
        if '#' in line:
            line = line.split('#')[0]
        line = line.strip()
        if not line:
            continue

        if line.startswith('- '):
            val_str = line[2:].strip()
            if val_str.lower() in ('true', 'yes'):
                val = True
            elif val_str.lower() in ('false', 'no'):
                val = False
            else:
                try:
                    val = int(val_str)
                except ValueError:
                    try:
                        val = float(val_str.replace(',', '.'))
                    except ValueError:
                        val = val_str
            if current_list is not None:
                current_list.append(val)

        elif ':' in line:
            k, v_str = line.split(':', 1)
            k = k.strip()
            v_str = v_str.strip()

            if v_str == '':
                current_list = []
                result[k] = current_list
            else:
                if v_str.lower() in ('true', 'yes'):
                    val = True
                elif v_str.lower() in ('false', 'no'):
                    val = False
                else:
                    try:
                        val = int(v_str)
                    except ValueError:
                        try:
                            val = float(v_str.replace(',', '.'))
                        except ValueError:
                            val = v_str
                result[k] = val
                current_list = None

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    merged_rows = []
    for row in rows:
        if key in row and row[key] in extra:
            new_row = extra[row[key]].copy()
            new_row.update(row)
            merged_rows.append(new_row)
        else:
            merged_rows.append(row.copy())
    return merged_rows


def records_to_json(records: list[dict]) -> str:
    if not records:
        return "[]"

    res = ["["]
    for i, rec in enumerate(records):
        keys = sorted(rec.keys())
        if not keys:
            res.append("  {}")
        else:
            res.append("  {")
            for j, k in enumerate(keys):
                v = rec[k]
                if isinstance(v, str):
                    v_str = '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'
                elif isinstance(v, bool):
                    v_str = "true" if v else "false"
                elif v is None:
                    v_str = "null"
                else:
                    v_str = str(v)

                comma = "," if j < len(keys) - 1 else ""
                res.append(f'    "{k}": {v_str}{comma}')
            res.append("  }")

        if i < len(records) - 1:
            res[-1] += ","

    res.append("]")
    return "\n".join(res)
