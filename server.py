from flask_app.controllers.artistas import editar_artistas,  login_artista
from flask_app.controllers.usuarios import usuarios, login_fan
from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.usuario import User
from flask_app.models.artista import Artista
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("pagina_principal.html" )

@app.route('/registrarse')
def registarse():

    if 'usuario' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect(url_for('usuario_logueado', id=session['usuario_id']))
    
    elif 'artista' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect(url_for('artista_logueado'), id=session['artista_id'])

    return render_template("/login/registrarse.html", )

@app.route('/registrarse/fan')
def registrarse_fans():

    if 'usuario' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect(url_for('usuario_logueado', id=session['usuario_id']))
    
    elif 'artista' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect(url_for('artista_logueado'), id=session['artista_id'])
    
    data = {
        'tipo':'artista',
        'nombre': 'Fan',
        'funcion':'registrar_form',
        'username':'Username'
    }
    return render_template('/login/form_login.html', data=data)

@app.route('/registrarse/artista')
def registrarse_artistas():

    if 'usuario' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect(url_for('usuario_logueado', id=session['usuario_id']))
    
    elif 'artista' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect(url_for('artista_logueado'), id=session['artista_id'])

    data = {
        'tipo':'fan',
        'nombre': 'Artista',
        'funcion':'registrar_form',
        'username':'Banda/Artista'
    }
    return render_template('/login/form_login.html', data=data)

@app.route('/login', methods=['GET','POST'])
def login():
    
    if 'usuario' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect(url_for('usuario_logueado', id=session['usuario_id']))
    
    if 'artista' in session:
        flash('Ya estás LOGEADO!', 'warning')
        return redirect(url_for('artista_logueado', id=session['artista_id']))

    if request.method == 'GET':
        return render_template('/login/inicio_session.html')
    
    #busca por email si pertenece a la tabla usuario o artista, si devulve false no pertenece
    if request.method == 'POST':
        usuarios = User.get_by_email(request.form['identificacion'])
        if not usuarios:
            artista = Artista.get_by_email(request.form['identificacion'])
            if not artista:
                flash("Correo/Clave Invalidas artista", "error")
                return redirect(url_for('login'))
            
            if not bcrypt.check_password_hash(artista.password, request.form['password']):
                flash("Correo/Clave Invalidas", "error")
                return redirect(url_for('login'))
    
            session['artista'] = artista.username
            session['artista_id'] = artista.artistas_id
            return redirect(url_for('artista_logueado', id=artista.username))

        
        if not bcrypt.check_password_hash(usuarios.password, request.form['password']):
            flash("Correo/Clave Invalidas", "error")
            return redirect(url_for('login'))

        session['usuario'] = usuarios.username
        session['usuario_id'] = usuarios.usuarios_id

        return redirect(url_for('usuario_logueado', id=usuarios.username))
            
@app.route('/logout')
def logout():
    session.clear()
    flash("Vuelve pronto", "success")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)



