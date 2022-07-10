from flask import Flask

import models
import routes


app = Flask(__name__)


def main():
    models.init_db(app)

    routes.init_routes(app)

    app.run()


if __name__ == '__main__':
    main()
