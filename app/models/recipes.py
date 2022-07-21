from models import db


recipes_ingredients = db.Table(
	'recipes_ingredients',
	db.Column(
		'recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
	db.Column(
		'ingredient_id', db.Integer, db.ForeignKey('ingredient.id'),
		primary_key=True))


class Recipe(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(100))
	prep_time = db.Column(db.Integer)
	cook_time = db.Column(db.Integer)
	directions = db.Column(db.Text)
	ingredients = db.relationship(
		'Ingredient', secondary=recipes_ingredients, lazy=True,
		backref=db.backref('recipes', lazy=True))

	def __init__(self, name, prep_time, cook_time, directions):
		self.name = name
		self.prep_time = prep_time
		self.cook_time = cook_time
		self.directions = directions

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'prep_time': self.prep_time,
			'cook_time': self.cook_time,
			'directions': self.directions
		}
