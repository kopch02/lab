db = connect( 'mongodb://localhost/semestrov' );

db.corpuses.drop()
db.rooms.drop()
db.customers.drop()
db.organizations_booking.drop()
db.complaints.drop()

let corpus_1 = db.corpuses.insertOne({
    "номер корпуса":1,
    "звёзд":5,
    "количество этажей":11,
    "количество комнат":100,
    "комнат на этаже":10,
    "метность номеров":2,
    "службы быта":[{
        "уборка номеров":"да",
        "прачичная":"да",
        "бар":"да",
        "ресторан":"да"
    }],
    "развлечения":[{
        "бассейн":"да",
        "сауна":"да",
        "бильяр":"да"
    }]
})
let corpus_2 = db.corpuses.insertOne({
    "номер корпуса":2,
    "звёзд":4,
    "количество этажей":20,
    "количество комнат":190,
    "комнат на этаже":10,
    "метность номеров":2,
    "службы быта":[{
        "уборка номеров":"да",
        "прачичная":"да",
        "бар":"да",
        "ресторан":"да"
    }],
    "развлечения":[{
        "бассейн":"нет",
        "сауна":"нет",
        "бильяр":"нет"
    }]
})
let corpus_3 = db.corpuses.insertOne({
    "номер корпуса":3,
    "звёзд":3,
    "количество этажей":8,
    "количество комнат":56,
    "комнат на этаже":8,
    "метность номеров":3,
    "службы быта":[{
        "уборка номеров":"да",
        "прачичная":"да",
        "бар":"нет",
        "ресторан":"да"
    }],
    "развлечения":[{
        "бассейн":"нет",
        "сауна":"нет",
        "бильяр":"нет"
    }]
})
let corpus_4 = db.corpuses.insertOne({
    "номер корпуса":4,
    "звёзд":3,
    "количество этажей":8,
    "количество комнат":168,
    "комнат на этаже":24,
    "метность номеров":1,
    "службы быта":[{
        "уборка номеров":"да",
        "прачичная":"да",
        "бар":"нет",
        "ресторан":"нет"
    }],
    "развлечения":[{
        "бассейн":"нет",
        "сауна":"нет",
        "бильяр":"нет"
    }]
})
let corpus_5 = db.corpuses.insertOne({
    "номер корпуса":5,
    "звёзд":2,
    "количество этажей":5,
    "количество комнат":25,
    "комнат на этаже":5,
    "метность номеров":3,
    "службы быта":[{
        "уборка номеров":"нет",
        "прачичная":"нет",
        "бар":"нет",
        "ресторан":"нет"
    }],
    "развлечения":[{
        "бассейн":"нет",
        "сауна":"нет",
        "бильяр":"нет"
    }]
})
let room_121 = db.rooms.insertOne({
    "корпус":corpus_1.insertedId,
    "номер_комнаты":121,
    "этаж":2,
    "цена_номера":7000,
    "статус":true
})
let room_122 = db.rooms.insertOne({
    "корпус":corpus_1.insertedId,
    "номер_комнаты":122,
    "этаж":2,
    "цена_номера":7000,
    "статус":true
})
let room_123 = db.rooms.insertOne({
    "корпус":corpus_1.insertedId,
    "номер_комнаты":123,
    "этаж":2,
    "цена_номера":7000,
    "статус":true
})
let room_124 = db.rooms.insertOne({
    "корпус":corpus_1.insertedId,
    "номер_комнаты":124,
    "этаж":2,
    "цена_номера":7000,
    "статус":true
})
let room_125 = db.rooms.insertOne({
    "корпус":corpus_1.insertedId,
    "номер_комнаты":125,
    "этаж":2,
    "цена_номера":7000,
    "статус":true
})


let cust_1 = db.customers.insertOne(
    {
        "фамилия":"петров",
        "имя":"петр",
        "отчество":"петрович",
        "номер телефона":"8(999)123-12-12",
        "забронированные комнаты":[
            {   
                "комната":room_121.insertedId,
                "дата заселения":new Date("25.07.2022"),
                "дата выселения":new Date("01.08.2022"),
            }
        ]
})
let cust_2 = db.customers.insertOne(
    {
        "фамилия":"иванов",
        "имя":"иван",
        "отчество":"иванович",
        "номер телефона":"8(999)333-22-22",
        "забронированные комнаты":[
            {   
                "комната":room_121.insertedId,
                "дата заселения":new Date("01.08.2022"),
                "дата выселения":new Date("03.08.2022"),
            }
        ]
})
let cust_3 = db.customers.insertOne(
    {
        "фамилия":"сидоров",
        "имя":"сидр",
        "отчество":"сидорович",
        "номер телефона":"8(923)285-01-01",
        "забронированные комнаты":[
            {   
                "комната":room_122.insertedId,
                "дата заселения":new Date("01.08.2022"),
                "дата выселения":new Date("31.08.2022"),
            }
        ]
})
let cust_4 = db.customers.insertOne(
    {
        "фамилия":"семёнов",
        "имя":"семён",
        "отчество":"семёнович",
        "номер телефона":"8(999)555-55-55",
        "забронированные комнаты":[
            {   
                "комната":room_123.insertedId,
                "дата заселения":new Date("01.09.2022"),
                "дата выселения":new Date("02.09.2022"),
            }
        ]
})
let cust_5 = db.customers.insertOne(
    {
        "фамилия":"зубина",
        "имя":"анастасия",
        "отчество":"петровна",
        "номер телефона":"8(999)654-32-10",
        "забронированные комнаты":[
            {   
                "комната":room_125.insertedId,
                "дата заселения":new Date("14.08.2022"),
                "дата выселения":new Date("17.08.2022"),
            }
        ]
})

let booking_1 = db.organizations_booking.insertOne({
        "название организации":"популярная",
        "количество людей":6,
        "количество комнат":3,
        "дата заселения":new Date("01.09.2022"),
        "дата выселения":new Date("15.09.2022"),
        "комнаты":[
            room_121.insertedId,
            room_122.insertedId,
            room_124.insertedId
        ]
})
let booking_2 = db.organizations_booking.insertOne({
    "название организации":"популярная",
    "количество людей":4,
    "количество комнат":2,
    "дата заселения":new Date("11.09.2022"),
    "дата выселения":new Date("15.09.2022"),
    "комнаты":[
        room_123.insertedId,
        room_125.insertedId,
    ]
})
let booking_3 = db.organizations_booking.insertOne({
    "название организации":"квн",
    "количество людей":10,
    "количество комнат":5,
    "дата заселения":new Date("01.10.2022"),
    "дата выселения":new Date("03.10.2022"),
    "комнаты":[
        room_121.insertedId,
        room_122.insertedId,
        room_123.insertedId,
        room_124.insertedId,
        room_125.insertedId
    ]
})
let booking_4 = db.organizations_booking.insertOne({
    "название организации":"nasa",
    "количество людей":2,
    "количество комнат":1,
    "дата заселения":new Date("05.08.2022"),
    "дата выселения":new Date("08.08.2022"),
    "комнаты":[
        room_121.insertedId
    ]
})
let booking_5 = db.organizations_booking.insertOne({
    "название организации":"samsung",
    "количество людей":3,
    "количество комнат":2,
    "дата заселения":new Date("01.11.2022"),
    "дата выселения":new Date("03.11.2022"),
    "комнаты":[
        room_121.insertedId,
        room_122.insertedId
    ]
})

db.complaints.insertMany([
    {
        "автор":cust_1.insertedId,
        "фамилия":"петров",
        "имя":"петр",
        "отчество":"петрович",
        "номер телефона":"8(999)123-12-12",
        "текст":"грубые сотрудники!!!"
    },
    {
        "автор":cust_1.insertedId,
        "фамилия":"петров",
        "имя":"петр",
        "отчество":"петрович",
        "номер телефона":"8(999)123-12-12",
        "текст":"в номере было грязно"
    },
    {
        "автор":cust_1.insertedId,
        "фамилия":"петров",
        "имя":"петр",
        "отчество":"петрович",
        "номер телефона":"8(999)123-12-12",
        "текст":"бассейн не работал"
    },
    {
        "автор":cust_1.insertedId,
        "фамилия":"петров",
        "имя":"петр",
        "отчество":"петрович",
        "номер телефона":"8(999)123-12-12",
        "текст":"сауна отстой"
    },
    {
        "автор":cust_1.insertedId,
        "фамилия":"петров",
        "имя":"петр",
        "отчество":"петрович",
        "номер телефона":"8(999)123-12-12",
        "текст":"сломался лифт"
    },
])