import pytest
from django.contrib.auth.models import User

from order.models import Order
from product.models import Product, Category
from order.serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer():
    # User creation
    user = User.objects.create_user(
        username="user",
        email="user@email.com",
        password="123456"
    )

    # Products creation
    product1 = Product.objects.create(
        title="Test Product",
        description="Test Description",
        price=5.50,
        active=True
    )
    product2 = Product.objects.create(
        title="Test Product 2",
        description="Test Description 2",
        price=59.50,
        active=True
    )

    # Categories creation
    category1 = Category.objects.create(
        title="Test Category",
        slug="test-category",
        description="Test Category Description",
        active=True
    )
    category2 = Category.objects.create(
        title="Test Category 2",
        slug="test-category-2",
        description="Test Category Description 2",
        active=True
    )

    # Category association
    product1.category.set([category1])
    product2.category.set([category2])

    # Order creation
    order = Order.objects.create(user=user)
    order.product.set([product1, product2])

    # Serialization
    serializer = OrderSerializer(order)
    data = serializer.data

    # Assertion
    assert data['total'] == 65
    assert len(data['product']) == 2

    product1_data = next(product for product in data['product'] if product['title'] == 'Test Product')
    assert product1_data['title'] == 'Test Product'
    assert product1_data['description'] == 'Test Description'
    assert product1_data['price'] == 5.50
    assert product1_data['category'][0]['slug'] == 'test-category'
    assert product1_data['active'] is True

    product2_data = next(product for product in data['product'] if product['title'] == 'Test Product 2')
    assert product2_data['title'] == 'Test Product 2'
    assert product2_data['description'] == 'Test Description 2'
    assert product2_data['price'] == 59.50
    assert product2_data['category'][0]['slug'] == 'test-category-2'
    assert product2_data['active'] is True
