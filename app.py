from flask import Flask, request
from waitress import serve

from applicationservices.LogonService import LogonService

app = Flask(__name__)


@app.route('/login', methods = ['post'])
def login():
    #TODO add response for get to all methods in this file
    jsondata = request.json

    logonservice = LogonService()

    data = logonservice.logonproviders.logonapi().loginAPI(jsondata)
    response = app.response_class(response=data, status=200, mimetype='application/json')
    return response

@app.route('/logout', methods = ['post'])
def logout():
    jsondata = request.json
    logonservice = LogonService()
    data = logonservice.logonproviders.logonapi().logoutAPI(jsondata)
    response = app.response_class(response=data, status=200, mimetype='application/json')
    return response

@app.route('/validate', methods=['post'])
def validate():
    jsondata = request.json
    logonservice = LogonService()
    data = logonservice.logonproviders.logonapi().validateSessionAPI(jsondata)
    response = app.response_class(response=data, status=200, mimetype='application/json')
    return response

if __name__ == '__main__':
    #app.run()
    serve(app)
