from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from model import BatchRequestSchema
from converter import convert_query


main_blueprint = Blueprint('main', __name__)
FILE_NAME = 'data/apache_logs.txt'


@main_blueprint.route("/perform_query", methods=['POST'])
def perform_query():
    data = request.json
    '''
    Проверка файла на валидность.
    '''
    try:
        valid_data = BatchRequestSchema().load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400
    '''
    Выполнение запроса.
    '''
    result = None
    for query in valid_data['queries']:
        result = convert_query(
            cmd=query['cmd'],
            value=query['value'],
            filename=FILE_NAME,
            data=result
        )

    return jsonify(result)
