import pytest
from decimal import Decimal
from django.contrib.auth.models import User

from order.models import Order
from product.models.product import Product

@pytest.mark.django_db
def test_order_creation():
    # User creation
    user = User.objects.create_user(
        username="user",
        email="user@email.com",
        password="123456"
    )

    # First product creation
    product1 = Product.objects.create(
        name="Test Product",
        description="Test Description",
        price=Decimal("5.50")
    )

    # Second product creation
    product2 = Product.objects.create(
        name="Test Product 2",
        description="Test Description 2",
        price=Decimal("59.50")
    )

    # Order creation
    order = Order.objects.create(user=user)
    order.product.set([product1, product2])

    assert order.user == user
    assert order.product.count() == 2
    assert product1 in order.product.all()
    assert product2 in order.product.all()