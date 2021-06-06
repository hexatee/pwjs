from flask import Flask, render_template, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin,login_required, login_user, logout_user
import sqlite3


app=Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='sekretny_klucz'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self,id):
        self.id = id
        self.name = "user"+str(id)
        self.password = self.name+"_secret"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


users = [User(id) for id in range(1,10)]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "_secret":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(url_for("index"))
        else:
            return abort(401)
    else:
        return render_template('login.html', tytul='Zaloguj się')

@app.errorhandler(401)
def page_not_found(e):
    tytul="Coś poszło nie tak..."
    blad = "401"
    return render_template('blad.html', tytul=tytul, blad=blad)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('logout.html', tytul='Wylogowanie')

@login_manager.user_loader
def load_user(userid):
    return User(userid)


@app.route('/dodaj')
@login_required
def dodaj():
    return render_template('dodaj.html', tytul="Dodaj pracownika")

@app.route('/dodajrekord', methods=['POST','GET'])
@login_required
def dodajrekord():
    try:
        imienazwisko = request.form['imienazwisko']
        adres = request.form['adres']
        nrpracownika = request.form['nrpracownika']

        conn = sqlite3.connect('pracownicy.db')
        cr = conn.cursor()
        cr.execute("INSERT INTO pracownicy (nrpracownika,imienazwisko,adres) VALUES(?, ?, ?)",(nrpracownika,imienazwisko,adres))

        conn.commit()
        msg = "Rekord zapisany"
    except:
        cr.rollback()
        msg = "Blad przy dodawaniu rekordu"

    finally:
        conn.close()
        return render_template("rezultat.html", msg=msg)



@app.route('/lista')
@login_required
def lista():
    conn = sqlite3.connect('pracownicy.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM pracownicy ORDER BY imienazwisko')
    rekordy = c.fetchall();
    conn.close()
    return render_template('lista.html', tytul='Lista pracowników', rekordy=rekordy)




if __name__=='__main__':
    conn = sqlite3.connect('pracownicy.db')
    c = conn.cursor()
    c.execute('DROP TABLE pracownicy')
    c.execute('''CREATE TABLE pracownicy
             (nrpracownika text, imienazwisko text, adres text)''')
    prac = [('1','Konrad Błaszkiewicz','Wojska Polskiego 12'),
            ('2','Anna Kowalska','Słoneczna 10'),
            ('3','Kamil Ślimak','Grunwaldzka 23')]
    c.executemany('INSERT INTO pracownicy VALUES (?,?,?)', prac)
    conn.commit()
    conn.close()
    app.run(debug=True)