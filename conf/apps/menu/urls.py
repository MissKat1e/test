from django.urls import path
from apps.menu.api.views.views import FoodCategoryListAPIView


urlpatterns = [
    path('foods/', FoodCategoryListAPIView.as_view(), name='food-list'),
]
