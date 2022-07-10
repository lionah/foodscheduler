from flask import Flask

import models
import routes


def main():
	app = Flask(__name__)

	with app.app_context():
		models.init_db(app)

	routes.init_routes(app)

	app.run()


if __name__ == '__main__':
	main()
