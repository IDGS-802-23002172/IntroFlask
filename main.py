from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    titulo="IDGS-802-Flask"
    lista= ['Juan', 'Karla', 'Miguel', 'Ana']
    return render_template('index.html',titulo=titulo,lista=lista)


@app.route('/formularios')
def formularios():
    return render_template("formularios.html")

@app.route('/reportes')
def reportes():
    return render_template("reportes.html")



@app.route('/hola')
def hola():
    return "¡Hola, hola!"

@app.route('/user/<user>')
def user(user):
    return f"¡Hola, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}" .format(n)

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} nombre: {}" .format(id, username)

@app.route('/suma/<float:n1>/<float:n2>')
def func(n1, n2):
    return "la suma es: {}" .format(n1+n2)
    
    
@app.route("/default")
@app.route("/default/<string:param>")
def func2(param="juan"):
    return f"<h1>!Hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
    <form>
    <label for "name">Nombre:</label>
    <input type="text" id="name" name="name" required>
    
    <label for "name">apaterno:</label>
    <input type="text" id="name" name="name" required>
    </form>

'''

@app.route("/operasBas")
def operas1():
    return render_template('operasBas.html')


@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        operacion = request.form.get("flexRadioDefault")
        
        num1 = float(n1)
        num2 = float(n2)
        res = 0

        if operacion == "suma":
            res = num1 + num2
        elif operacion == "resta":
            res = num1 - num2
        elif operacion == "multi": 
            res = num1 * num2
        elif operacion == "division":
            if num2 != 0:
                res = num1 / num2
            else:
                res = "Error: División por cero"

        return f"El resultado de la {operacion} es: {res}"
    



if __name__  == '__main__':

    app.run(debug=True)
