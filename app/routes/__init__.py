from routes.root import rootbp


def init_routes(app):
    app.register_blueprint(rootbp)
