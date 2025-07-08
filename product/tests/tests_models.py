import pytest
from decimal import Decimal

from product.models import Product
from product.models import Category

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name="Test Product",
        description="Test Description",
        price=Decimal("100.00"),
    )

    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == Decimal("100.00")

@pytest.mark.django_db
def test_category_creation():
    category = Category.objects.create(
        name="Test Category",
        description="Test Description",
        slug="test-category",
        active=True,
    )

    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.slug == "test-category"
    assert category.active is True
    assert str(category) == "Test Category"