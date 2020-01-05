from flask import Flask, g
from routes import major_powers, requested_country, api_kt, api_per_capita, major_powers_api

app = Flask(__name__) 
app.config['SECRET_KEY'] = '6tB,GHg2OM[4UU2/@h5#!Rtz._sample_key'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

app.add_url_rule('/', 'index', major_powers)
app.add_url_rule('/major_powers', 'major_powers', major_powers)
app.add_url_rule('/', 'requested_country', requested_country, methods=["POST"])

app.add_url_rule('/api/<string:country>/kt', 'api_kt', api_kt, methods=["GET"])
app.add_url_rule('/api/<string:country>/percapita', 'api_per_capita', api_per_capita, methods=['GET'])
app.add_url_rule('/api/majorpowers', 'major_powers_api', major_powers_api, methods=['GET'])