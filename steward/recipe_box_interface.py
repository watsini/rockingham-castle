from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from recipe_cards import MainDishCard

Base = declarative_base()
engine = create_engine('sqlite:///recipebox.sqlite')
session = sessionmaker()
session.configure(bind=engine)
s = session()


class MainDishTab(Base):
    __tablename__ = 'maindishtab'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    ingredients = Column(String(2500))
    prep_instructions = Column(String(2500))
    frequency = Column(String(250))
    date_last_eaten = Column(String(250))
    cuisine = Column(String(250))
    protein = Column(String(250))
    preferred_sides = Column(String(2500))


class SideDishTab(Base):
    __tablename__ = "sidedishtab"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    ingredients = Column(String(2500))
    prep_instructions = Column(String(2500))
    frequency = Column(String(250))
    date_last_eaten = Column(String(250))
    category = Column(String(250))


class DessertTab(Base):
    __tablename__ = "desserttab"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    ingredients = Column(String(2500))
    prep_instructions = Column(String(2500))
    frequency = Column(String(250))
    date_last_eaten = Column(String(250))
    type = Column(String(250))


class AppetizerTab(Base):
    __tablename__ = "appetizertab"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    ingredients = Column(String(2500))
    prep_instructions = Column(String(2500))
    frequency = Column(String(250))
    date_last_eaten = Column(String(250))
    type = Column(String(250))


def get_recipe(table, name):
    s.query(table).filter(table.name == name).all()


def build_main_table(mains_list):
    for main in mains_list:

        if main.preferred_sides:
            main.preferred_sides = "~".join(main.sides)
        if main.ingredients:
            main.ingredients = "~".join(main.ingredients)
        if main.prep_instructions:
            main.prep_instructions = "~".join(main.prep_instructions)

        if not s.query(MainDishTab).filter(MainDishTab.name == main.name).all():
            add_recipe = MainDishTab(name=main.name, cuisine=main.cuisine,
                                     protein=main.protein, preferred_sides=main.preferred_sides,
                                     ingredients=main.ingredients, prep_instructions=main.prep_instructions,
                                     frequency=main.frequency, date_last_eaten=main.date_last_eaten)
            print "Adding {} to {}".format(main.name, add_recipe.__tablename__)
            s.add(add_recipe)
            s.commit()


def import_mains_table():
    generated_recipe_list = []
    recipes = s.query(MainDishTab).all()

    for recipe in recipes:
        generated_recipe_list.append(MainDishCard(recipe.id, recipe.name, recipe.cuisine, recipe.protein,
                                                  recipe.preferred_sides, recipe.ingredients, recipe.prep_instructions,
                                                  recipe.frequency, recipe.date_last_eaten))
    return generated_recipe_list


def build_side_table(side_list):
    for side in side_list:

        if side.ingredients:
            side.ingredients = "~".join(side.ingredients)

        if side.prep_instructions:
            side.prep_instructions = "~".join(side.prep_instructions)

        if not s.query(SideDishTab).filter(SideDishTab.name == side.name).all():
            add_recipe = SideDishTab(name=side.name, category=side.type,
                                     ingredients=side.ingredients, prep_instructions=side.prep_instructions,
                                     frequency=side.frequency, date_last_eaten=side.date_last_eaten)
            s.add(add_recipe)
            s.commit()


def build_dessert_table(dessert_list):
    for dessert in dessert_list:

        ingredients = "~".join(dessert.ingredients)
        prep_instructions = "~".join(dessert.prep_instructions)

        if not s.query(DessertTab).filter(DessertTab.name == dessert.name).all():
            add_recipe = DessertTab(name=dessert.name, ingredients=ingredients,
                                    prep_instructions=prep_instructions,
                                    frequency=dessert.frequency, date_last_eaten=dessert.date_last_eaten)
            s.add(add_recipe)
            s.commit()


def build_app_table(app_list):
    for app in app_list:

        ingredients = "~".join(app.ingredients)
        prep_instructions = "~".join(app.prep_instructions)

        if not s.query(AppetizerTab).filter(AppetizerTab.name == app.name).all():
            add_recipe = AppetizerTab(name=app.name, ingredients=ingredients, prep_instructions=prep_instructions,
                                      frequency=app.frequency, date_last_eaten=app.date_last_eaten)
            s.add(add_recipe)
            s.commit()


if __name__ == '__main__':
    try:
        if not s.query(MainDishTab).all():

            print "The database is is initialized... creating"
            Base.metadata.create_all(engine)
            main_list = [MainDishCard(None, 'Grilled chicken', 'American', 'Chicken', 1),
                         MainDishCard(None, 'Sausage corn chowder', 'American', 'Sausage', 2),
                         MainDishCard(None, 'Spaghetti', 'Italian', 'Sausage', 2),
                         MainDishCard(None, 'Orange BBQ chicken pockets', 'American', 'Chicken', 2),
                         MainDishCard(None, 'Pad Thai', 'Asian', 'Chicken', 2),
                         MainDishCard(None, 'Scalloped potatoes w/ham', 'American', 'Ham', 3),
                         MainDishCard(None, 'Hamburgers', 'American', 'Hamburger', 2),
                         MainDishCard(None, 'Taco salad', 'Mexican', 'Hamburger', 2),
                         MainDishCard(None, 'Tacos', 'Mexican', 'Hamburger', 2),
                         MainDishCard(None, 'Shrimp scampi', 'Italian', 'Seafood', 3),
                         MainDishCard(None, 'Mini meatloaves', 'American', 'Hamburger', 3),
                         MainDishCard(None, 'Tortellini salad', 'Italian', 'Chicken', 2),
                         MainDishCard(None, 'Homemade pizzas', 'Italian', 'Any', 2),
                         MainDishCard(None, 'Fajitas', 'Mexican', 'Chicken', 2),
                         MainDishCard(None, 'Chili meatballs', 'American', 'Hamburger', 2),
                         MainDishCard(None, 'Teriyaki chicken', 'Asian', 'Chicken', 2),
                         MainDishCard(None, 'Breakfast for dinner', 'American', 'Bacon', 2),
                         MainDishCard(None, 'Steak', 'American', 'Steak', 2),
                         MainDishCard(None, 'BLTs', 'American', 'Bacon', 2),
                         MainDishCard(None, 'Brats', 'American', 'Sausage', 2),
                         MainDishCard(None, 'Chili', 'American', 'Hamburger', 3),
                         MainDishCard(None, 'Dinosaur eggs', 'Italian', 'Hamburger', 3),
                         MainDishCard(None, 'Sandwiches', 'American', 'Any', 2),
                         MainDishCard(None, 'Apple Pork Chops', 'American', 'Pork', 2),
                         MainDishCard(None, 'Wild Rice Pork Chops', 'American', 'Pork', 1),
                         MainDishCard(None, 'Tuna Noodle Casserole', 'American', 'Seafood', 3),
                         MainDishCard(None, 'Pot Roast', 'American', 'Beef', 3),
                         MainDishCard(None, 'Beef Stew', 'American', 'Beef', 2),
                         MainDishCard(None, 'Jambalaya', 'American', 'Sausage', 2),
                         MainDishCard(None, 'Chicken and Biscuits', 'American', 'Chicken', 3),
                         MainDishCard(None, 'Lasagna', 'Italian', 'Sausage', 2),
                         MainDishCard(None, 'Roasted Chicken', 'American', 'Chicken', 3),
                         MainDishCard(None, 'Firecracker Shrimp Tacos', 'Asian', 'Seafood', 3),
                         MainDishCard(None, 'Pasta Carbonara', 'Italian', 'Bacon', 2),
                         MainDishCard(None, 'Marinated Flank Steak', 'American', 'Steak', 3),
                         MainDishCard(None, 'DIY Mad Greens', 'American', 'Chicken', 3),
                         MainDishCard(None, 'Chili Fig Pork Roast', 'American', 'Pork', 2),
                         MainDishCard(None, 'Mushroom Ravioli', 'Italian', 'Vegetarian', 2),
                         MainDishCard(None, 'Meatball Subs', 'Italian', 'Hamburger', 2),
                         MainDishCard(None, 'Beans and Weanies', 'American', 'Sausage', 3),
                         MainDishCard(None, 'Hamburger Pie', 'American', 'Hamburger', 2),
                         MainDishCard(None, 'Lamb Kabobs', 'Mediterranean', 'Lamb', 3),
                         MainDishCard(None, 'Maple Mustard Chicken', 'American', 'Chicken', 2),
                         MainDishCard(None, 'Spicy Tofu Udon', 'Asian', 'Vegetarian', 3),
                         MainDishCard(None, 'Pork Tenderloin with Balsamic Reduction', 'American', 'Pork', 3),
                         MainDishCard(None, 'Eat Out', 'Any', 'Eat Out', 1)]

            build_main_table(main_list)

        else:
            print "The recipe box is overflowing..."

    except Exception:
        print "Something went terrible wrong... Rexamine your life."
