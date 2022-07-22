import json

from flask import Blueprint
from flask import request

from models import db
from models.recipes import Recipe


recipesbp = Blueprint('recipes', __name__, url_prefix="/recipes")


@recipesbp.route('/<int:recipe_id>', methods=['DELETE', 'GET', 'POST'])
def recipe(recipe_id):
	recipe = Recipe.query.get(recipe_id)

	if request.method == 'DELETE':
		return _delete_recipe(recipe, request)
	elif request.method == 'GET':
		return _get_recipe(recipe)
	elif request.method == 'POST':
		return _post_recipe(recipe, request)


@recipesbp.route('/', methods=['GET', 'POST'])
def recipes():
	if request.method == 'GET':
		return _get_recipes(request)
	elif request.method == 'POST':
		return _post_recipes(request)


def _delete_recipe(recipe, request):
	db.session.delete(recipe)

	db.session.commit()

	return json.dumps(recipe.to_dict())


def _get_recipe(recipe):
	return json.dumps(recipe.to_dict())


def _post_recipe(recipe, request):
	name = request.form.get('name')
	prep_time = request.form.get('prep_time')
	cook_time = request.form.get('cook_time')
	directions = request.form.get('directions')

	recipe.name = name or recipe.name
	recipe.prep_time = int(prep_time or recipe.prep_time)
	recipe.cook_time = int(cook_time or recipe.cook_time)
	recipe.directions = directions or recipe.directions

	db.session.add(recipe)

	db.session.commit()

	return json.dumps(recipe.to_dict())


def _get_recipes(request):
	recipes = map(
		lambda recipe: recipe.to_dict(), Recipe.query.all())

	return json.dumps(list(recipes))


def _post_recipes(request):
	name = request.form.get('name')
	prep_time = int(request.form.get('prep_time') or 0)
	cook_time = int(request.form.get('cook_time') or 0)
	directions = request.form.get('directions')

	recipe = Recipe(name, prep_time, cook_time, directions)

	db.session.add(recipe)

	db.session.commit()

	return json.dumps(recipe.to_dict())
