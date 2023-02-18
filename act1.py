from flask import Flask,render_template,redirect,url_for,request
import forms

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def cajaDinamica():
     numeros_form = forms.NumeroForm(request.form)
     if request.method == 'POST' :
          print(numeros_form.numero.data)
          if numeros_form.numero.data is not None:                   
               for i in range(int(numeros_form.numero.data)):
                    print(i)
                    print(request.form.get('num'+str(i)))
     return render_template('cajadinamica.html',form=numeros_form)
     

if __name__ == '__main__':
    app.run(debug=True)