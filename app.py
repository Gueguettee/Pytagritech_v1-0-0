from base import *
from database import *

@app.route('/', methods = ['POST', 'GET'])
def ajouter_capteur():
    if request.method == 'POST':
        id_recup = int(request.form['ajouter_id'])
        latitude_recup = float(request.form['ajouter_lat'])
        longitude_recup = float(request.form['ajouter_long'])
        #gestion d'erreur...
        nouveau_capteur = capteur(id = id_recup, latitude = latitude_recup, longitude = longitude_recup)
        try:
            db.session.add(nouveau_capteur)
            db.session.commit()
            return redirect('/')
        except:
            flash('Veuillez réessayer')
            print("error")
            return redirect('/')        
    else:
        return render_template('ajouter_capteur.html')


@app.route('/map', methods = ['POST', 'GET'])
def map():
    return render_template('map.html')


@app.route('/table', methods = ['POST', 'GET'])
def table():
    if request.method == 'POST':
        num_cap_supprimer = int(request.form['supprimer'])
        cap_supprimer = capteur.query.get_or_404(num_cap_supprimer)
        #gestion erreur...
        db.session.delete(cap_supprimer)
        db.session.commit()
        return redirect('/table')
    else:
        liste_cap = capteur.query.order_by(capteur.num).all()
        return render_template('table.html', liste_cap = liste_cap)


if __name__ == "__main__":
    app.run()