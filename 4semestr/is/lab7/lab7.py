from asyncio.windows_events import NULL
from email import message
from http import server
from tkinter import SE




def num1():
    class BigBell(object):
        def __init__(self):
            self.ding = "ding"
            self.dong = "dong"
            self.dzin = self.ding

        def sound(self):
            if self.dzin == self.ding:
                print(self.dzin)
                self.dzin = self.dong
            else:
                print(self.dzin)
                self.dzin = self.ding
    Bell = BigBell()
    Bell.sound()
    Bell.sound()
    Bell.sound()
    Bell.sound()




def num2():
    class balance(object):
        def __init__(self):
            self.weigth = 0

        def add_left(self, left):
            self.weigth += left

        def add_right(self, right):
            self.weigth -= right

        def result(self):
            if self.weigth > 0:
                print("L")
            elif self.weigth < 0:
                print("R")
            else:
                print("=")
                
    Balans = balance()
    Balans.add_left(100)
    Balans.add_right(102)

    Balans.result()


def num3():
    class Selector(object):
        def __init__(self, array):
            self.array = array

        def get_odds(self):
            for x in self.array:
                if x % 2 != 0:
                    print(x)

        def get_evens(self):
            for x in self.array:
                if x % 2 == 0:
                    print(x)
    sel = Selector([1, 2, 3, 4, 5, 5, 4, 4, 3, 6, 8, 9])
    sel.get_odds()
    print()
    sel.get_evens()


def num4():
    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other: object):
            if self.x == other.x:
                if self.y == other.y:
                    return True
            return False

    p1 = Point(10, 30)
    p2 = Point(10, 30)
    if p1 == p2:
        print("равны")
    else:
        print("не равны")


def num5():
    class ReversedList():
        def __init__(self, array):
            self.rev_list = array[::-1]

        def __len__(self):
            return len(self.rev_list)

        def __getitem__(self, a):
            return self.rev_list[a]

    a = [1, 2, 3, 4, 5, 6]
    r = ReversedList(a)
    print(r[1])
    print(len(r))


def num6():
    class SparseArray():
        def __init__(self):
            self.array = {}

        def __setitem__(self, key, value):
            self.array[key] = value

        def __getitem__(self, key):
            return self.array.get(key, 0)
    
    sparse=SparseArray()
    sparse[1]=9
    sparse[10]=1
    for x in range(11):
        print(sparse[x])
        
        
def num7():
    class Polynomial():
        def __init__(self,array):
            self.array=array
            
        def __getattribute__(self, __name: str):
            pass
        
        
def num9():
    class Triangle(object):
        def __init__(self,a,b,c):
            self.a=a
            self.b=b
            self.c=c
        def perimitr(self):
            return self.a+self.b+self.c
        
    class EquilateralTriange(Triangle):
        def __init__(self,a):
            super().__init__(a,a,a)
            
            
    t1=Triangle(10,20,30)
    print(t1.perimitr())
    t2=EquilateralTriange(50)
    print(t2.perimitr())
        
        
def num13():
    from math import fabs
    class Weapon(object):
        def __init__(self,name,damage,range):
            self.name=name
            self.damage=damage
            self.range=range
            
        def hit(self, actor, target):
            if target.is_alive():
                if fabs(actor.pos_x-target.pos_x)<=self.range:
                    print("врагу нанесён урон оружием %s в размере %s"%(self.name,self.damage))
                    target.hp-=self.damage
                else:
                    print("враг слишком далеко для оружия ",self.name)
            else:
                print("враг уже повержен")    
        
        def __str__(self):
            return self.name
        
    class BaseCharacter(object):
        def __init__(self,pos_x,pos_y,hp):
            self.pos_x=pos_x
            self.pos_y=pos_y
            self.hp=hp
        def move(self,delta_x,delta_y):
            self.pos_x=delta_x
            self.pos_y=delta_y
        def is_alive(self):
            if self.hp>0:
                return True
            else:
                return False
        def get_damage(self,amount):
            self.hp-=amount
        def get_coords(self):
            return tuple ([self.pos_x, self.pos_y])
    
    class BaseEnemy(BaseCharacter):
        def __init__(self, pos_x, pos_y,weapon, hp):
            super().__init__(pos_x, pos_y, hp)
            self.weapon=weapon
            
        def hit(self,target):
            if type(target) is MainHero:
                self.weapon.hit(self,target)
            else:
                print("могу ударить только главного героя")
        def __str__(self):
            print("Враг на позиции %s ,%s с оружием %s" %(self.pos_x,self.pos_y,self.weapon))
            
    class MainHero(BaseCharacter):
        def __init__(self, pos_x, pos_y,name, hp):
            super().__init__(pos_x, pos_y, hp)
            self.name=name
            self.weapon=[]
            self.current_weapon=NULL
        def hit(self,target):
            if self.current_weapon==NULL:
                print("я безоружен")
            else:
                if type(target)==BaseEnemy:
                    self.current_weapon.hit(self,target)
                else:
                    print("могу ударить только врага")
        def add_weapon(self,weapon):
            if type(weapon) is Weapon:
                self.weapon.append(weapon)
                print("подобрал",str(weapon))
                if self.current_weapon==NULL:
                    self.current_weapon=weapon
                    
            else:
                print("это не оружие")
        def next_weapon(self):
            if len(self.weapon)==0:
                print("я безоружен")
            elif len(self.weapon)==1:
                print("у меня только одно оружие")
            else:
                self.current_weapon=self.weapon[(self.weapon.index(self.current_weapon)+1)%len(self.weapon)]
                print("поменял оружие на",str(self.current_weapon))
        def heal(self,amount):
            self.hp+=amount
            if self.hp>200:
                self.hp=200
            print("подлечился, теперь здоровья ",self.hp)
            
    weapon1=Weapon("короткий меч",5,1)
    weapon2=Weapon("длинный меч",7,2)
    weapon3=Weapon("лук",3,10)
    weapon4=Weapon("лазерная орбитальная пушка",1000,1000)
    princess=BaseCharacter(100,100,100)
    arcger=BaseEnemy(50,50,weapon3,100)
    armored_swordsman=BaseEnemy(50,50,weapon2,500)
    arcger.hit(armored_swordsman)
    armored_swordsman.move(10,10)
    print(armored_swordsman.get_coords())
    main_hero=MainHero(0,0,"король артур",200)
    main_hero.hit(armored_swordsman)
    main_hero.next_weapon()
    main_hero.add_weapon(weapon1)
    main_hero.hit(armored_swordsman)
    main_hero.add_weapon(weapon4)
    main_hero.hit(armored_swordsman)
    main_hero.next_weapon()
    main_hero.hit(princess)
    main_hero.hit(armored_swordsman)
    main_hero.hit(armored_swordsman)
    
def num14():
    class User(object):
        def __init__(self):
            pass
        
      
    class Server(object):
        def __init__(self):
            self.mail={}
        def receive(self,user):
            if user in self.mail:
                print(self.mail[user])
                del self.mail[user]
            else:
                print("писем нет...(((")
        def add_mail(self,user,message):
            self.mail[user]=message
            
    class MailClient(object):
        def __init__(self,server,user):
            self.user=user
            self.server=server
        def receive_mail(self):
            return self.server.receive(self.user)
        def send_mail(self,user,message):
            self.server.add_mail(user,message)
            
    serv1=Server()
    serv2=Server()
    serv3=Server()
    
    s=["serv1","serv2","serv3"]
    
    def list_servera(s):
        print("доступные сервера:")
        for x in s:
            print(x)
        
    while True:
        print("что вы хотите сделать?")
        print("1 -- посмотреть список серверов")
        print("2 -- залогиниться на сервере")
        print("3 -- выйти")
        try:
            turn=int(input("-->"))
            if turn==3:
                quit()
            elif turn==1:    
                list_servera(s)
            elif turn==2:
                print("как вас зовут?")
                user_name=input("-->").lower()
                print("к какому серверу вы хотите подключиться?")
                server_name=input("-->").lower()
                if server_name in s:
                    if server_name==s[0]:
                        server_name=serv1
                    if server_name==s[1]:
                        server_name=serv2    
                    if server_name==s[2]:
                        server_name=serv3
                    client=MailClient(server_name,user_name)
                    print("подключение к серверу прошло успешно!")
                    while True:
                        print("1 -- отправить письмо")
                        print("2 -- проверить почту")
                        print("3 -- разлогиниться")
                        
                        turn=int(input("-->"))
                        if turn==3:
                            break
                        elif turn==2:
                            client.receive_mail()
                        elif turn==1:
                            recipient=input("кому отправить? -->")
                            message=input("текст письма -->")
                            client.send_mail(recipient,user_name+" - "+message)
                else:
                    print("такого сервера нет!!!")
        except ValueError:
            print("вы попытались ввести слово, там где нужно вводить цифры!!")
        
    
num14()