
from flask import Flask, request, url_for, redirect, abort, render_template
#from flask_mysqldb import MySQL
#import pymysql
import mysql.connector
app = Flask (__name__)


midb = mysql.connector.connect(host='localhost', user='dany', password='redamerica10', database='prueba')
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'dany'
# app.config['MYSQL_PASSWORD'] = 'redamerica10'
# app.config['MYSQL_DB'] = 'prueba'
# mysql = MySQL(app)

#cursor= mysql.connection.cursor()
cursor = midb.cursor(dictionary=True) # retorna los datos como diccionario
 
@app.route('/')
def index():
    return 'Hola mundo'

#GET, POST, PUT, PATCH, DELETE
#curl -X GET http://localhost:5000/post/  para probar la ruta
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method== 'GET':
        return "El id del post es: "+post_id
    else:
        return "Este es otro metodo y no GET"

# @app.route('/post/<post_id>', methods=['GET'])
# def lala(post_id):
#     return "El id del post es: "+post_id

# @app.route('/post/<post_id>', methods=['POST'])
# def lili(post_id):
#     return "El id del post es: "+post_id

#curl -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000/lele  enviar datos atraves de un formulario
@app.route('/lele', methods=['POST', 'GET']) 
def lele():
    cursor.execute('select * from usuario')
    usuarios  = cursor.fetchall()
    print(usuarios)
    #cursor.close()
    #print(url_for('index')) # redirigir a otra url dandole como parametro el nombre de la funcion
    #abort(403) # abortar la ejecucion
    #return redirect(url_for('lala', post_id=2)) # redirecciona a la pagina dada
     
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    #return render_template('lele.html') # redirecciona a una pagina predefinida
    # return {
    #     "username": 'ximena',
    #     "email": 'hola@gmail.com'
    # } # envia un objeto tipo json
    return render_template('lele.html', usuarios= usuarios) 

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola Mundo')

@app.route('/crear', methods=['POST', 'GET'])
def crear():
    if request.method=='POST':
        ide = request.form['id']
        nombre = request.form['username']
        email = request.form['email']
        sql = "insert into usuario (id, username, email) values(%s, %s, %s)"
        values = (ide, nombre, email)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for('lele'))
    return render_template('crear.html')



