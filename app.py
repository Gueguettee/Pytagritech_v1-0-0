from base import *
from database import *

@app.route('/', methods = ['POST', 'GET'])
def Add_sensor():
    if request.method == 'POST':
        id_recover = int(request.form['add_id'])
        lat_recover = float(request.form['add_lat'])
        long_recover = float(request.form['add_long'])
        #Error management
        new_sensor = sensor(id = id_recover, lat = lat_recover, long = long_recover)
        try:
            db.session.add(new_sensor)
            db.session.commit()
            return redirect('/')
        except:
            flash("Retry")
            print("error")
            return redirect('/')        
    else:
        return render_template('add_sensor.html')


@app.route('/map', methods = ['POST', 'GET'])
def Map():
    list_sensor = sensor.query.order_by(sensor.num).all()
    return render_template('map.html', list_sensor = list_sensor)


@app.route('/table', methods = ['POST', 'GET'])
def Table():
    if request.method == 'POST':
        num_to_delete = int(request.form['delete'])
        sensor_to_delete = sensor.query.get_or_404(num_to_delete)
        #Error management
        db.session.delete(sensor_to_delete)
        db.session.commit()
        return redirect('/table')
    else:
        list_sensor = sensor.query.order_by(sensor.num).all()
        return render_template('table.html', list_sensor = list_sensor)

#@app.route('/plot', methods = ['POST', 'GET'])
#def Plot_sensor():


if __name__ == "__main__":
    app.run()
    