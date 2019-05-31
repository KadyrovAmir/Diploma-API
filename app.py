import datetime, time

import flask
import uuid
from database import *
from playhouse.shortcuts import model_to_dict
import json

app = flask.Flask(__name__)

X = float(5 / 64000)
Y = float(5 / 111000)


def converter(o):
    if isinstance(o, uuid.UUID):
        return o.__str__()

    if isinstance(o, datetime.datetime):
        return o.__str__()


def validate_data(data):
    try:
        if data.get('inputPower') is not None:
            float(data['inputPower'])
        float(data['inputStartX'])
        float(data['inputStartY'])
        float(data['inputEndX'])
        float(data['inputEndY'])
        float(data['inputDepth'])
        datetime.datetime.strptime(flask.request.form['inputWorkDate'], "%d/%m/%Y %H:%M")
        return True
    except:
        return False

def validate_marker(data):
    try:
        float(data['inputCoordX'])
        float(data['inputCoordY'])
        float(data['inputHeight'])
        return True
    except:
        return False


def to_json(data):
    return json.dumps(data, default=converter, ensure_ascii=False) + "\n"


def resp(code, data):
    return flask.Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )


def get_user_position():
    return flask.request.headers.get('x_pos'), flask.request.headers.get('y_pos')


@app.errorhandler(400)
def page_not_found_1(e):
    return resp(400, {})


@app.errorhandler(404)
def page_not_found_2(e):
    return resp(404, {})


@app.errorhandler(405)
def page_not_found_3(e):
    return resp(405, {})


@app.route('/admin', methods=['GET'])
def admin_panel():
    return flask.render_template('admin.html')


@app.route('/admin/<string:data_type>/delete', methods=['POST'])
def admin_delete(data_type):
    data_id = flask.request.args.get('id')
    db = flask.request.path[7:-21]
    if data_type == 'marker':
        data = Marker.get(Marker.id == data_id)
        data.delete_instance()
        return flask.redirect(flask.url_for('admin_marker'))
    if db == 'water':
        data = Water.get(Water.id == data_id)
        data.delete_instance()
        return flask.redirect(flask.url_for('admin_water'))
    elif db == 'electricity':
        data = Electricity.get(Electricity.id == data_id)
        data.delete_instance()
        return flask.redirect(flask.url_for('admin_electricity'))
    elif db == 'gas':
        data = Gas.get(Gas.id == data_id)
        data.delete_instance()
        return flask.redirect(flask.url_for('admin_gas'))
    elif db == 'data':
        data = Data.get(Data.id == data_id)
        data.delete_instance()
        return flask.redirect(flask.url_for('admin_data'))
    else:
        return page_not_found_2()


@app.route('/admin/marker/edit', methods=['GET', 'POST'])
def admin_marker_edit():
    data_id = flask.request.args.get('id')
    if flask.request.method == 'POST':
        if validate_marker(flask.request.form):
            new_data = Marker(id=uuid.uuid4(),
                              coordinate_x=flask.request.form['inputCoordX'],
                              coordinate_y=flask.request.form['inputCoordY'],
                              height=flask.request.form['inputHeight'],
                              description=flask.request.form['inputInfo'])
            new_data.save()
            return flask.redirect(flask.url_for('admin_marker'))
        else:
            return flask.redirect(flask.url_for('admin_panel'))
    else:
        data = model_to_dict(Marker.get(Marker.id == data_id))
        return flask.render_template('marker_edit.html', data=data, id=data_id)



@app.route('/admin/<string:data_type>/edit', methods=['GET', 'POST'])
def admin_edit(data_type):
    data_id = flask.request.args.get('id')
    db = flask.request.path[7:-19]
    if flask.request.method == 'POST':
        if validate_data(flask.request.form):
            if db == 'water':
                new_data = Water(id=data_id,
                                 type=flask.request.form['inputType'],
                                 owner=flask.request.form['inputOwner'],
                                 start_coordinate_x=float(flask.request.form['inputStartX']),
                                 start_coordinate_y=float(flask.request.form['inputStartY']),
                                 end_coordinate_x=float(flask.request.form['inputEndX']),
                                 end_coordinate_y=float(flask.request.form['inputEndY']),
                                 depth=float(flask.request.form['inputDepth']),
                                 work_info=flask.request.form['inputWorkInfo'],
                                 work_date=datetime.datetime.strptime(flask.request.form['inputWorkDate'],
                                                                      "%d/%m/%Y %H:%M"))
                new_data.save()
                return flask.redirect(flask.url_for('admin_water'))
            elif db == 'electricity':
                new_data = Electricity(id=data_id,
                                       owner=flask.request.form['inputOwner'],
                                       power=int(flask.request.form['inputPower']),
                                       start_coordinate_x=float(flask.request.form['inputStartX']),
                                       start_coordinate_y=float(flask.request.form['inputStartY']),
                                       end_coordinate_x=float(flask.request.form['inputEndX']),
                                       end_coordinate_y=float(flask.request.form['inputEndY']),
                                       depth=float(flask.request.form['inputDepth']),
                                       work_info=flask.request.form['inputWorkInfo'],
                                       work_date=datetime.datetime.strptime(flask.request.form['inputWorkDate'],
                                                                            "%d/%m/%Y %H:%M"))
                new_data.save()
                return flask.redirect(flask.url_for('admin_electricity'))
            elif db == 'gas':
                new_data = Gas(id=data_id,
                               owner=flask.request.form['inputOwner'],
                               start_coordinate_x=float(flask.request.form['inputStartX']),
                               start_coordinate_y=float(flask.request.form['inputStartY']),
                               end_coordinate_x=float(flask.request.form['inputEndX']),
                               end_coordinate_y=float(flask.request.form['inputEndY']),
                               depth=float(flask.request.form['inputDepth']),
                               work_info=flask.request.form['inputWorkInfo'],
                               work_date=datetime.datetime.strptime(flask.request.form['inputWorkDate'],
                                                                    "%d/%m/%Y %H:%M"))
                new_data.save()
                return flask.redirect(flask.url_for('admin_gas'))
            elif db == 'data':
                new_data = Data(id=data_id,
                                owner=flask.request.form['inputOwner'],
                                start_coordinate_x=float(flask.request.form['inputStartX']),
                                start_coordinate_y=float(flask.request.form['inputStartY']),
                                end_coordinate_x=float(flask.request.form['inputEndX']),
                                end_coordinate_y=float(flask.request.form['inputEndY']),
                                depth=float(flask.request.form['inputDepth']),
                                work_info=flask.request.form['inputWorkInfo'],
                                work_date=datetime.datetime.strptime(flask.request.form['inputWorkDate'],
                                                                     "%d/%m/%Y %H:%M"))
                new_data.save()
                return flask.redirect(flask.url_for('admin_data'))
            else:
                return page_not_found_2()
    else:
        if db == 'water':
            data = model_to_dict(Water.get(Water.id == data_id))
        elif db == 'electricity':
            data = model_to_dict(Electricity.get(Electricity.id == data_id))
        elif db == 'gas':
            data = model_to_dict(Gas.get(Gas.id == data_id))
        elif db == 'data':
            data = model_to_dict(Data.get(Data.id == data_id))
        else:
            return page_not_found_2()
        data['work_date'] = datetime.datetime.strftime(data['work_date'], "%d/%m/%Y %H:%M")
        return flask.render_template('data_edit.html', type=data_type, data=data, id=data_id)


@app.route('/admin/marker/add', methods=['GET', 'POST'])
def admin_add_marker():
    if flask.request.method == 'POST':
        if validate_marker(flask.request.form):
            new_data = Marker(id=uuid.uuid4(),
                              coordinate_x=flask.request.form['inputCoordX'],
                              coordinate_y=flask.request.form['inputCoordY'],
                              height=flask.request.form['inputHeight'],
                              description=flask.request.form['inputInfo'])
            new_data.save(force_insert=True)
            return flask.redirect(flask.url_for('admin_marker'))
        else:
            return flask.redirect(flask.url_for('admin_panel'))
    else:
        return flask.render_template('marker_add.html')



@app.route('/admin/<string:data_type>/add', methods=['GET', 'POST'])
def admin_add(data_type):
    if flask.request.method == 'POST':
        db = flask.request.path[7:-18]
        if validate_data(flask.request.form):
            if db == 'water':
                new_data = Water(id=uuid.uuid4(),
                                 type=flask.request.form['inputType'],
                                 owner=flask.request.form['inputOwner'],
                                 start_coordinate_x=float(flask.request.form['inputStartX']),
                                 start_coordinate_y=float(flask.request.form['inputStartY']),
                                 end_coordinate_x=float(flask.request.form['inputEndX']),
                                 end_coordinate_y=float(flask.request.form['inputEndY']),
                                 depth=float(flask.request.form['inputDepth']),
                                 work_info=flask.request.form['inputWorkInfo'],
                                 work_date=datetime.datetime.strptime(flask.request.form['inputWorkDate'],
                                                                      "%d/%m/%Y %H:%M"))
                new_data.save(force_insert=True)
                return flask.redirect(flask.url_for('admin_water'))
            elif db == 'electricity':
                new_data = Electricity(id=uuid.uuid4(),
                                       owner=flask.request.form['inputOwner'],
                                       power=int(flask.request.form['inputPower']),
                                       start_coordinate_x=float(flask.request.form['inputStartX']),
                                       start_coordinate_y=float(flask.request.form['inputStartY']),
                                       end_coordinate_x=float(flask.request.form['inputEndX']),
                                       end_coordinate_y=float(flask.request.form['inputEndY']),
                                       depth=float(flask.request.form['inputDepth']),
                                       work_info=flask.request.form['inputWorkInfo'],
                                       work_date=datetime.datetime.strptime(flask.request.form['inputWorkDate'],
                                                                            "%d/%m/%Y %H:%M"))
                new_data.save(force_insert=True)
                return flask.redirect(flask.url_for('admin_electricity'))
            elif db == 'gas':
                new_data = Gas(id=uuid.uuid4(),
                               owner=flask.request.form['inputOwner'],
                               start_coordinate_x=float(flask.request.form['inputStartX']),
                               start_coordinate_y=float(flask.request.form['inputStartY']),
                               end_coordinate_x=float(flask.request.form['inputEndX']),
                               end_coordinate_y=float(flask.request.form['inputEndY']),
                               depth=float(flask.request.form['inputDepth']),
                               work_info=flask.request.form['inputWorkInfo'],
                               work_date=datetime.datetime.strptime(flask.request.form['inputWorkDate'],
                                                                    "%d/%m/%Y %H:%M"))
                new_data.save(force_insert=True)
                return flask.redirect(flask.url_for('admin_gas'))
            elif db == 'data':
                new_data = Data(id=uuid.uuid4(),
                                owner=flask.request.form['inputOwner'],
                                start_coordinate_x=float(flask.request.form['inputStartX']),
                                start_coordinate_y=float(flask.request.form['inputStartY']),
                                end_coordinate_x=float(flask.request.form['inputEndX']),
                                end_coordinate_y=float(flask.request.form['inputEndY']),
                                depth=float(flask.request.form['inputDepth']),
                                work_info=flask.request.form['inputWorkInfo'],
                                work_date=datetime.datetime.strptime(flask.request.form['inputWorkDate'],
                                                                     "%d/%m/%Y %H:%M"))
                new_data.save(force_insert=True)
                return flask.redirect(flask.url_for('admin_data'))
            else:
                return page_not_found_2()
        else:
            return flask.redirect(flask.url_for('admin_panel'))
    else:
        return flask.render_template('data_add.html', type=data_type)


@app.route('/admin/marker', methods=['GET'])
def admin_marker():
    markers = Marker.select()
    marker_json = [model_to_dict(marker) for marker in markers]
    return flask.render_template('marker.html', type='marker', data=marker_json)


@app.route('/admin/water_communication', methods=['GET'])
def admin_water():
    waters = Water.select()
    water_json = [model_to_dict(water) for water in waters]
    return flask.render_template('data.html', type='water', data=water_json)


@app.route('/admin/electricity_communication', methods=['GET'])
def admin_electricity():
    electricity = Electricity.select()
    electricity_json = [model_to_dict(elem) for elem in electricity]
    return flask.render_template('data.html', type='electricity', data=electricity_json)


@app.route('/admin/gas_communication', methods=['GET'])
def admin_gas():
    gas = Gas.select()
    gas_json = [model_to_dict(elem) for elem in gas]
    return flask.render_template('data.html', type='gas', data=gas_json)


@app.route('/admin/data_communication', methods=['GET'])
def admin_data():
    data = Data.select()
    data_json = [model_to_dict(elem) for elem in data]
    return flask.render_template('data.html', type='data', data=data_json)


@app.route('/marker', methods=['GET'])
def get_markers():
    x_pos, y_pos = get_user_position()
    markers = Marker.select().where((Marker.coordinate_x < x_pos + X) &
                                    (Marker.coordinate_x > x_pos - X) &
                                    (Marker.coordinate_y < y_pos + Y) &
                                    (
                                            Marker.coordinate_y > y_pos - Y)) if x_pos is not None and y_pos is not None else Marker.select()
    markers_json = [model_to_dict(marker) for marker in markers]
    return resp(200, markers_json)


@app.route('/marker/<string:marker_id>', methods=['GET'])
def get_marker_by_id(marker_id):
    try:
        marker = Marker.get(Marker.id == marker_id)
        marker_json = model_to_dict(marker)
        return resp(200, marker_json)
    except DoesNotExist:
        return page_not_found_2()


@app.route('/water_communication', methods=['GET'])
def get_water_communication():
    x_pos, y_pos = get_user_position()
    water_communications = Water.select().where((Water.start_coordinate_x < x_pos + X) &
                                                (Water.start_coordinate_x > x_pos - X) &
                                                (Water.start_coordinate_y < y_pos + Y) &
                                                (Water.start_coordinate_y > y_pos - Y)) if x_pos is not None and y_pos is not None else Water.select()
    water_communications_json = [model_to_dict(water_communication) for water_communication in water_communications]
    return resp(200, water_communications_json)


@app.route('/water_communication/<string:water_id>', methods=['GET'])
def get_water_communication_by_id(water_id):
    try:
        water_communication = Water.get(Water.id == water_id)
        water_communication_json = model_to_dict(water_communication)
        return resp(200, water_communication_json)
    except DoesNotExist:
        return page_not_found_2()


@app.route('/electricity_communication', methods=['GET'])
def get_electricity_communication():
    x_pos, y_pos = get_user_position()
    electricity_communications = Electricity.select((Electricity.start_coordinate_x < x_pos + X) &
                                                    (Electricity.start_coordinate_x > x_pos - X) &
                                                    (Electricity.start_coordinate_y < y_pos + Y) &
                                                    (Electricity.start_coordinate_y > y_pos - Y)) if x_pos is not None and y_pos is not None else Electricity.select()
    electricity_communications_json = [model_to_dict(electricity_communication) for electricity_communication in
                                       electricity_communications]
    return resp(200, electricity_communications_json)


@app.route('/electricity_communication/<string:electricity_id>', methods=['GET'])
def get_electricity_communication_by_id(electricity_id):
    try:
        electricity_communication = Electricity.get(Electricity.id == electricity_id)
        electricity_communication_json = model_to_dict(electricity_communication)
        return resp(200, electricity_communication_json)
    except DoesNotExist:
        return page_not_found_2()


@app.route('/gas_communication', methods=['GET'])
def get_gas_communication():
    x_pos, y_pos = get_user_position()
    gas_communications = Gas.select((Gas.start_coordinate_x < x_pos + X) &
                                    (Gas.start_coordinate_x > x_pos - X) &
                                    (Gas.start_coordinate_y < y_pos + Y) &
                                    (Gas.start_coordinate_y > y_pos - Y)) if x_pos is not None and y_pos is not None else Gas.select()
    gas_communications_json = [model_to_dict(gas_communication) for gas_communication in gas_communications]
    return resp(200, gas_communications_json)


@app.route('/gas_communication/<string:gas_id>', methods=['GET'])
def get_gas_communication_by_id(gas_id):
    try:
        gas_communication = Gas.get(Gas.id == gas_id)
        gas_communication_json = model_to_dict(gas_communication)
        return resp(200, gas_communication_json)
    except DoesNotExist:
        return page_not_found_2()


@app.route('/data_communication', methods=['GET'])
def get_data_communication():
    x_pos, y_pos = get_user_position()
    data_communications = Data.select((Data.start_coordinate_x < x_pos + X) &
                                      (Data.start_coordinate_x > x_pos - X) &
                                      (Data.start_coordinate_y < y_pos + Y) &
                                      (Data.start_coordinate_y > y_pos - Y)) if x_pos is not None and y_pos is not None else Data.select()
    data_communications_json = [model_to_dict(data_communication) for data_communication in data_communications]
    return resp(200, data_communications_json)


@app.route('/data_communication/<string:data_id>', methods=['GET'])
def get_data_communication_by_id(data_id):
    try:
        data_communication = Data.get(Data.id == data_id)
        data_communication_json = model_to_dict(data_communication)
        return resp(200, data_communication_json)
    except DoesNotExist:
        return page_not_found_2()


if __name__ == '__main__':
    app.debug = True
    app.run()
