import imghdr
import os
from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.usuario import User
from flask_app.models.artista import Artista
from flask_app.models.integrante import Integrante
from flask_app.models.sociales_band import Social
from flask_app.models.cancion import Cancion
from flask_app.models.image import Image
from flask_app.models.generos_artista import Generos_artista
from flask_app.models.genero import Genero

from flask_app.utils.utils import allowed_file
from werkzeug.utils import secure_filename



@app.route('/artista/<id>')
def artista_logueado(id):

    if 'artista' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')
    return render_template('/artistas/perfil_artista_adm.html')

@app.route('/artista/tour')
def tour():

    if 'artista' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')

    data = {
        'session': session['artista'],
        'id': session['artista_id']

        }

    return render_template('/artistas/tour.html', data=data)

@app.route('/artista/editar_cuenta/biografia', methods=['GET','POST'])
def editar_cuenta_biografia():

    artistas = Artista.get_by_id(session['artista_id'])
    data = {
            'session': session['artista'],
            'id': session['artista_id']
            }

    if request.method == 'GET':
        return render_template('/artistas/editar/editar_artista_biografia.html', data=data, artistas=artistas)
        
    if request.method == 'POST': 
        
        artista = {
            'año_formacion': request.form['año_formacion'],
            'biografia': request.form['biografia'],
            'username': request.form['username'],
            'email': request.form['email'],
            'artistas_id': session['artista_id']
        }
        
        Artista.update(artista)
        return redirect(url_for('artista_logueado', id=session['artista']))

@app.route('/artista/editar_cuenta/fotos')
def add_image():
    imagenes = Image.get_by_id(session['artista_id'])
    total_imagenes = False
    if imagenes is None:
        return render_template('/artistas/editar/add_artista_photo.html', imagenes=imagenes, total_imagenes=total_imagenes)

    image_max = len(imagenes)
    if image_max > 3:
        total_imagenes = True
        return render_template('/artistas/editar/add_artista_photo.html', imagenes=imagenes, total_imagenes=total_imagenes)

    return render_template('/artistas/editar/add_artista_photo.html', imagenes=imagenes)

@app.route('/artistas/photo/subir/', methods=['POST'])
def upload_photo():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part','error')
            return redirect(url_for('add_image'))
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(url_for('add_image'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = {
                'image': filename,
                'artistas_id': session['artista_id']
            }
            Image.save(data)
            return redirect(url_for('add_image')) 

@app.route('/artista/destroy_image/<id>')
def destroy_image(id):
    Image.destroy(id)
    return redirect(url_for('add_image'))

@app.route('/artista/editar_cuenta/add_integrantes', methods=['GET','POST'])
def add_integrantes():

    if request.method == 'GET':
        integrantes = Integrante.get_by_id(session['artista_id'])
        return render_template('/artistas/editar/integrantes.html', integrantes=integrantes)

    if request.method == 'POST':
        data = {
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'instrumento': request.form['instrumento'],
            'artistas_id': session['artista_id']
        }
        Integrante.save(data)
        return redirect(url_for('add_integrantes'))

@app.route('/artista/destroy_integrante/<id>')
def destroy_integrante(id):
    Integrante.destroy(id)
    return redirect(url_for('add_integrantes'))


@app.route('/artista/editar_cuenta/sociales', methods=['GET','POST'])
def add_sociales():

    if request.method == 'GET':
        sociales = Social.get_by_id(session['artista_id'])
        return render_template('/artistas/editar/sociales.html', sociales=sociales)
    
    if request.method == 'POST':
        data = {
            'red_social': request.form['red_social'],
            'link': request.form['link'],
            'artistas_id': session['artista_id']
        }
        Social.save(data)
        return redirect(url_for('add_sociales'))

@app.route('/artista/destroy_redes/<id>')
def destroy_redes(id):
    Social.destroy(id)
    return redirect(url_for('add_sociales'))

@app.route('/artista/editar_cuenta/add_tour')
def add_tour():
    data = {
        'session': session['artista'],
        'id': session['artista_id'],
        
        }

    return render_template('/artistas/editar/add_tour.html', data=data)

@app.route('/artista/editar_cuenta/songs')
def add_songs():
    canciones = Cancion.get_by_id(session['artista_id']) 
    total_songs = False
    if canciones is None:
        return render_template('/artistas/editar/add_artista_music.html', canciones=canciones, total_songs=total_songs)

    songs_max = len(canciones)
    if songs_max > 10:
        total_songs = True
        return render_template('/artistas/editar/add_artista_music.html', canciones=canciones, total_songs=total_songs)
    return render_template('/artistas/editar/add_artista_music.html', canciones=canciones)


@app.route('/artistas/canciones/subir/', methods=['POST'])
def upload_songs():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part','error')
            return redirect(url_for('add_songs'))
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(url_for('add_songs'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = {
                'cancion': filename,
                'artistas_id': session['artista_id']
            }
            Cancion.save(data)
            return redirect(url_for('add_songs')) 

@app.route('/artista/destroy_songs/<id>')
def destroy_songs(id):
    Cancion.destroy(id)
    return redirect(url_for('add_songs'))


@app.route('/artista/add_genero/', methods=['GET','POST'])
def add_genero():
    if request.method == 'GET':
        generos = Genero.get_all()
        tipos = Generos_artista.generos(session['artista_id'])
        return render_template('/artistas/editar/add_artista_genero.html', generos=generos, tipos=tipos)
    
    if request.method == 'POST':
        print(request.form)
        data = {
            'genero_id':request.form['tipo'],
            'artistas_id': session['artista_id']
        }

        Generos_artista.save(data)
        return redirect(url_for('add_genero'))

@app.route('/artista/destroy_genero/<id>')
def destroy_genero(id):
    Generos_artista.destroy(id)
    return redirect(url_for('add_genero'))

