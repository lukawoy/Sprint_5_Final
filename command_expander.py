# Последняя успешная посылка 106842378


def command_expander(in_command: str, num_char: int = 1, calls: int = 0):
    """
    Возвращает расшифрованную строку.

        Параметры:
            in_command (str): зашифрованная строка
            num_char (int): количество символов в подстроке (для рекурсии)
            calls (int): счетчик глубины рекурсии (для рекурсии)

        Возвращаемое значение:
            current_str (str): расшифрованная строка
            index (int): текущий индекс цикла (для рекурсии)
    """
    open_square_bracket = '['
    string_zero = '0'
    length: int = len(in_command)
    current_str: str = ''
    current_num: str = ''
    index: int = -1

    while index < length:
        index += 1

        if index == length:
            return current_str, index

        item: str = in_command[index]

        if item.isdecimal():
            current_num += item
        elif item == open_square_bracket:
            return_str, skip = command_expander(in_command[index + 1:],
                                                int(current_num),
                                                calls=calls + 1)
            index += skip
            current_str += return_str
            current_num = string_zero
        elif item.isalpha():
            current_str += item
        else:
            if calls == 0 and index != length - 1:
                return_str, skip = command_expander(in_command[index + 1:], 1,
                                                    calls=calls + 1)
                index += skip
                current_str += return_str
                continue
            return current_str * num_char, index + 1


if __name__ == '__main__':
    print(command_expander(input())[0])
