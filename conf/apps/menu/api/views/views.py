from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from apps.menu.api.filters import FoodCategoryFilter
from apps.menu.models import Food, FoodCategory
from apps.menu.api.serializers.serializers import FoodCategorySerializer


class FoodCategoryListAPIView(ListAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

