from flask import Blueprint
from blogapp import app

main_routes = Blueprint('routes', __name__)


@app.route('/health', methods=['GET'])
def health():
    return "working"
