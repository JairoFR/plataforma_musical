from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.usuario import User
from flask_app.models.artista import Artista
from flask_app.models.info_artista import Info_artista


@app.route('/artista/<id>')
def artista_logueado(id):

    if 'artista' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')

    data = {
        'session': session['artista'],
        'id': session['artista_id']
        }
    return render_template('/artistas/perfil_artista_adm.html', data=data)

@app.route('/artista/tour/<id>')
def tour(id):

    if 'artista' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/')

    data = {
        'session': session['artista'],
        'id': session['artista_id']

        }

    return render_template('/artistas/tour.html', data=data)

@app.route('/artista/editar_cuenta/biografia/<id>', methods=['GET','POST'])
def editar_cuenta_biografia(id):

    info_artista = Info_artista.get_by_id(id)
    print('>>>>>>>>>>>>><<infor',info_artista)
    artistas = Artista.get_by_id(id)
    print(artistas, 'artistas>>>>>>>')

    if info_artista is None:
        return redirect(url_for('add_info_artista'))#Agregar año formacion y biografia

    data = {
            'session': session['artista'],
            'id': session['artista_id']
            }
    if request.method == 'GET':
        return render_template('/artistas/editar/editar_artista_biografia.html', data=data, info_artista=info_artista, artistas=artistas)
        
    
    if request.method == 'POST': #terminar post
        
        datos = {
            'año_formacion': request.form['año_formacion'],
            'biografia': request.form['biografia'],
            'artistas_id': session['artista_id']
        }
        

@app.route('/artista/editar_cuenta/add_info', methods=['GET','POST'])
def add_info_artista():
    data = {
        'session': session['artista'],
        'id': session['artista_id'],
        'data': 'fotos'
    }
    if request.method == 'GET':
        return render_template('/artistas/editar/add_info_artista.html', data=data)
    
    if request.method == 'POST':
        datos = {
            'año_formacion': request.form['año_formacion'],
            'biografia': request.form['biografia'],
            'artistas_id': session['artista_id']
        }
        if not Info_artista.save(datos):
            print('fue falso')
            return redirect(url_for('add_info_artista'))
        return redirect(url_for('editar_cuenta_biografia', id=data['id']))

@app.route('/artista/editar_cuenta/fotos/<id>')
def editar_cuenta_image(id):

    data = {
        'session': session['artista'],
        'id': session['artista_id'],
        'data': 'fotos'

        }
    return render_template('/artistas/editar/editar_artista_image.html', data=data)

@app.route('/artista/editar_cuenta/songs/<id>')
def editar_cuenta_songs(id):
    data = {
        'session': session['artista'],
        'id': session['artista_id'],
        'data': 'canciones'
        }

    return render_template('/artistas/editar/editar_artista_image.html', data=data)

@app.route('/artista/editar_cuenta/integrantes/<id>')
def editar_integrantes(id):
    data = {
        'session': session['artista'],
        'id': session['artista_id'],
        
        }

    return render_template('/artistas/editar/integrantes.html', data=data)

@app.route('/artista/editar_cuenta/sociales/<id>')
def editar_sociales(id):
    data = {
        'session': session['artista'],
        'id': session['artista_id'],
        
        }

    return render_template('/artistas/editar/sociales.html', data=data)

@app.route('/artista/editar_cuenta/add_tour/<id>')
def add_tour(id):
    data = {
        'session': session['artista'],
        'id': session['artista_id'],
        
        }

    return render_template('/artistas/editar/add_tour.html', data=data)

