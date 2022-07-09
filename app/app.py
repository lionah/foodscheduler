from flask import Flask


app = Flask(__name__)


def main():
    import routes

    routes.init_routes(app)

    app.run()


if __name__ == '__main__':
    main()
