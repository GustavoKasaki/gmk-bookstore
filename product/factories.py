import factory

from product.models import Product
from product.models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.faker.Faker('name')
    slug = factory.faker.Faker('slug')
    description = factory.Faker('text')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    price = factory.Faker('pyint')
    category = factory.LazyAttribute(CategoryFactory)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)
                
    class Meta:
        model = Product