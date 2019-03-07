import flask
from database import *
from playhouse.shortcuts import model_to_dict
import json

app = flask.Flask(__name__)


def to_json(data):
    return json.dumps(data) + "\n"


def resp(code, data):
    return flask.Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )


@app.errorhandler(400)
def page_not_found_1(e):
    return resp(400, {})


@app.errorhandler(404)
def page_not_found_2(e):
    return resp(404, {})


@app.errorhandler(405)
def page_not_found_3(e):
    return resp(405, {})


@app.route('/water_communication', methods=['GET'])
def get_water_communication():
    water_communications = Water.select()
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
    electricity_communications = Electricity.select()
    electricity_communications_json = [model_to_dict(electricity_communication) for electricity_communication in electricity_communications]
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
    gas_communications = Gas.select()
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
    data_communications = Data.select()
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
    app.run()
