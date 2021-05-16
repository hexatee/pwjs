from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    dane = {'tytul': 'O mnie', 'tresc': 'Konrad Błaszkiewicz Nr albumu: 19324'}
    return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/informacje')
def informacje():
    informacje = [{
        'author':{'username':'Konrad'},
        'body':'Jest to zadanie 4 z laboratorium nr 11'
    },{
        'author':{'username':'Kasia'},
        'body':'Jest słonecznie w Elblągu!'
    }]
    return render_template('informacje.html', tytul='Informacje', informacje=informacje)




if __name__=='__main__':
    app.run(debug=True)