from django.contrib import admin
from django.urls import include, path, re_path

from accounts.views import (
    login_view,
    logout_view,
    register_view
)

from meals.views import meal_queue_toggle_view

from search.views import search_view
from .views import home_view

urlpatterns = [
    path('', home_view), # index / home / root 
    path('pantry/recipes/', include('recipes.urls')),
    path('articles/', include('articles.urls')),
    path('meal-toggle/<int:recipe_id>/', meal_queue_toggle_view, name='meal-toggle'),
    path('search/', search_view, name='search'),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]