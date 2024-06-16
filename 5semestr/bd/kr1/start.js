db.news.insertMany([{
    "название статьи":"статья про Америку",
    "автор":"Иванов Иван Иванович",
    "дата размещения": new Date("2022-10-10"),
    "url":"news/005",
    "теги":["Америка","Запад"],
    "комментарии":[{
        "name":"анонимус",
        "email":"anonimus@gmail.com",
        "телефон":89055552020,
        "текст":"автора всё по фактам рассказал",
        "оценка":10
    }]
},
{
    "название статьи":"самая интересная статья",
    "автор":"Сидоров Михаил Петрович",
    "дата размещения": new Date("2010-12-31"),
    "url":"news/001",
    "теги":["Новый год","Праздник"],
    "комментарии":[{
        "name":"Антон",
        "email":"AntonK1992@gmail.com",
        "телефон":89995337876,
        "текст":"лучшее, что я читал",
        "оценка":10
    }]
},
{
    "название статьи":"очень рисковананя статья",
    "автор":"Иванов Иван Иванович",
    "дата размещения": new Date("2019-04-20"),
    "url":"news/002",
    "теги":["Риски","Провокации"],
    "комментарии":[{
        "name":"Зубенко Михаил",
        "email":"zubenko@mail.ru",
        "телефон":89059404100,
        "текст":"ни слова правды!",
        "оценка":1
    }]
},
{
    "название статьи":"статья про Россию",
    "автор":"Быков Алёша Попович",
    "дата размещения": new Date("2019-09-01"),
    "url":"news/003",
    "теги":["1 Сентября","Праздник"],
    "комментарии":[{
        "name":"Илья Муромец",
        "email":"muromec@mail.ru",
        "телефон":89055506314,
        "текст":"бедные дети",
        "оценка":7
    }]
},
{
    "название статьи":"статья про курс валют",
    "автор":"Хонко Иван Кириллович",
    "дата размещения": new Date("2022-02-10"),
    "url":"news/004",
    "теги":["Доллар","Запад","Евро"],
    "комментарии":[{
        "name":"Ибрагим",
        "email":"killer002@gmail.com",
        "телефон":89997770101,
        "текст":"да фигня это всё",
        "оценка":3
    }]
},
{
    "название статьи":"самая интересная статья 2!",
    "автор":"Сидоров Михаил Петрович",
    "дата размещения": new Date("2022-12-31"),
    "url":"news/006",
    "теги":["Новый год","Праздник"],
    "комментарии":[{
        "name":"Антон",
        "email":"AntonK1992@gmail.com",
        "телефон":89995337876,
        "текст":"лучшее, что я читал повторилось!",
        "оценка":10
    },
    {
        "name":"анонимус",
        "email":"anonimus@gmail.com",
        "телефон":89055552020,
        "текст":"автора всё по фактам рассказал",
        "оценка":10
    }]
}])