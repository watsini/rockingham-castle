from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.exc import OperationalError

Base = declarative_base()
engine = create_engine('sqlite:///recipebox.sqlite')
session = sessionmaker()
session.configure(bind=engine)
s = session()

class Main_Dish(Base):
    __tablename__ = 'maindish'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cuisine = Column(String(250))
    protein = Column(String(250))
    preferred_sides = Column(String(2500))
    ingredients = Column(String(2500))
    prep_instructions = Column(String(2500))

class Recipe(Base):
    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    main_id = Column(Integer, ForeignKey('maindish.id'))
    main = relationship(Main_Dish)




def build_recipe_db():

    add_main = Main_Dish(name="test_meal", protein="test_pro")
    s.add(add_main)
    s.commit()

    add_recipe = Recipe(name="e", main=add_main)
    s.add(add_recipe)
    s.commit()

    recipedb = s.query(Recipe).all()

    for rec in recipedb:
        print rec.main.name


if __name__ == '__main__':
    try:
        Base.metadata.create_all(engine)
    except OperationalError:
        print "The database is is intialized... creating"
        Base.metadata.create_all(engine)
    finally:
        build_recipe_db()
