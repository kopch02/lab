import datetime
import pytest
from unittest.mock import Mock
from unittest.mock import patch
import mym


def is_past_date(date):
    result_flag = True
    today = mym.get_today()
    if date >= today:
        result_flag = False
    return result_flag


data = []
for i in range(27, 30):
    data.append(datetime.date(2022, 11, i))

res = [True,False,False]
#for i in range(3):
#    res.append(is_past_date(data[i]))

print(datetime.date(2022, 11,28))
print(type(datetime.date(2022, 11,28)))


@pytest.mark.parametrize("num, output", list(zip(data, res)))
def test_multiplication_11(num, output):
    with patch('mym.get_today', return_value = datetime.date(2022, 11,28)) as m:
        is_past_date(num) == output

    
