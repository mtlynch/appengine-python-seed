import json
import logging

import flask

logger = logging.getLogger(__name__)
app = flask.Flask(__name__)

_HEADERS = {
    'Access-Control-Allow-Origin': '*',
}


@app.route('/hello', methods=['GET'])
def hello_world():
    return flask.Response(
        json.dumps('hello, world!'),
        status=200,
        mimetype='application/json',
        headers=_HEADERS)


@app.errorhandler(404)
def not_found_error(e):
    logger.exception(e)
    return flask.Response(e.message, status=404, headers=_HEADERS)


@app.errorhandler(500)
def server_error(e):
    logger.exception(e)
    return flask.Response(e.message, status=500, headers=_HEADERS)
