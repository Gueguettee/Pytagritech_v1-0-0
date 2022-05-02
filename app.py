from sqlalchemy import null
from base import *
from database import *
import requests

@app.route('/', methods = ['POST', 'GET'])
def Add_sensor():
    if request.method == 'POST':
        id_recover = int(request.form['add_id'])
        lat_recover = float(request.form['add_lat'])
        long_recover = float(request.form['add_long'])
        request_data = {'id':str(id_recover),'long=':str(long_recover),'lat=':str(lat_recover)}
        request_send = requests.post('http://localhost:5000/data', data=request_data)
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

@app.route('/data', methods = ['POST'])
def Receive_data():
    id_recover = int(request.args.get['id'])
    lat_recover = float(request.args.get['lat'])
    long_recover = float(request.args.get['long'])
    new_sensor = sensor(id = id_recover, lat = lat_recover, long = long_recover)
    try:
        db.session.add(new_sensor)
        db.session.commit()
    except:
        flash("Retry")
        print("error")
    return None


if __name__ == "__main__":
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)              ###############################################
    