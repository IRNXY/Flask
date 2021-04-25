import sqlite3

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
from forms.free import Free
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
    #     form = RegisterForm ()
    #     # if form.validate_on_submit():
    #     #     if form.password.data != form.password_again.data:
    #     #         return render_template ( 'register.html', title='Регистрация',
    #     #                                  form=form,
    #     #                                  message="Пароли не совпадают" )
    #     #     db_sess = db_session.create_session ()
    #     #     if db_sess.query ( Corp ).filter ( Corp.name == form.name.data ).first ():
    #     #         return render_template ( 'register.html', title='Регистрация',
    #     #                                  form=form,
    #     #                                  message="Такой пользователь уже есть" )
    #     #     corp = Corp (
    #     #         name=form.name.data,
    #     #         email=form.email.data,
    #     #         fon_num=form.fon_num.data
    #     #     )
    #     #     corp.set_password ( form.password.data )
    #     #     db_sess.add ( corp )
    #     #     db_sess.commit ()
    #     #     return redirect ( '/login' )
    #     # db_sess = db_session.create_session()
    #     # user_search = db_sess.query(CorpNext.prize, CorpNext.about).filter(CorpNext.id > 0)
    #     # print(user_search[0])
    #     # user_search = [(1, 2), (3, 4)]
    #     # answ = []
    #     # for e, i in enumerate(user_search):
    #     #     if i:
    #     #         answ.append(("label_2" + str(e + 1), "btn_cont" + str(e)))
    #     # if user_search:
    #     #     print(answ)
    #     return render_template ('test.html', title='Main', form=form)

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
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Пароли не совпадают")
            db_sess = db_session.create_session()
            if db_sess.query(Corp).filter(Corp.name == form.name.data).first():
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Такой пользователь уже есть")

            name_main = form.name.data
            email = form.email.data
            fon_num = form.fon_num.data
            password = form.password.data

            return redirect('/login/' + name_main + '/' + email + '/' + fon_num + '/' + password)
        return render_template('register.html', title='Регистрация', form=form)

    @app.route (  '/login/<name_main>/<email>/<fon_num>/<password>', methods=['GET', 'POST'])
    def login(name_main, email, fon_num, password):
        print(name_main, email, fon_num, password)
        a = [(('/login_rek/' + name_main + '/' + email + '/' + fon_num + '/' + password),
              ('/login_tov/' + name_main + '/' + email + '/' + fon_num + '/' + password))]
        return render_template("login.html", title='Регистрация', a=a)

    @app.route('/login_rek/<name_main>/<email>/<fon_num>/<password>', methods=['GET', 'POST'])
    def login_rek(name_main, email, fon_num, password):
        form = CorpRek()
        if form.validate_on_submit():
            db_sess = db_session.create_session()

            corp = Corp(
                name=name_main,
                email=email,
                who="1",
                fon_num=fon_num
            )
            corp.set_password(password)
            db_sess.add(corp)

            corp = CorpNext(
                name=name_main,
                sphere=request.form['Sphere'],
                prize=form.prize.data,
                count=request.form['Viewers'],
                age=request.form['Viewers_Age'],
                about=request.form['text'],
            )
            db_sess.add(corp)
            db_sess.commit()
            return redirect('/main_menu/' + str(1))
        return render_template("login_rek.html", title='Регистрация', form=form)

    @app.route('/login_tov/<name_main>/<email>/<fon_num>/<password>', methods=['GET', 'POST'])
    def login_tov(name_main, email, fon_num, password):
        form = CorpTov()
        if form.validate_on_submit():
            db_sess = db_session.create_session()

            corp = Corp(
                name=name_main,
                email=email,
                who="2",
                fon_num=fon_num
            )
            corp.set_password(password)
            db_sess.add(corp)

            corp = CorpAnother(
                name_main=name_main,
                name=form.name.data,
                sphere=request.form['Sphere'],
                prize=form.prize.data,
                about=request.form['text'],
            )
            db_sess.add(corp)
            db_sess.commit()
            return redirect('/main_menu/' + str(2))
        return render_template("login_tov.html", title='Регистрация', form=form)

    @app.route('/main_menu/<type>', methods=['GET', 'POST'])
    def main_menu(type):
        answ = []
        form = Free()
        if not form.validate_on_submit() and type == "2":
            try:
                a = request.form['text']
                con = sqlite3.connect("corp.db")
                cur = con.cursor()
                result = cur.execute(f"""SELECT corp.name, corps_next.prize, corps_next.sphere, corps_next.count 
                                        FROM corp, corps_next WHERE corp.name = '{a}' AND corps_next.name = '{a}'""").fetchall()
                print(result)
                con.close()
                # db_sess = db_session.create_session()
                # user = db_sess.query(Corp).filter(Corp.name == a, Corp.name).first()
                answ = []
                for e, i in enumerate(result):
                    if i:
                        answ.append(("label_n_2" + str(e + 1), "btn_cont" + str(e + 1), "label_p_2" + str(e + 1),
                                     "label_s_2" + str(e + 1), "label_a_2" + str(e + 1), "label_p_-_2" + str(e + 1),
                                     "label_s_-_2" + str(e + 1), "label_a_-_2" + str(e + 1), i[0], i[1], i[2], i[3]))
                return render_template("main.html", user_search=answ, form=form)

            except Exception:
                print(21212)
                return render_template("main.html", user_search=answ, form=form)

        return render_template("main.html", user_search=answ, form=form)

    @app.route("/start")
    def start():
        return render_template("start.html")

    app.run()


if __name__ == '__main__':
    main()
