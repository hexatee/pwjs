from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    dane = {'tytul': 'O mnie', 'tresc': 'Konrad Błaszkiewicz Nr albumu: 19324'}
    return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/about/<name>')
def user(name):
    return render_template('omnie.html', tytul=f'Witaj, {name}', tresc=f'{name}, witaj na swojej stronie!')



if __name__=='__main__':
    app.run(debug=True)