
class PasswordError(Exception):
    pass

class LoginError(Exception):
    pass

class not_found(LoginError):
    pass

class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass

class CopyError(PasswordError):
    pass

class invalid_password(PasswordError):
    pass


strs = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю',
        'qwertyuiop', 'asdfghjkl', 'zxcvbnm']
low = set(''.join(strs))
up = set(''.join(strs).upper())
num = set('1234567890')


def pass_is_valid(psw):
    for i in range(len(psw) - 2):
        psw_ = psw[i:i + 3].lower()
        for i in strs:
            if psw_ in i:
                return False
    return True


def passworld_check(t):
        if not len(str(t)) >8: raise LengthError("пароль слишком короткий")
        if not (set(t) & num): raise DigitError("в пароле нет числе")
        if not (set(t) & up): raise LetterError("в пароле нет загланыйх букв")
        if not (set(t) & low): raise LetterError("в пароле нет маленьких букв")
        if not pass_is_valid(t): raise SequenceError("пароль слишком простой")
        return True


