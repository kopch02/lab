from flask import Flask, url_for, render_template, redirect, send_from_directory, abort, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.jobs import Categories
from data.jobs import Link
from data.departament import Departament
from forms.user import RegisterForm, LoginForm
from forms.authorization import AuthorizationForm
from forms.job import JobsForm
from forms.deportament import DeportamentForm
from num1 import add_user, add_departament, add_jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


@app.route('/')
@app.route('/index')
def index():
    param = {}
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        categories = db_sess.query(Categories).all()
        jobs = db_sess.query(Jobs).all()
        param["categories"] = categories
        param["jobs"] = jobs
        param["header"] = "Все работы"
        return render_template('index.html', **param)
    else:
        return render_template('authorization.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        add_user(form.surname.data,
                 form.name.data,
                 form.age.data,
                 form.position.data,
                 form.speciality.data,
                 form.addres.data,
                 form.email.data,
                 passworld=form.password.data)
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if not (user):
            return render_template(
                'login.html',
                title='Вход',
                form=form,
                message="Пользователь с такой почтой не найден")
        if not (user.check_password(form.password.data)):
            return render_template('login.html',
                                   title='Вход',
                                   form=form,
                                   message="Не правильный пароль")
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login.html', title='Вход', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/add_job', methods=['GET', 'POST'])
@login_required
def add_job():
    db_sess = db_session.create_session()
    form = JobsForm()
    team_list = db_sess.query(User).all()
    categori_list = db_sess.query(Categories).all()
    form.team_leader.choices = [(user.id, user.name + " " + user.surname)
                                for user in team_list]
    form.collaborators.choices = [(user.id, user.name + " " + user.surname)
                                  for user in team_list]
    form.categori.choices = [(categoria.id, categoria.title)
                             for categoria in categori_list]
    if form.validate_on_submit():
        collaborators = ""
        for i in form.collaborators.data:
            collaborators += str(int(i)) + ";"
        #sost = request.form['team_leader']
        #temp = request.form['temp']
        #print(type(form.team_leader.data))
        add_jobs(int(form.team_leader.data),
                 form.job.data,
                 form.work_size.data,
                 collaborators,
                 is_finished=form.is_finished.data,
                 categori=form.categori.data)

        return redirect('/')
    return render_template('add_job.html', title='Опять работать? ', form=form)


@app.route('/delete_job/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_job(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if job:
        links = db_sess.query(Link).filter(Link.jobs_id == id).all()
        if links:
            for i in links:
                db_sess.delete(i)
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/job/<int:id>', methods=['GET', 'POST'])
@login_required
def job_editing(id):
    form = JobsForm()
    db_sess = db_session.create_session()
    team_list = db_sess.query(User).all()
    categori_list = db_sess.query(Categories).all()
    form.team_leader.choices = [(user.id, user.name + " " + user.surname)
                                for user in team_list]
    form.collaborators.choices = [(user.id, user.name + " " + user.surname)
                                  for user in team_list]
    form.categori.choices = [(categoria.id, categoria.title)
                             for categoria in categori_list]
    if request.method == "GET":
        job = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if job:
            form.team_leader.data = str(job.user)
            form.job.data = job.job
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.is_finished.data = job.is_finished
            form.categori.data = job.categories
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if job:

            job.team_leader = form.team_leader.data
            job.job = form.job.data
            job.work_size = form.work_size.data
            job.is_finished = form.is_finished.data
            collaborators = ""
            for i in form.collaborators.data:
                collaborators += str(int(i)) + ";"
            job.collaborators = collaborators
            if form.is_finished.data:
                cat = db_sess.query(Categories).filter_by(
                    title="Завершённые").first()
                job.categories.append(cat)
            else:
                cat = db_sess.query(Categories).filter_by(
                    title="Завершённые").first()
                if cat in job.categories:
                    links = db_sess.query(Link).filter(
                        Link.jobs_id == job.id,
                        Link.categories_id == cat.id).all()
                    if links:
                        for i in links:
                            db_sess.delete(i)
            db_sess.commit()
            return redirect("/")
        else:
            abort(404)
    return render_template("add_job.html",
                           title="Редактирование работы",
                           form=form)


@app.route('/deportaments', methods=['GET', 'POST'])
@login_required
def deportaments():
    db_sess = db_session.create_session()
    deps = db_sess.query(Departament).all()
    return render_template("deportaments.html", deps=deps)


@app.route('/delete_deportament/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_deportaments(id):
    db_sess = db_session.create_session()
    deportament = db_sess.query(Departament).filter(
        Departament.id == id, ).first()
    if deportament:
        db_sess.delete(deportament)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/add_deportament', methods=['GET', 'POST'])
@login_required
def add_departaments():
    db_sess = db_session.create_session()
    form = DeportamentForm()
    team_list = db_sess.query(User).all()
    form.chief.choices = [(user.id, user.name + " " + user.surname)
                          for user in team_list]
    form.members.choices = [(user.id, user.name + " " + user.surname)
                            for user in team_list]
    if form.validate_on_submit():
        members = ""
        for i in form.members.data:
            members += str(int(i)) + ";"
        add_departament(form.title.data, int(form.chief.data), members,
                        form.email.data)
        return redirect('/')
    return render_template('add_deportament.html',
                           title='Новый депортамент? ',
                           form=form)


@app.route('/deportament/<int:id>', methods=['GET', 'POST'])
@login_required
def deportament_editing(id):
    form = DeportamentForm()
    db_sess = db_session.create_session()
    team_list = db_sess.query(User).all()
    form.chief.choices = [(user.id, user.name + " " + user.surname)
                          for user in team_list]
    form.members.choices = [(user.id, user.name + " " + user.surname)
                            for user in team_list]
    if request.method == "GET":
        departament = db_sess.query(Departament).filter(
            Departament.id == id).first()
        if departament:
            form.title.data = departament.title
            form.chief.data = str(departament.chief)
            form.members.data = departament.members
            form.email.data = departament.email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        departament = db_sess.query(Departament).filter(
            Departament.id == id).first()
        if departament:
            departament.title = form.title.data
            departament.chief = form.chief.data
            departament.email = form.email.data
            members = ""
            for i in form.members.data:
                members += str(int(i)) + ";"
            departament.members = members
            db_sess.commit()
            return redirect("/")
        else:
            abort(404)
    return render_template("add_deportament.html",
                           title="Редактирование депортамента",
                           form=form)


@app.route('/authorization')
def authorization():
    form = AuthorizationForm()
    return render_template('authorization.html', form=form)


@app.route('/categories/<int:id>', methods=['GET', 'POST'])
@login_required
def categories(id):
    param = {}
    db_sess = db_session.create_session()
    categori = db_sess.query(Categories).filter_by(id=id).first()
    param["categori_title"] = categori.title
    param["jobs"] = categori.jobs
    return render_template("categories.html", **param)


if __name__ == '__main__':
    main()