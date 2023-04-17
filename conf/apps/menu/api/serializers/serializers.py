from rest_framework import serializers
from apps.menu.models import Food, FoodCategory, Topping


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name',)


class FoodSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(many=True)

    class Meta:
        model = Food
        fields = ('name', 'description', 'price', 'is_special', 'is_vegan', 'is_publish', 'toppings')


class FoodCategorySerializer(serializers.ModelSerializer):
    foods = serializers.SerializerMethodField()

    class Meta:
        model = FoodCategory
        fields = ('id', 'name', 'foods')

    def get_foods(self, obj):
        foods = Food.objects.filter(category=obj, is_publish=True)

        is_vegan = self.context.get('request').query_params.get('is_vegan')
        if is_vegan is not None:
            foods = foods.filter(is_vegan=is_vegan)

        is_special = self.context.get('request').query_params.get('is_special')
        if is_special is not None:
            foods = foods.filter(is_special=is_special)

        toppings = self.context.get('request').query_params.getlist('topping')
        if toppings:
            foods = foods.filter(toppings__name__in=toppings)

        return FoodSerializer(foods, many=True).data
