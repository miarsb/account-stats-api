from flask import Flask, jsonify, request, abort
from functools import wraps
import os
from api_helpers import ReadAccountData
#test
app = Flask(__name__)

def require_appkey(view_function):
    """Method to ensure the request is authorized

            Returns:
                A 401 if unauthorized or allows the request to
                pass through if authorized"""
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        key = os.environ.get('ACCOUNT_API_SECRET')
        token = request.headers.get('Authorization')
        if token and token == key:
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

    data = ReadAccountData(account_id).account_data
    return jsonify(account=account_id,
                    account_traffic=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
