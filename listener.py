from datetime import datetime

from flask import Flask, request
from flask import jsonify, make_response

from sqlalchemy.orm import Session
from sqlalchemy import select, update
from db_engine import engine

from werkzeug.wrappers import response


from models import Warning
from settings import get_setting

app = Flask(__name__)

@app.route('/everythingisok', methods=['POST']) # type: ignore
def everythingisok():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        with Session(engine) as session:
            warning = session.scalar(
                select(Warning)
                .where(Warning.id == json['warning_id'])
            )
            if warning:
                warning.last_success = datetime.now() # type: ignore
                session.commit()
                message = {'message': f'Warning_id {warning.id} is OK'}
                response = make_response(jsonify(message), 200)
            else:
                warning_id = json['warning_id']
                message = {'message': f'Warning_id {warning_id} is not found!'}
                response = make_response(jsonify(message), 406)
    else:
        message = {'message': f'Content-Type not supported!'}
        response = make_response(jsonify(message), 415)

    print(response)
    return response

@app.route('/everythingisok', methods=['GET', 'PUT']) # type: ignore
def everythingisok_wrong_method():
    message = {'message': f'Wrong method!'}
    response = make_response(jsonify(message), 405)
    return response

# any other request must return 404 and print request data
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE']) # type: ignore
def catch_all(path):
    message = {'message': f'Endpoint not found!'}
    response = make_response(jsonify(message), 404)
    print(request)
    return response


if __name__ == '__main__':
    app.run(debug = False, port = int(get_setting('listen_port')), host='0.0.0.0')
