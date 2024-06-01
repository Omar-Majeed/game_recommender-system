from django.urls import path
from .views import RecommendationView

urlpatterns = [
    #path('recommend/<str:game_name>', RecommendationView.as_view(), name='recommend'),
    path('recommend/', RecommendationView.as_view(), name='recommend'),
]
