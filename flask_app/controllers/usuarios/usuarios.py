from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import User



@app.route('/fan/<id>')
def usuario_logueado(id):

    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')
    data = {
        'session': session['usuario']
        }

    return render_template('/usuario/editar/perfil_usuario_adm', data=data)