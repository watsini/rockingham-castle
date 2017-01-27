import random
from recipe_box_interface import import_mains_table
from datetime import datetime

DAYS = ['M', 'T', 'W', 'TH', 'F', 'S', 'SU']


def menu_generator(weeks):
    meal_list = import_mains_table()
    last_week_menu = []
    for i in range(weeks):
        menu = []

        while len(menu) < 7:

            random_meal = random.choice(meal_list)
            if random_meal not in menu and random_meal not in last_week_menu:

                for meal in menu:
                    if random_meal.protein == meal.protein:
                        break
                else:
                    menu.append(random_meal)

        print "Week {}: {}".format(i, [str(meal.name) for meal in menu])

        last_week_menu = menu


if __name__ == '__main__':

    try:
        WEEKS = int(raw_input('How many weeks do you want to plan? '))
        menu_generator(WEEKS)
    except IndexError:
        print "You are too picky out of options"
    except ValueError:
        print "Not a Number!"
