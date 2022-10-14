import os
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import User
from flask_app.models.artista import Artista

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#revisar
# def login():

#     if 'usuario' in session:
#         flash('Ya estás LOGEADO!', 'warning')
#         return redirect('/')

#     return render_template("login.html")

@app.route('/registrar_form/Artista', methods=['POST'])
def registrar():

    if request.method == 'GET':
        return render_template('/login/form_login.html')

    if request.method == 'POST':

        datos = {
            'username' : request.form['username'],
            'email' : request.form['email']
        }

        dato ={
            'password' : request.form['password'],
            'cpassword' : request.form['cpassword'],
            'email' : request.form['email']
        }
        if not Artista.validar(datos):
            return redirect('/registrarse_artistas')

        if  not Artista.validar_pass(dato):
            return redirect('/registrarse_artistas')
        pw_hash = bcrypt.generate_password_hash(request.form['password'])

        data = {
            "username": request.form['username'],
            "email": request.form['email'],
            "password" : pw_hash
        }

        resultado = Artista.save(data)

        if not resultado:
            flash("error al crear el usuario", "error")
            return redirect("/registrarse_artistas")

        flash("Usuario creado correctamente", "success")
        return redirect('/')



@app.route("/procesar_login", methods=["POST"])
def procesar_login_artista():

    usuario=id

    if not usuario:
        flash("Correo/Clave Invalidas", "error")
        return redirect("/")

    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Correo/Clave Invalidas", "error")
        return redirect("/")

    session['usuario'] = usuario.nombre
    session['usuario_id'] = usuario.id

    return redirect('/')










#editar usuario
# @app.route('/users/<int:id>', methods=['GET', 'POST'])
# def editar_users(id): 

#     if request.method == 'GET':

#         users = User.get_by_id(id)
#         return render_template('edit.html', users=users, magazine=magazine)
    
#     if request.method == 'POST':

#         data = {
#             'nombre': request.form['nombre'],
#             'apellido': request.form['apellido'],
#             'email': request.form['email'],
#             'id': session['usuario_id']

#         }
#     print(request.form)

#     if not User.validar(data):
#         return redirect(f'/users/{id}')

#     User.update(data)
#     return redirect('/dashboard')