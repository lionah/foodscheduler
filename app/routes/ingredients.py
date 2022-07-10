import json

from flask import Blueprint
from flask import request

from models import db
from models.ingredients import Ingredient


ingredientsbp = Blueprint('ingredients', __name__, url_prefix="/ingredients")


def root_get(request):
	ingredients = map(
		lambda ingredient: ingredient.to_dict(), Ingredient.query.all())

	return json.dumps(list(ingredients))


def root_post(request):
	name = request.form.get('name')

	ingredient = Ingredient(name)

	db.session.add(ingredient)

	db.session.commit()

	return json.dumps(ingredient.to_dict())


@ingredientsbp.route('/', methods=['GET', 'POST'])
def root():
	if request.method == 'GET':
		return root_get(request)
	elif request.method == 'POST':
		return root_post(request)
