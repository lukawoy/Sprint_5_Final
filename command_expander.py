# Последняя успешная посылка 106764944
abbreviated_command = input()


def command_expander(in_command: str, num_char: int = 1, calls: int = 0):
    """Функция дешифратор сокращенных сообщений,
    возвращает расшифрованную строку исключительно с буквами.
    """

    length: int = len(in_command)
    current_str: str = ''
    current_num: str = ''
    index: int = -1

    while index < length:
        index += 1

        if index == length:
            return current_str, index

        item: str = in_command[index]

        if item.isdigit():
            current_num += item
        elif item == '[':
            return_str, skip = command_expander(in_command[index + 1:],
                                                int(current_num),
                                                calls=calls + 1)
            index += skip
            current_str += return_str
            current_num = '0'
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
    print(command_expander(abbreviated_command)[0])
