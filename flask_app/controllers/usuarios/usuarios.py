from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import User
from flask_app.models.image import Image



@app.route('/fan/<id>')
def usuario_logueado(id):

    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')
    usuarios= User.get_all()
    imagenes = Image.primera_foto_usuario(session['usuario_id'])
    return render_template('/usuarios/usuario_index_adm.html', usuarios=usuarios, imagenes=imagenes)
