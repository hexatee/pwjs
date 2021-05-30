from flask import Flask, render_template, request
import sqlite3


app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dodaj')
def dodaj():
    return render_template('dodaj.html', tytul="Dodaj pracownika")

@app.route('/dodajrekord', methods=['POST','GET'])
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