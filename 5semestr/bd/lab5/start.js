db = connect( 'mongodb://localhost/FirstDB' );
db.EMPLOYEE_BLANK.insertMany(
    [{  
        _id:1,
        "name":"Иван",
        "sername":"Иванов",
        "father_name":"Иванович",
        "email":"ivan@gmail.com",
        "telefone_number":"8(777)111-11-11",
        "date_birth":"10.10.1987",
        "yvlecenia":["плаванье","шахматы"],
        "document":"Номер уведомления: 123"
    },
    {
        _id:2,
        "name":"Николай",
        "sername":"Семерук",
        "father_name":"Александрович",
        "email":"killer@rambler.ru",
        "telefone_number":"7(777)523-68-91",
        "yvlecenia":["бокс","каратэ"],
        "document":"Номер приказа: 1001"
    },
    {
        _id:3,
        "name":"Александр",
        "sername":"Хопта",
        "father_name":"Петрович",
        "email":"sasha@.ru",
        "telefone_number":"(2-20-47)",
        "yvlecenia":["плавание","бокс"],
        "document":"Номер распоряжения: 202"
    },
    {
        _id:4,
        "name":"Владимир",
        "sername":"Никифоров",
        "father_name":"Александрович",
        "email":"vova@rambler.ru",
        "telefone_number":"2-45-48",
        "date_birth":"12.07.1967",
        "document":"Номер приказа: 404"
    },
    {
        _id:5,
        "name":"Семен",
        "sername":"Лобанов",
        "father_name":"Иванович",
        "email":"semen@yandex.com",
        "telefone_number":"8(777)654-12-21",
        "yvlecenia":["борьба","шахматы"],
        "document":"Номер приказа: 15"
    },
    {
        _id:6,
        "name":"Глеб",
        "sername":"Кисегач",
        "father_name":"Викторович",
        "email":"gleb@mail.",
        "telefone_number":"2-87-98",
        "yvlecenia":["компьютерные игры","плванье"],
        "document":"Номер распоряжения: 333"
    },
    {
        _id:7,
        "name":"Варя",
        "sername":"Черноус",
        "father_name":"Петрович",
        "email":"cher@mail.ru",
        "telefone_number":null,
        "date_birth":"14.01.1980",
        "document":"Номер приказа: 1"
    }
])