from base import *
from database import N_DATA, data_sensor,sensor
import json

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


@app.route('/plotTEMP', methods = ['POST', 'GET'])
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
    
@app.route('/data2', methods = ['POST', 'GET'])    
def Receive_data2():
    if request.method == 'POST':
        tmp       = [float(i) for i in request.form.getlist('data')]
        app.datas = app.datas + tmp
        app.ids   = app.ids   + list(range(app.nbr, app.nbr+len(tmp)))
        app.nbr   = app.nbr   + len(tmp)
        
        # print(app.datas)
        app.datas = app.datas[-1000:]
        app.ids = app.ids[-1000:]
        # print(app.datas)
        
        app.battery = request.form['battery']
        
        return "ack"
    else:
        # return json.dumps({'battery':app.battery, 'dates':app.dates, 'datas':app.datas})
        return json.dumps([[app.dates[-1], app.datas[-1]]])
        
@app.route('/plot', methods = ['POST', 'GET'])
@app.route('/temp_sensor', methods = ['POST', 'GET'])
@cross_origin()

def Temp_sensor():
        
    if "ajax" in request.args:
        if app.lastSend in app.ids:
            idx = app.ids.index(app.lastSend)
            app.lastSend = app.ids[-1]
            return json.dumps({"datas":[app.ids[idx+1:], app.datas[idx+1:]], "battery":app.battery})
        else :
            app.lastSend = app.ids[-1]
            return json.dumps({"datas":[app.ids, app.datas], "battery":app.battery})
    else:
        # app.nbr = 0
        if 'id' in request.args:
                sensor_id = int(request.args.get('id'))
                if sensor_id != 1:
                    return render_template(f'temp_sensor{sensor_id}.html')
        return render_template('temp_sensor.html')
