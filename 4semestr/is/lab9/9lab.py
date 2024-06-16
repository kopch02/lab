from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler ,CallbackQueryHandler
from telegram import CallbackQuery, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton
from datetime import datetime, date
from random import randint
from config import telegram_token
from config import kino_token
import codecs
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.film_request import FilmRequest
from kinopoisk_unofficial.request.films.filters_request import FiltersRequest
from kinopoisk_unofficial.model.filter_country import FilterCountry
from kinopoisk_unofficial.model.filter_genre import FilterGenre
from kinopoisk_unofficial.model.filter_order import FilterOrder
from kinopoisk_unofficial.request.films.film_search_by_filters_request import FilmSearchByFiltersRequest
from kinopoisk_unofficial.request.persons.person_by_name_request import PersonByNameRequest
from kinopoisk_unofficial.request.films.facts_request import FactsRequest


api_client = KinopoiskApiClient(kino_token)


start_text='''Привет, я обычный бот и вот, что я могу:
Повторять все твои сообщения, если я не знаю, что с ними делать
Бросать кубики
Ставить таймер
присылать случаный фильм драмму и комедию
их оценку на кинопоиске 
и сслыку на кинопоиск

В будующем я смогу больше!'''

reply_keyboard = [ ['/dice', '/timer'],
                    ["/films комедия","/films драма"],
                    ["/person"]]
dice_keyboard = [['/1_six_sided', '/2_six_sided'], 
                    ['/20_sided', '/back']]
timer_keyboard = [['/set 30sec', '/set 1min'], 
                    ['/set 5min', '/reset'], 
                    ["/back"]]

markup_dice = ReplyKeyboardMarkup(dice_keyboard,
                                  one_time_keyboard=False,
                                  resize_keyboard=True)
markup_timer = ReplyKeyboardMarkup(timer_keyboard,
                                   one_time_keyboard=False,
                                   resize_keyboard=True)
markup = ReplyKeyboardMarkup(reply_keyboard,
                             one_time_keyboard=False,
                             resize_keyboard=True)


def log_whire(update,bot_text="",bot_text_list=[]):
    try:
        id=update.message.from_user["id"]
    except:
        id=bot_text["chat"]["id"]
        bot_text=bot_text["text"]
    with codecs.open("4semestr\\is\\lab9\\telelog\\{name}.log".format(name=str(id)),"a", "utf-8") as idlog:
        try:
            text= str(update.message.text+"\n")
            idlog.write("user: "+text)
        except:
            idlog.write("user: "+" ")
        try:
            for text in bot_text_list:
                idlog.write("bot: "+text["text"]+"\n")
            idlog.write("\n")
        except:
            pass
        idlog.write("bot: "+bot_text+"\n"+"\n")
        
        


def tg_start(update, context):
    update.message.reply_text(start_text, reply_markup=markup)
    log_whire(update)



def close_keyboard(update, context):
    update.message.reply_text("Ok", reply_markup=ReplyKeyboardRemove())


def echo(update, context):
    
    if update.message.text == "qwe":
        bot_text=update.message.reply_text("zxc")
        
    else:
        bot_text=update.message.reply_text(update.message.text)
    log_whire(update,bot_text["text"])


def dice(update, context):
    bot_text=update.message.reply_text("какой кубик боросить?",
                              reply_markup=markup_dice)
    log_whire(update,bot_text["text"])




def one_six_sided(update, context):
    bot_text=update.message.reply_text(str(randint(1, 6)))
    log_whire(update,bot_text["text"])




def two_six_sided(update, context):
    bot_text=update.message.reply_text(str(randint(1, 6)) + "  " + str(randint(1, 6)))
    log_whire(update,bot_text["text"])




def twinty_sided(update, context):
    bot_text=update.message.reply_text(str(randint(1, 20)))
    log_whire(update,bot_text["text"])




def timer(update, context):
    bot_text=update.message.reply_text("на сколько поставить таймер?"+"\n вы можете использовать /set 'нужное вам количество секунд'",
                              reply_markup=markup_timer)
    log_whire(update,bot_text["text"])




def back(update, context):
    bot_text=update.message.reply_text("что-то ещё?", reply_markup=markup)
    log_whire(update,bot_text["text"])



def set_timer(update, context):
    """Добавляем задачу в очередь"""
    chat_id = update.message.chat_id
    try:
        if context.args[0]=="30sec":
            due =30
        elif context.args[0]=="1min":
            due =60
        elif context.args[0]=="5min":
            due =300
        else:
            due = int(context.args[0])
        if due < 0:
            bot_text=update.message.reply_text(
                'Извините, не умеем возвращаться в прошлое')
            return

        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        if due == 30:
            new_job = context.job_queue.run_once(callback30, due, context=chat_id)
        elif due == 60:
            new_job = context.job_queue.run_once(callback60, due, context=chat_id)
        elif due == 300:
            new_job = context.job_queue.run_once(callback300, due, context=chat_id)
        else:
            new_job = context.job_queue.run_once(callback, due, context=chat_id)
        context.chat_data['job'] = new_job
        bot_text=update.message.reply_text(f'Вернусь через {due} секунд')
    except (IndexError, ValueError):
        bot_text=update.message.reply_text('Использование: /set <секунд>')
    log_whire(update,bot_text["text"])



def callback(update):
    job = update.job
    bot_text=update.bot.send_message(job.context, text="время истекло")
    log_whire(update,bot_text["text"])



def callback30(update):
    job = update.job
    bot_text=update.bot.send_message(job.context, text="30 секунд истекли")
    log_whire(update,bot_text["text"])



def callback60(update):
    job = update.job
    bot_text=update.bot.send_message(job.context, text="1 минута истекла")
    log_whire(update,bot_text["text"])



def callback300(update):
    job = update.job
    bot_text=update.bot.send_message(job.context, text="5 минут истекли")
    log_whire(update,bot_text["text"])



def unset_timer(update,context):
    if 'job' not in context.chat_data:
        bot_text=update.message.reply_text('Нет активного таймера')
        return
    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']
    bot_text=update.message.reply_text('Хорошо, вернулся сейчас!')
    log_whire(update,bot_text["text"])

                        

def random_i(update, _):
    keyboard_dice = [
        [
            InlineKeyboardButton("1 шестигранный", callback_data='1_dice'),
            InlineKeyboardButton("2 шестигранных", callback_data='2_dice'),

        ],
        [   InlineKeyboardButton("1 двадцатигранный", callback_data='3_dice'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard_dice)
    bot_text=update.message.reply_text('Какой кубик бросить?:', reply_markup=reply_markup)
    log_whire(update,bot_text["text"])



def button(update, _):
    query = update.callback_query
    variant = query.data

    query.answer()
    if variant =="1_dice":
        bot_text=query.message.reply_text(str(randint(1, 6)))
    elif variant =="2_dice":
        bot_text=query.message.reply_text(str(randint(1, 6)) + "  " + str(randint(1, 6)))
    elif variant =="3_dice":
        bot_text=query.message.reply_text(str(randint(1, 20)))
    log_whire(update,bot_text)


def films(update,context):

    request = FilmSearchByFiltersRequest()
    request.genres=[]
    bot_text_list=[]
    if context.args[0]=="драма":
        request.year_from = 2021
        request.rating_from = 5
        request.order = FilterOrder.RATING
        request.add_genre(FilterGenre(8, 'драма'))
        response = api_client.films.send_film_search_by_filters_request(request)
        num=randint(0,len(response.items)-1)
        bot_text_list.append(update.message.reply_text("название фильма: "+response.items[num].name_ru))
        bot_text_list.append(update.message.reply_text("оценка на кинопоиске: "+str(response.items[num].rating_kinopoisk)))
        bot_text_list.append(update.message.reply_text("ссылка на кинопоиск :\n "+"https://www.kinopoisk.ru/series/{id}/".format(id=response.items[num].kinopoisk_id)))
        request = FactsRequest(response.items[num].kinopoisk_id)
        response = api_client.films.send_facts_request(request)
        try:
            bot_text_list.append(update.message.reply_text("Интересный факт: "+response.items[0].text))
        except:
            pass

    elif context.args[0]=="комедия":
        request.year_from = 2021
        request.rating_from = 5
        request.order = FilterOrder.RATING
        request.add_genre(FilterGenre(6, 'комедия'))
        response = api_client.films.send_film_search_by_filters_request(request)
        num=randint(0,len(response.items)-1)
        bot_text_list.append(update.message.reply_text("название фильма: "+response.items[num].name_ru))
        bot_text_list.append(update.message.reply_text("оценка на кинопоиске: "+str(response.items[num].rating_kinopoisk)))
        bot_text_list.append(update.message.reply_text("ссылка на кинопоиск :\n "+"https://www.kinopoisk.ru/series/{id}/".format(id=response.items[num].kinopoisk_id)))
        request = FactsRequest(response.items[num].kinopoisk_id)
        response = api_client.films.send_facts_request(request)
        try:
            bot_text_list.append(update.message.reply_text("Интересный факт: "+response.items[0].text))
        except:
            pass
    log_whire(update,bot_text_list=bot_text_list)


def person(update,context):
    try:
        request = PersonByNameRequest("{pers}".format(pers=context.args[0])+" "+"{pers}".format(pers=context.args[1]))
        response = api_client.persons.send_person_by_name_request(request)
        bot_text=update.message.reply_text("ссылка на кинопоиск: "+response.items[0].web_url)
    except:
        bot_text=update.message.reply_text("используйте /person Имя Фамилия\nдля интересующего вас актёра или режисёра\nесли вы писали правильно, но видите это, значит я не справился((...")
    log_whire(update,bot_text["text"])

def main():
    updater = Updater(telegram_token,use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("close", close_keyboard))

    dp.add_handler(CommandHandler("dice", random_i))
    dp.add_handler(CommandHandler("timer", timer))
    dp.add_handler(CommandHandler("back", back))

    dp.add_handler(CommandHandler("1_six_sided", one_six_sided))
    dp.add_handler(CommandHandler("2_six_sided", two_six_sided))
    dp.add_handler(CommandHandler("20_sided", twinty_sided))

    dp.add_handler(CommandHandler("set",set_timer))
    dp.add_handler(CommandHandler("reset", unset_timer, pass_chat_data=True))

    dp.add_handler(CommandHandler("random",random_i))

    dp.add_handler(CommandHandler("films",films))
    dp.add_handler(CommandHandler("person",person))


    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    #conv_handler = ConversationHandler(
    #    entry_points=[CommandHandler('start', tg_start)],
    #    states={ # словарь состояний разговора, возвращаемых callback функциями
    #        FIRST: [
    #            CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
    #            CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
    #            CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
    #            CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
    #        ],
    #        SECOND: [
    #            CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
    #            CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
    #        ],
    #    },
    #    fallbacks=[CommandHandler('start', tg_start)],
    #)

    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
