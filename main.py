import datetime
from os import abort

# http://127.0.0.1:5000
from flask import Flask, render_template, request, make_response, session
# noinspection PyUnresolvedReferences
from data import db_session
# noinspection PyUnresolvedReferences
# from data.users import User
from data.corp import Corp
from data.corps_next import CorpNext
from data.corps_another import CorpAnother
# noinspection PyUnresolvedReferences
from data.news import News
# noinspection PyUnresolvedReferences
# from forms.user import RegisterForm
from forms.corps import RegisterForm
# noinspection PyUnresolvedReferences
from forms.news import NewsForm
from werkzeug.utils import redirect
import flask_login
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from forms.join import Join
from forms.corp_rek import CorpRek
from forms.corp_tov import CorpTov


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def load_user(user_id):
    db_sess = db_session.create_session ()
    return db_sess.query ( User ).get ( user_id )


def main():
    db_session.global_init ( "db/corp.db" )

    # user = User()
    # user.name = "kolay"
    # user.about = "биография пользователя kolay"
    # user.email = "email.kondakov@email.ru"
    # user.set_password("123")
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    # for user in db_sess.query ( User ).all ():
    #     print ( user )
    # for user in db_sess.query ( User ).filter ( User.id > 1, User.email.notilike ( "%1%" ) ):
    #     print ( user )
    # for user in db_sess.query ( User ).filter ( (User.id > 2)  ):
    #     print ( user )
    # user = db_sess.query ( User ).filter ( User.id == 1 ).first ()
    # print ( user )
    # user.name = "Измененное имя пользователя"
    # user.created_date = datetime.datetime.now ()
    # db_sess.commit ()
    # db_sess.query ( User ).filter ( User.id >= 3 ).delete ()
    # db_sess.commit ()
    # user = db_sess.query ( User ).filter ( User.id == 2 ).first ()
    #     # db_sess.delete ( user )
    #     # db_sess.commit ()
    # news = News ( title="Первая новость", content="Привет блог!",
    #               user_id=1, is_private=False )
    # db_sess.add ( news )
    # db_sess.commit ()
    # user = db_sess.query ( User ).filter ( User.id == 1 ).first ()
    # news = News ( title="Вторая новость", content="Уже вторая запись!",
    #               user=user, is_private=False )
    # db_sess.add ( news )
    # db_sess.commit ()
    # user = db_sess.query ( User ).filter ( User.id == 1 ).first ()
    # news = News ( title="Личная запись", content="Эта запись личная",
    #               is_private=True )
    # user.news.append ( news )
    # for news in user.news:
    #     print ( news)
    # db_sess.commit ()

    # @app.route('/', methods=['GET', 'POST'])
    # def test():
    #     return render_template ( 'test.html', title='Main')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template ( 'index.html', title='Main')

    @app.route('/join', methods=['GET', 'POST'])
    def join():
        form = Join()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            user = db_sess.query(Corp).filter(Corp.name == form.name.data).first()
            if user and user.check_password(form.password.data):
                # login_user(user, remember=form.remember_me.data)
                return redirect("/main")
            return render_template('join.html', title='Регистрация', form=form, message="Неверный ПАРОЛЬ или ИМЯ организации")
        return render_template('join.html', title='Регистрация', form=form)

    @app.route ( '/register', methods=['GET', 'POST'] )
    def reqister():
        form = RegisterForm ()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template ( 'register.html', title='Регистрация',
                                         form=form,
                                         message="Пароли не совпадают" )
            db_sess = db_session.create_session ()
            if db_sess.query ( Corp ).filter ( Corp.email == form.email.data ).first ():
                return render_template ( 'register.html', title='Регистрация',
                                         form=form,
                                         message="Такой пользователь уже есть" )
            corp = Corp (
                name=form.name.data,
                email=form.email.data,
                fon_num=form.fon_num.data
            )
            corp.set_password ( form.password.data )
            db_sess.add ( corp )
            db_sess.commit ()
            return redirect ( '/login' )
        return render_template ( 'register.html', title='Регистрация', form=form )

    @app.route ( '/login', methods=['GET', 'POST'] )
    def login():
        form = RegisterForm()
        return render_template("login.html", title='Регистрация', form=form)

    @app.route ( '/login_rek', methods=['GET', 'POST'] )
    def login_rek():
        form = CorpRek()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            corp = CorpNext(
                sphere=request.form['Sphere'],
                prize=form.prize.data,
                count=request.form['Viewers'],
                age=request.form['Viewers_Age'],
                about=form.about.data,
            )
            db_sess.add(corp)
            db_sess.commit()
            return redirect('/main')
        return render_template("login_rek.html", title='Регистрация', form=form)

    @app.route('/login_tov', methods=['GET', 'POST'])
    def login_tov():
        form = CorpTov()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            corp = CorpAnother(
                name=form.name.data,
                sphere=request.form['Sphere'],
                prize=form.prize.data,
                about=form.about.data,
            )
            db_sess.add(corp)
            db_sess.commit()
            return redirect('/main')
        return render_template("login_tov.html", title='Регистрация', form=form)

    @app.route ( '/main', methods=['GET', 'POST'] )
    def main_menu():
        return render_template("main.html")

    @app.route("/start")
    def start():
        return render_template("start.html")

    app.run()


if __name__ == '__main__':
    main()
