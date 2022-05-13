from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from datetime import datetime, date
from random import randint
from config import telegram_token

reply_keyboard = [['/time', '/date'], 
                    ['/dice', '/timer']]
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


def tg_start(update, context):
    update.message.reply_text("Что вам нужно?", reply_markup=markup)


def close_keyboard(update, context):
    update.message.reply_text("Ok", reply_markup=ReplyKeyboardRemove())


def echo(update, context):
    
    if update.message.text == "qwe":
        update.message.reply_text("zxc")
        
    else:
        update.message.reply_text(update.message.text)
        print(update.message.from_user)


def time_bot(update, context):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    update.message.reply_text(current_time)


def date_bot(update, context):
    current_date = date.today()
    update.message.reply_text(str(current_date))


def dice(update, context):
    update.message.reply_text("какой кубик боросить?",
                              reply_markup=markup_dice)


def one_six_sided(update, context):
    update.message.reply_text(str(randint(1, 6)))


def two_six_sided(update, context):
    update.message.reply_text(str(randint(1, 6)) + "  " + str(randint(1, 6)))


def twinty_sided(update, context):
    update.message.reply_text(str(randint(1, 20)))


def timer(update, context):
    update.message.reply_text("нсколько поставить таймер?",
                              reply_markup=markup_timer)


def back(update, context):
    update.message.reply_text("что-то ещё?", reply_markup=markup)


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
            update.message.reply_text(
                'Извините, не умеем возвращаться в прошлое')
            return

        print(context.chat_data)
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        print(context.chat_data)
        if due == 30:
            new_job = context.job_queue.run_once(callback30, due, context=chat_id)
        if due == 60:
            new_job = context.job_queue.run_once(callback60, due, context=chat_id)
        if due == 300:
            new_job = context.job_queue.run_once(callback300, due, context=chat_id)
        context.chat_data['job'] = new_job
        update.message.reply_text(f'Вернусь через {due} секунд')
    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <секунд>')


def callback30(context):
    job = context.job
    context.bot.send_message(job.context, text="30 секунд истекли")


def callback60(context):
    job = context.job
    context.bot.send_message(job.context, text="1 минута истекла")


def callback300(context):
    job = context.job
    context.bot.send_message(job.context, text="5 минут истекли")


def unset_timer(update, context):
    if 'job' not in context.chat_data:
        update.message.reply_text('Нет активного таймера')
        return
    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']
    update.message.reply_text('Хорошо, вернулся сейчас!')
                        

def main():
    updater = Updater(telegram_token,use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("close", close_keyboard))

    dp.add_handler(CommandHandler("time", time_bot))
    dp.add_handler(CommandHandler("date", date_bot))
    dp.add_handler(CommandHandler("dice", dice))
    dp.add_handler(CommandHandler("timer", timer))
    dp.add_handler(CommandHandler("back", back))

    dp.add_handler(CommandHandler("1_six_sided", one_six_sided))
    dp.add_handler(CommandHandler("2_six_sided", two_six_sided))
    dp.add_handler(CommandHandler("20_sided", twinty_sided))

    dp.add_handler(CommandHandler("set",set_timer))
    dp.add_handler(CommandHandler("reset", unset_timer, pass_chat_data=True))

    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
