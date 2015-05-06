import factory
import factory.fuzzy

from .models import BreadTestModel, BreadTestModel2


class BreadTestModel2Factory(factory.DjangoModelFactory):
    FACTORY_FOR = BreadTestModel2

    text = factory.fuzzy.FuzzyText(length=10)


class BreadTestModelFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BreadTestModel

    name = factory.fuzzy.FuzzyText(length=10)
    other = factory.SubFactory(BreadTestModel2Factory)
