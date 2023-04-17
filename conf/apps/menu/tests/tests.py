from unittest import TestCase

from rest_framework.test import APITestCase
from django.urls import reverse

from apps.menu.api.serializers.serializers import FoodCategorySerializer, ToppingSerializer, FoodSerializer
from apps.menu.models import *


class FoodModelTestCase(TestCase):
    def setUp(self):
        self.topping = Topping.objects.create(name='Cheese')
        self.category = FoodCategory.objects.create(name='Pizza', is_publish=True)

    def test_create_food(self):
        food = Food.objects.create(
            category=self.category,
            name='Margherita',
            description='description',
            price=100,
            is_special=False,
            is_vegan=False,
        )
        food.toppings.set([self.topping])

        self.assertEqual(food.name, 'Margherita')
        self.assertEqual(food.description, 'description')
        self.assertEqual(food.price, 100)
        self.assertFalse(food.is_special)
        self.assertFalse(food.is_vegan)
        self.assertTrue(food.is_publish)


class FoodCategoryListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.topping = Topping.objects.create(name='Cheese')
        self.pizza_category = FoodCategory.objects.create(name='Pizza', is_publish=True)
        self.pizza_margherita = Food.objects.create(
            category=self.pizza_category,
            name='Margherita',
            description='description',
            price=100,
            is_special=False,
            is_vegan=False,
        )
        self.pizza_margherita.toppings.set([self.topping])

        self.pasta_category = FoodCategory.objects.create(name='Pasta', is_publish=True)
        self.pasta_bolognese = Food.objects.create(
            category=self.pasta_category,
            name='Bolognese',
            description='description',
            price=150,
            is_special=False,
            is_vegan=False,
        )
        self.pasta_bolognese.toppings.set([self.topping])

    def test_list_food_categories_with_filters(self):
        url = reverse('food-list') + '?is_vegan=True&topping=Cheese'
        response = self.client.get(url)
        expected_data = FoodCategorySerializer(self.pizza_category, context={'request': response}).data
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, expected_data)


class ToppingSerializerTestCase(TestCase):
    def test_serialization(self):
        topping = Topping.objects.create(name='Mushrooms')
        serializer = ToppingSerializer(topping)
        expected_data = {'name': 'Mushrooms'}
        self.assertEqual(serializer.data, expected_data)


class FoodSerializerTestCase(TestCase):
    def test_serialization(self):
        topping = Topping.objects.create(name='Mushrooms')
        food = Food.objects.create(name='Pizza', description='Delicious pizza', price=10.0, is_special=True, is_vegan=False, is_publish=True)
        food.toppings.add(topping)
        serializer = FoodSerializer(food)
        expected_data = {'name': 'Pizza', 'description': 'Delicious pizza', 'price': 10.0, 'is_special': True, 'is_vegan': False, 'is_publish': True, 'toppings': [{'name': 'Mushrooms'}]}
        self.assertEqual(serializer.data, expected_data)
