import datetime
import sqlite3

con = sqlite3.connect("sadic.sqlite")
cursor = con.cursor()

EAT_PRICE = 27
HOUR_PRICE = 250
DAY_PRICE = 1200
STANDART_PRICE = 15600
OLD_PRICE = 13000


def save(cursor2):
    cursor2.execute("commit")


def insert_paymeant(cursor, id_ch, mm, cash):
    yy = datetime.datetime.now()
    yy = int(yy.year)
    paymeant = cursor.execute(f'''select MAX(id) from paymeant ''')
    for i in paymeant:
        try:
            max_id = i[0] + 1
        except TypeError as e:
            max_id = 1
    cursor.execute(
        f'''INSERT INTO paymeant VALUES({max_id}, {id_ch}, '{mm}.{yy}', {cash})'''
    )


def insert_children(cursor2, fio, tarif, lgota):
    children = cursor2.execute(f'''select MAX(id) from children ''')
    for i in children:
        max_id = i[0] + 1
    cursor2.execute(
        f'''INSERT INTO children VALUES({max_id}, '{fio}', '{tarif}', '{lgota}') '''
    )


def sum_cash(cursor, fio, mm):
    yy = datetime.datetime.now()
    yy = int(yy.year)
    children = cursor.execute(f'''select * from children
    where fio='{fio}' ''')
    for i in children:
        lgota = i[3]
        tarif = i[2]
        id = i[0]

    visiting = cursor.execute(f'''select * from visiting 
    where id_children={id} 
    AND date_ BETWEEN '{yy}-{mm}-01' AND '{yy}-{mm}-30'
    ''')
    day = 0
    eat = 0
    hours = 0
    for x in visiting:
        print(x)
        day += 1
        eat += x[5]
        start = datetime.datetime(int(x[2][6:10]), int(x[2][3:5]),
                                  int(x[2][:2]), int(x[2][11:13]),
                                  int(x[2][14:16]))
        end = datetime.datetime(int(x[3][6:10]), int(x[3][3:5]), int(x[3][:2]),
                                int(x[3][11:13]), int(x[3][14:16]))
        hours += int(str(end - start)[:-6])

    if tarif == 'полный':
        res = STANDART_PRICE + eat * EAT_PRICE

    elif tarif == 'старый':
        res = OLD_PRICE + eat * EAT_PRICE

    elif tarif == 'дневной':
        res = DAY_PRICE * day + eat * EAT_PRICE

    elif tarif == 'почасовой':
        res = HOUR_PRICE * hours + eat * EAT_PRICE

    else:
        print("Error")

    if lgota == "да":
        res //= 2

    #print(f"id ребёнка = {id}")
    #print(f"количество посещений = {day}")
    #print(f"количество часов = {hours}")
    #print(f"льгота = {lgota}")
    #print(f"тариф = {tarif}")
    #print(f"сколько раз поел = {eat}")
    #print(f"сумма за {mm} месяц = {res}")
    insert_paymeant(cursor, id, mm, res)

    #return res

    
def insert_visiting(id_ch, time_start, time_end, date, food):
    gosai = cursor.execute(f'''select MAX(id) from visiting ''')
    for i in gosai:
        max_id = i[0] + 1
    cursor.execute(
        f'''INSERT INTO visiting VALUES({max_id}, {id_ch}, '{time_start}', '{time_end}', '{date}', {food} '''
    )


cursor.close()
con.close()