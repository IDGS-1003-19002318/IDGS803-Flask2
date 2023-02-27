class Translator:

    def guardarTraduccion(self, form):
        palabras = []
        form = form.data
        if form["idioma"] == '1':
            palabras.append(form["palabra"].lower())  # Español
            palabras.append(form["traduccion"].lower())  # Ingles
        else:
            palabras.append(form["traduccion"].lower())  # Español
            palabras.append(form["palabra"].lower())  # Ingles
        f = open('traducciones.txt', 'a')  # if not exists create but if exist append
        f.write('\n' + ','.join(palabras))
        f.close()

    def traerTraduccion(self, form):
        traduccion = ''
        form = form.data
        f = open('traducciones.txt', 'r')
        f.seek(1)
        palabras = f.readlines()
        if palabras:
            if form['idioma'] == '1':
                for item in palabras:
                    if item.split(',')[0] == form['palabra']:
                        traduccion = item.split(',')[1].replace('\n', '')
                        break
            else:
                for item in palabras:
                    if item.split(',')[1].replace('\n', '') == form['palabra']:
                        traduccion = item.split(',')[0]
                        break
        else:
            traduccion = "No hay traducciones"
        return traduccion
