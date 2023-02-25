from collections import Counter
from flask import Flask, render_template, redirect, url_for, request
import forms

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def cajaDinamica():
    numeros = []
    contadores = {}
    minimo = 0
    maximo = 0
    promedio = 0
    numeros_form = forms.NumeroForm(request.form)
    if request.method == 'POST':
        if len(request.form) > 1:
            for i in range(len(request.form)):
                num = int(request.form.get('num' + str(i)))
                numeros.append(num)
            minimo = min(numeros)
            maximo = max(numeros)
            promedio = sum(numeros) // len(numeros)
            counter = Counter(numeros)
            contadores = dict(counter)
    return render_template('cajadinamica.html', form=numeros_form, numeros=numeros, minimo=minimo, maximo=maximo,
                           contadores=contadores, promedio=promedio)


if __name__ == '__main__':
    app.run(debug=True, port = 3000)
