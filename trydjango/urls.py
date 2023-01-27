
from django.contrib import admin
from django.urls import include, path, re_path

from accounts.views import (
    login_view,
    logout_view,
    register_view
)
from django.conf import settings
from django.conf.urls.static import static


from search.views import search_view
from .views import home_view

urlpatterns = [
    path('', home_view), # index / home / root 
    path('pantry/recipes/', include('recipes.urls')),
    path('articles/', include('articles.urls')),
    path('search/', search_view, name='search'),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
