from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from meal import Meal

Base = declarative_base()
engine = create_engine('sqlite:///meals.sqlite')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()


class FamilyMeals(Base):
    __tablename__ = 'familymeals'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    protein = Column(String)


def db_meals_list():
    generated_meal_list = []
    mealsdb = s.query(FamilyMeals).all()

    for meal in mealsdb:
        generated_meal_list.append(Meal(meal.name, meal.protein))

    return generated_meal_list


def update_last_date(meal):
    mealsdb = s.query(FamilyMeals).all()


def build_meals_db():
    meals_list = [Meal('Grilled chicken', 'Chicken'),
                  Meal('Sausage corn chowder', 'Sausage'),
                  Meal('Spaghetti', 'Sausage'),
                  Meal('Orange BBQ chicken pockets', 'Chicken'),
                  Meal('Pad Thai', 'Chicken'),
                  Meal('Scalloped potatoes w/ham', 'Ham'),
                  Meal('Hamburgers', 'Hamburger'),
                  Meal('Taco salad', 'Hamburger'),
                  Meal('Tacos', 'Hamburger'),
                  Meal('Shrimp scampi', 'Seafood'),
                  Meal('Mini meatloaves', 'Hamburger'),
                  Meal('Tortellini salad', 'Chicken'),
                  Meal('Homemade pizzas', 'Any'),
                  Meal('Fajitas', 'Chicken'),
                  Meal('Chili meatballs', 'Hamburger'),
                  Meal('Teriyaki chicken', 'Chicken'),
                  Meal('Breakfast for dinner', 'Bacon'),
                  Meal('Steak', 'Steak'),
                  Meal('BLTs', 'Bacon'),
                  Meal('Brats', 'Sausage'),
                  Meal('Chili', 'Hamburger'),
                  Meal('Dinosaur eggs', 'Hamburger'),
                  Meal('Sandwiches', 'Any'),
                  Meal('Apple Pork Chops', 'Pork'),
                  Meal('Wild Rice Pork Chops', 'Pork'),
                  Meal('Tuna Noodle Casserole', 'Seafood'),
                  Meal('Pot Roast', 'Beef'),
                  Meal('Beef Stew', 'Beef'),
                  Meal('Jambalaya', 'Sausage'),
                  Meal('Chicken and Biscuits', 'Chicken'),
                  Meal('Lasagna', 'Sausage'),
                  Meal('Roasted Chicken', 'Chicken'),
                  Meal('Firecracker Shrimp Tacos', 'Seafood'),
                  Meal('Pasta Carbonara', 'Bacon'),
                  Meal('Marinated Flank Steak', 'Steak'),
                  Meal('DIY Mad Greens', 'Chicken'),
                  Meal('Chili Fig Pork Roast', 'Pork'),
                  Meal('Mushroom Ravioli', 'Vegetarian'),
                  Meal('Meatball Subs', 'Hamburger'),
                  Meal('Beans and Weanies', 'Sausage'),
                  Meal('Hamburger Pie', 'Hamburger'),
                  Meal('Lamb Kabobs', 'Lamb'),
                  Meal('Maple Mustard Chicken', 'Chicken'),
                  Meal('Spicy Tofu Udon', 'Vegetarian'),
                  Meal('Pork Tenderloin with Balsamic Reduction', 'Pork'),
                  Meal('Eat Out', 'Eat Out')]

    for meal in meals_list:

        if not s.query(FamilyMeals).filter(FamilyMeals.name == meal.name).all():
            add_meal = FamilyMeals(name=meal.name, protein=meal.protein)
            s.add(add_meal)
            s.commit()
    print s.query(FamilyMeals).count()


if __name__ == '__main__':
    build_meals_db()
