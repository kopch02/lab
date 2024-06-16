db = connect( 'mongodb://localhost/lab8' );
db.articles.insertMany([
    {
        title: "Икона",
        autor: "Иванов",
        date_of_public: new Date("05.06.2002"),
        text: "1",
        tags: ["бог", "святой"],
        comments: [{
            name:"User1.1",
            text_comment: "text1.1",
            raiting: 6,
        },
        {
            name:"User1.2",
            text_comment: "text1.2",
            raiting: 5,
        }],
    },

    {
        title: "Бег",
        autor: "Хопта",
        date_of_public: new Date("25.07.2012"),
        text: "2",
        tags: ["спорт", "выносливость"],
        comments: [{
            name:"User2.1",
            text_comment: "text2.1",
            raiting: 8,
        },
        {
            name:"Иванов",
            text_comment: "text2.2",
            raiting: 7,
        }],
    },

    {
        title: "Мусор",
        autor: "Белов",
        date_of_public: new Date("01.01.2001"),
        text: "3",
        tags: ["грязь"],
        comments: [{
            name:"Хопта",
            text_comment: "text3.1",
            raiting: 3,
        },
        {
            name:"User3.2",
            text_comment: "text3.2",
            raiting: 9,
        }],
    },

    {
        title: "Школа",
        autor: "Набоков",
        date_of_public: new Date("04.06.1999"),
        text: "4",
        tags: ["радость"],
        comments: [{
            name:"User4.1",
            text_comment: "text4.1",
            raiting: 2,
        },
        {
            name:"User4.2",
            text_comment: "text4.2",
            raiting: 2,
        }],
    },

    {
        title: "Еда",
        autor: "Кучер",
        date_of_public: new Date("06.07.1989"),
        text: "5",
        tags: ["производная"],
        comments: [{
            name:"User5.1",
            text_comment: "text5.1",
            raiting: 10,
        },
        {
            name:"User5.2",
            text_comment: "text5.2",
            raiting: 10,
        }],
    },

    {
        title: "Супер статья",
        autor: "Тестировщик",
        date_of_public: new Date("06.07.2022"),
        text: "тестируем",
        tags: ["тесты","мега тесты"],
        comments: [{
            name:"User222",
            text_comment: "я тут единственный",
            raiting: 10,
        }
        ],
    }
]
)