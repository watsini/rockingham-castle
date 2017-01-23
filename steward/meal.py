"""This is a Class Doc String"""

from datetime import date
from datetime import timedelta

class Meal(object):

    def __init__(self, name, protein, cuisine=None, tier=3, ingredients=None,
                 preferred_side=None, other_sides=None, recipe=None, last_used=None):

        self.name = name
        self.protein = protein
        self.cuisine = cuisine
        self.tier = tier
        self.recipe = recipe
        self.ingredients = ingredients
        self.preferred_side = preferred_side
        self.other_sides = other_sides
        self.recipe = recipe
        self.last_used = last_used or date(2016, 1, 1)

    def print_ingredient_list(self):

        for ingredient in self.ingredients:
            print ingredient

    def is_available(self):

        since_eaten = date.today() - self.last_used

        if since_eaten.days > 14 and self.tier == 1:
            return True

        elif since_eaten.days > 21 and self.tier == 2:
            return True

        elif since_eaten.days > 28 and self.tier == 3:
            return True

        else:
            return False
1








