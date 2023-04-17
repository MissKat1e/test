import django_filters

from apps.menu.models import FoodCategory


class FoodCategoryFilter(django_filters.FilterSet):
    topping_name = django_filters.CharFilter(field_name='foods__toppings__name', lookup_expr='iexact')

    class Meta:
        model = FoodCategory
        fields = ['topping_name']