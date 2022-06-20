from . import views
from django.urls import path
from django.conf.urls.static import static
from neighbour import settings
from django.contrib.auth import views as auth_views

app_name = 'business'
urlpatterns = [
    path('search', views.Search, name="Search"),
    path('<str:username>/businesses/', views.MyBusinesses, name='MyBusinesses'),
    path('<str:username>/add/business/', views.AddBusiness, name='AddBusiness'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)