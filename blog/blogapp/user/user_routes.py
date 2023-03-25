from flask import Blueprint

user = Blueprint("user", __name__)


@user.route("/test-user", methods=["GET"])
def test():
    return "working"
