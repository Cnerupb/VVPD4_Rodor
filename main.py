"""ВВПД Практическая 5"""


def is_cbs(lisp_reference: str) -> int:
    """Функция проверки строки.
    Проверяет, является ли строка ПСП

    Examples:
        print(is_cbs("()()"))  # 1
        print(is_cbs("(()))("))  # 0
        print(is_cbs("abc"))  # -1

    Args:
        lisp_reference (str): строка

    Returns:
        int: коректность ПСП
    """
    balance = 0
    for char in lisp_reference:
        if char not in "()":
            return -1
        if char == "(":
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                return 0
    return 1 if balance == 0 else 0


def need_to_move(lisp_reference: str) -> int:
    """Функция вычисляет, сколько минимальных изменений необходимо
    сделать в строке, чтобы превратить её в ПСП.

    Examples:
        print(need_to_move("()()"))  # 0
        print(need_to_move("(()))("))  # 2
        print(need_to_move(")))(((()"))  # 3

    Args:
        lisp_reference (str): строка

    Returns:
        int: количество изменений

    Raises:
        ValueError: Неправильная переменная
    """
    if list_reference is None:
        raise ValueError
    balance = 0
    max_balance = 0
    for char in lisp_reference:
        if char == "(":
            balance += 1
        else:
            balance -= 1
        max_balance = max(max_balance, -balance)
    return max_balance


def main():
    """Основная функция"""
    # Примеры использования
    print(is_cbs("()()"))  # 1
    print(is_cbs("(()))("))  # 0
    print(is_cbs("abc"))  # -1

    print(need_to_move("()()"))  # 0
    print(need_to_move("(()))("))  # 2
    print(need_to_move(")))(((()"))  # 3


if __name__ == "__main__":
    main()
