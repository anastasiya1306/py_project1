def word_upper(user_input):
    """
    Функция принимает на вход строку и возвращает её, со всеми заглавными буквами
    """
    return user_input.upper()


print(word_upper(input()))


def word_title(user_input):
    """
    Функция делает заглавными первые буквы каждого слова в строке, поступившей на вход функции
    """
    return user_input.title()


print(word_title(input()))