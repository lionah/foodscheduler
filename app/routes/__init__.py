from routes.ingredients import Ingredient, ingredientsbp
from routes.recipes import Recipe, recipesbp
from routes.root import rootbp


def init_routes(app):
	app.register_blueprint(rootbp)

	app.register_blueprint(ingredientsbp)
	app.register_blueprint(recipesbp)
