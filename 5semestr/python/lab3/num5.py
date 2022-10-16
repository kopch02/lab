class NumberError(Exception):
    pass


class FormatError(NumberError):
    pass


class LenghtError(NumberError):
    pass


class CountryError(NumberError):
    pass


class OperatorError(NumberError):
    pass


MTS=str(list(range(910,920)) + list(range(980,990)))
MEGAFON=str(list(range(920,940)))
BILAIN=str(list(range(902,907)) + list(range(960,970)))



def Format(number):
    return number.count("(") == number.count(")") or "--" in number


def Lenght(number):
    return len(number) == 11


def Country(psw):
    t = False
    if psw[0] == "8":
        t = True
    elif psw[0] == "7":
        t = True
    return t


def Operator(psw):
    return (psw[1:4] in MTS) or (psw[1:4] in MEGAFON) or (psw[1:4] in BILAIN)


def check_phone(n):
    if not Format(n) : raise FormatError("неверный формат")
    chars = ['-', '+', '(', ')', ' ']
    for i in chars:
        n = n.replace(i,"")
    if not Lenght(n) : raise LenghtError("неверное количество цифр")
    if not Country(n) : raise CountryError("неверный код страны")
    if not Operator(n) : raise OperatorError("не определяется оператор сотовой связи")

    res = f"+7{n[1:]}"

    return res

numbers = [
        "+7(902)123-4567",
        "8(902)1-2-3-45-67",
        "504))635(22))9    9",
        "8--9019876543-22-3--4",
        "87393))985942",
        "9914273   13-87",
        "8846776522",
        "+71113253136",
        "8(916)     12 4 32-6 7"
    ]

for i in numbers:
    try:
        print(check_phone(i))
    except NumberError as e:
        print(e)


