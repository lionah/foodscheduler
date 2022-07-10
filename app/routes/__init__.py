from routes.root import rootbp
from routes.ingredients import Ingredient, ingredientsbp


def init_routes(app):
	app.register_blueprint(rootbp)
	app.register_blueprint(ingredientsbp)
