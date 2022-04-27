from base import *
from database import *

@app.route('/', methods = ['POST', 'GET'])
def ajouter_capteur():
    if request.method == 'POST':
        id_recup = int(request.form[''])
        latitude_recup = float(request.form[''])
        longitude_recup = float(request.form[''])
        #gestion d'erreur...
        nouveau_capteur = (id == id_recup, latitude == latitude_recup, longitude == longitude_recup)
        try:
            db.session.add(nouveau_capteur)
            db.session.commit()
            return redirect('/')
        except:
            flash('Veuillez réessayer')
    else:
        return render_template('ajouter_capteur.html')


@app.route('/map', methods = ['POST', 'GET'])
def map():
    return render_template('map.html')


@app.route('/table', methods = ['POST', 'GET'])
def table():
    if request.method == 'POST':
        num_cap_supprimer = int(request.form[''])
        cap_supprimer = capteur.query.get_or_404(num_cap_supprimer)
        #gestion erreur...
        db.session.delete(cap_supprimer)
        db.session.commit()
        return redirect('/table')
    else:
        return render_template('table.html')


if __name__ == "__main__":
    app.run()