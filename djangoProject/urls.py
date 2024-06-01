from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recommend_games.urls')),  # Include the recommendations app's URLs
]
