
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

@app.route('/artista/<id>')
def artista_logueado(id):

    if 'artista' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')
    generos = Generos_artista.generos(session['artista_id'])
    canciones = Cancion.get_by_id_songs(session['artista_id'])
    imagenes = Image.get_by_id_foto(session['artista_id'])
    integrantes = Integrante.get_by_id_integrantes(session['artista_id'])
    artistas = Artista.get_by_id(session['artista_id'])
    # redes = Social.get_by_id_redes(session['artista_id'])
    imagen = Image.primera_foto(session['artista_id'])

    return render_template('/artistas/perfil_artista_adm.html',
                            generos=generos,
                            imagenes=imagenes,
                            canciones=canciones,
                            integrantes=integrantes,
                            artistas=artistas,
                            # redes=redes,
                            imagen=imagen)
                            
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

@app.route('/artistas_registrados')
def artistas_registrados():
    artistas = Artista.get_fotos_username()
    return render_template('/artistas/lista_artistas.html', artistas=artistas)

@app.route('/perfil_artista/<id>')
def perfil_artista(id):
    generos = Generos_artista.generos(id)
    canciones = Cancion.get_by_id_songs(id)
    imagenes = Image.get_by_id_foto(id)
    integrantes = Integrante.get_by_id_integrantes(id)
    artistas = Artista.get_by_id(id)
    # redes = Social.get_by_id_redes(session['artista_id'])
    imagen = Image.primera_foto(id)
    return render_template('/artistas/artista_index.html',
                            generos=generos,
                            imagenes=imagenes,
                            canciones=canciones,
                            integrantes=integrantes,
                            artistas=artistas,
                            # redes=redes,
                            imagen=imagen)
