from base import *
from database import N_DATA, data_sensor,sensor


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
    list_sensor = sensor.query.order_by(sensor.id).all()
    return render_template('map.html', list_sensor = list_sensor)


@app.route('/table', methods = ['POST', 'GET'])
def Table():
    if request.method == 'POST':
        id_to_delete = int(request.form['delete'])
        sensor_to_delete = sensor.query.get_or_404(id_to_delete)
        #Error management
        db.session.delete(sensor_to_delete)
        db.session.commit()
        return redirect('/table')
    else:
        list_sensor = db.session.query(sensor).order_by(sensor.id).all()
        return render_template('table.html', list_sensor = list_sensor)


@app.route('/plot', methods = ['POST', 'GET'])
def Plot_sensor():
    if request.method == 'GET':
        id = int(request.args.get('id'))
        all_data = db.session.query(data_sensor).filter_by(id = id).limit(N_DATA).all()
        #all_data.query(data_sensor).order_by(data_sensor.time).all()
        return render_template('plot_sensor.html', data = all_data)


@app.route('/data', methods = ['POST'])
def Receive_data():
    id_recover = int(request.form['id'])
    time_recover = str(request.form['time'])
    data_recover = float(request.form['data'])
    new_sensor_data = data_sensor(id = id_recover, time = time_recover, data = data_recover)
    all_data = db.session.query(data_sensor).filter_by(id = id_recover).all()
    try:
        if len(all_data) >= N_DATA:
            num_to_delete = len(all_data) - N_DATA + 1
            for num in range(0,num_to_delete):
                data_sensor_to_delete = all_data[num]
                db.session.delete(data_sensor_to_delete)
        db.session.add(new_sensor_data)
        db.session.commit()
        return "ok"
    except:
        flash("Retry")
        print("error")
        return "nok"
    