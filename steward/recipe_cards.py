from datetime import date


class BaseRecipeCard(object):

    def __init__(self, id_num, name, frequency, ingredients=None, prep_instructions=None, date_last_eaten=None):
        self.id = id_num
        self.name = name
        self.frequency = frequency
        self.ingredients = ingredients
        self.prep_instructions = prep_instructions
        self.date_last_eaten = date_last_eaten

    def add_to_tab(self):
        pass

    def edit_in_tab(self):
        pass

    def is_available(self):

        since_eaten = date.today() - self.date_last_eaten

        if since_eaten.days > 14 and self.frequency == 1:
            return True

        elif since_eaten.days > 21 and self.frequency == 2:
            return True

        elif since_eaten.days > 28 and self.frequency == 3:
            return True

        else:
            return False


class MainDishCard(BaseRecipeCard):

    def __init__(self, id_num, name, cuisine, protein, frequency, preferred_sides=None,
                 ingredients=None, prep_instructions=None, date_last_eaten=None
                 ):
        super(MainDishCard, self).__init__(id_num, name, frequency, ingredients, prep_instructions, date_last_eaten)

        self.cuisine = cuisine
        self.protein = protein
        self.preferred_sides = preferred_sides


class SideDishCard(BaseRecipeCard):

    def __init__(self, id_num, name, category, frequency, ingredients=None,
                 prep_instructions=None, date_last_eaten=None
                 ):

        super(SideDishCard, self).__init__(id_num, name, frequency, ingredients, prep_instructions, date_last_eaten)
        self.type = category


class DessertCard(BaseRecipeCard):

    def __init__(self, id_num, name, frequency, ingredients=None, prep_instructions=None, date_last_eaten=None):

        super(DessertCard, self).__init__(id_num, name, frequency, ingredients, prep_instructions, date_last_eaten)


class AppetizerCard(BaseRecipeCard):

    def __init__(self, id_num, name, frequency, ingredients=None, prep_instructions=None, date_last_eaten=None):

        super(AppetizerCard, self).__init__(id_num, name, frequency, ingredients, prep_instructions, date_last_eaten)


