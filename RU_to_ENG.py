# Ru2Eng
def Ru2ENG(msg):
    """Принимает на вход сообщение на русском и преобразует его в выражение написанное на английсом"""
    new_message = ''
    LETTERS = {'ь': '', 'ъ': '', 'а': 'a', 'б': 'b', 'в': 'v',
               'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
               'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l',
               'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
               'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
               'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ы': 'yi',
               'э': 'e', 'ю': 'yu', 'я': 'ya'}

    for i in msg:
        if i.lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            if i.isupper():
                LETTER = LETTERS.get(i.lower()).upper()
            else:
                LETTER = LETTERS.get(i.lower())
            new_message += LETTER
        else:
            new_message += i
    return new_message


def main():
    message = input('Введите сообщение на русском: ')
    print(Ru2ENG(message))


if __name__ == '__main__':
    main()
