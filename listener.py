from datetime import datetime

from flask import Flask, request
from flask import jsonify, make_response
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from werkzeug.wrappers import response

from db_engine import engine
from models import Warning

app = Flask(__name__)

@app.route('/everythingisok', methods=['POST']) # type: ignore
def everythingisok():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
    else:
        return 'Content-Type not supported!'
    print (json)
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
            return response
        else:
            warning_id = json['warning_id']
            message = {'message': f'Warning_id {warning_id} is not found!'}
            response = make_response(jsonify(message), 404)
            return response

if __name__ == '__main__':
    app.run(debug = False, port = 5050, host='0.0.0.0')

