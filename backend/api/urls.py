from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (IngredientViewSet, TagViewSet,
                    RecipeViewSet, UserSubscriptionsViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('tags', TagViewSet, basename='tags')
router.register('recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('users/subscriptions/',
         UserSubscriptionsViewSet.as_view({'get': 'list'})),
    path('users/<int:user_id>/subscribe/',
         UserSubscriptionsViewSet.as_view(
             {'post': 'post', 'delete': 'delete'}
         )),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
