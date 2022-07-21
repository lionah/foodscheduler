import json

from flask import Blueprint
from flask import request

from models import db
from models.ingredients import Ingredient


ingredientsbp = Blueprint('ingredients', __name__, url_prefix="/ingredients")


@ingredientsbp.route('/<int:ingredient_id>', methods=['DELETE', 'GET', 'POST'])
def ingredient(ingredient_id):
	ingredient = Ingredient.query.get(ingredient_id)

	if request.method == 'DELETE':
		return _delete_ingredient(ingredient, request)
	elif request.method == 'GET':
		return _get_ingredient(ingredient)
	elif request.method == 'POST':
		return _post_ingredient(ingredient, request)


@ingredientsbp.route('/', methods=['GET', 'POST'])
def ingredients():
	if request.method == 'GET':
		return _get_ingredients(request)
	elif request.method == 'POST':
		return _post_ingredients(request)


def _delete_ingredient(ingredient, request):
	db.session.delete(ingredient)

	db.session.commit()

	return json.dumps(ingredient.to_dict())


def _get_ingredient(ingredient):
	return json.dumps(ingredient.to_dict())


def _post_ingredient(ingredient, request):
	name = request.form.get('name')

	ingredient.name = name

	db.session.add(ingredient)

	db.session.commit()

	return json.dumps(ingredient.to_dict())


def _get_ingredients(request):
	ingredients = map(
		lambda ingredient: ingredient.to_dict(), Ingredient.query.all())

	return json.dumps(list(ingredients))


def _post_ingredients(request):
	name = request.form.get('name')

	ingredient = Ingredient(name)

	db.session.add(ingredient)

	db.session.commit()

	return json.dumps(ingredient.to_dict())
