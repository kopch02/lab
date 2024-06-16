from flask import Flask, url_for, render_template, redirect, send_from_directory
from loginform import LoginForm
import json
import random
import os
import smtplib 
from string import Template 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText


app = Flask(__name__)
app.config["PHOTO_FOLDER"] = os.path.join(app.root_path,"members","photo")

app.config['SECRET_KEY'] = 'my_secret_key'
profs = [
    'садовод', 'рабочий', 'инженер', 'пилот', 'строитель', 'врач',
    'климатолог', 'астрогеолог', 'гляциолог', 'киберинженер'
]
urls = ['/index', '/list_prof']


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Добро пожаловать!'
    #param['urls'] = urls
    param['h1'] = "Миссия Колонизация Марса"
    param['h4'] = "И на Марсе будут яблони цвести!"
    redirect('/success')
    return render_template('index.html', **param)


@app.route('/list_prof/<list>')
def list_prof(list):
    param = {}
    param['title'] = "Список профессий"
    param['list_prof'] = profs
    param['list'] = list
    return render_template('list_prof.html', **param)


@app.route('/distribution')
def distribution():
    param = {}
    with open("members//crew.json", "r") as json_file:
        members_load = json.load(json_file)
        param['members'] = members_load
    param['title'] = "Размещение"
    return render_template('distribution.html', **param)



@app.route('/photo/<path:name>')
def photo(name):
    return send_from_directory(app.config["PHOTO_FOLDER"],name,as_attachment = True)

@app.route('/member/<int:number>')
def member_num(number = None):
    param = {}
    with open("members//crew.json", "r") as json_file:
        members_load = json.load(json_file)
        #param['url'] = url_for('static', filename=members_load[number]["photo"])
        param['members'] = members_load
    param['title'] = "Член экипажа"
    param['number'] = number
    return render_template('member.html', **param)


@app.route('/member/random')
def member_random():
    param = {}
    number = random.randint(0,9)
    with open("members//crew.json", "r") as json_file:
        members_load = json.load(json_file)
        #param['url'] = url_for('static', filename=members_load[number]["photo"])
        param['members'] = members_load
    param['title'] = "Член экипажа"
    param['number'] = None
    return render_template('member.html', **param)


@app.route('/room/<sex>/<int:age>')
def room(sex,age):
    param = {}
    param['title'] = "Оформление каюты"
    param['sex'] = sex
    param['age'] = age
    return render_template('room.html', **param)


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    param = {}
    param['title'] = "Запись добровольцем"
    form = LoginForm()
    param['form'] = form
    if form.validate_on_submit():
        print(form.data)
        
        #return redirect('/success')
    return render_template('astronaut_selection.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')