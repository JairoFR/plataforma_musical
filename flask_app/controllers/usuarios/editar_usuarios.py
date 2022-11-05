import os
from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.usuario import User
from flask_app.models.image import Image

from flask_app.utils.utils import allowed_file
from werkzeug.utils import secure_filename

@app.route('/usuarios/editar_cuenta/fotos')
def add_image_usuarios():
    imagenes = Image.primera_foto_usuario(session['usuario_id'])
    total_imagenes = False
    if imagenes is None:
        return render_template('/usuarios/editar/add_usuario_photo.html', imagenes=imagenes, total_imagenes=total_imagenes)

    image_max = len(imagenes)
    if image_max > 6:
        total_imagenes = True
        return render_template('/usuarios/editar/add_usuario_photo.html', imagenes=imagenes, total_imagenes=total_imagenes)

    return render_template('/usuarios/editar/add_usuario_photo.html', imagenes=imagenes)

@app.route('/usuarios/photo/subir/', methods=['POST'])
def upload_photo_usuario():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part','error')
            return redirect(url_for('add_image_usuarios'))
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(url_for('add_image_usuarios'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = {
                'image': filename,
                'usuarios_id': session['usuario_id']
            }
            Image.save_photo_users(data)
            return redirect(url_for('add_image_usuarios')) 

@app.route('/usuario/destroy_image/<id>')
def destroy_image_usuario(id):
    Image.destroy(id)
    return redirect(url_for('add_image_usuarios'))

@app.route('/usuario/editar_bio', methods=['POST', 'GET'])
def editar_biografia_users():

    if request.method == 'GET':
        usuarios= User.get_all()    
        return render_template('/usuarios/editar/editar_usuario_biografia.html', usuarios=usuarios)
    
    if request.method == 'POST': 
       
        data = {
            'username' : request.form['username'],
            'email' : request.form['email'],
            'usuarios_id': session['usuario_id']
        }   
        User.update(data)
        return redirect(url_for('editar_biografia_users'))
















