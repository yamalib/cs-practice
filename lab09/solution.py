import numpy as np

def make_hours() -> list[int]:
    """Возвращает вектор часов: от 0 до 21 с шагом 3."""
    return np.arange(0, 22, 3).tolist()


def vector_report(values: list[float]) -> dict:
    """Возвращает третий, последний, средний срез, каждый второй и развёрнутый вектор."""
    arr = np.array(values)

    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }


def change_vector(values: list[float]) -> list[float]:
    """В независимой копии заменяет индексы 2–4 на 99, затем каждый второй — на -1."""
    arr = np.array(values).copy()

    arr[2:5] = 99
    arr[::2] = -1

    return arr.tolist()


def cap_above(values: list[float], limit: float) -> list[float]:
    """Заменяет все значения больше limit на limit с помощью одной маски."""
    arr = np.array(values).copy()

    arr[arr > limit] = limit

    return arr.tolist()


def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    """Переводит весь вектор температур из Цельсия в Фаренгейт без цикла."""
    arr = np.array(values)
    return (arr * 9 / 5 + 32).tolist()
