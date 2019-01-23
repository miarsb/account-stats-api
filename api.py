from flask import Flask, jsonify
from flask import request, abort
from functools import wraps
import api_helpers

app = Flask(__name__)

def require_appkey(view_function):
    """Method to ensure the request is authorized

            Returns:
                A 401 if unauthorized or allows the request to
                pass through if authorized"""
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        key_file = open('key.txt')
        key = key_file.readline()
        key_file.close()
        token = request.headers.get('Authorization')
        if token and token == key.strip():
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

@app.route('/traffic/api/v1/<string:account_id>', methods=['GET'])
@require_appkey
def get_account(account_id):
    """API path for requesting account score by account name

        Args:
            Must provide an account name as part of the reequest
            Must provide the valid authorization key as well
            example: /traffic/api/v1/wpengine?auth='test'"""

    data = api_helpers.pull_account_traffic(account_id)
    return jsonify(account=account_id,
                    account_traffic=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
