from flask import Blueprint


rootbp = Blueprint('root', __name__)


@rootbp.route('/')
def root():
	return "Hello World!"
