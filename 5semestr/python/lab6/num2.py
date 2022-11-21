import re

def is_correct_mobile_phone_number_ru(s):
    p = r"(^\+7|^8)\s?((\(\d{3}\)\s?)|(\-?\d{3}\s?\-?))\d{3}\-?\d{2}\-?\d{2}"
    if re.search(p,s) == None:
        return False
    return True



def my_test_is_correct_mobile_phone_number_ru():
    test_cases = (
        ('', False),
        ('+7' + 'a' * 10, False),
        ('+89991112233', False),
        ('+79991112233', True),
        ('89991112233', True),
        ('8-800-111-11-11', True),
        ('+7-800-111-11-11', True),
        ('8 (999) 123-45-67', True),
        ('8 (999 123-45-67', False),
        ('8 )999( 123-45-67', False),  # can't just cut off parentheses
        ('8 (999) (123)-45-67', False),  # even paired parentheses may be incorrect
    )
    for in_s, correct_answer in test_cases:
        answer = is_correct_mobile_phone_number_ru(in_s)
        if answer != correct_answer:
            return False
    return True


print('YES') if my_test_is_correct_mobile_phone_number_ru() else print('NO')