from . import views
from django.urls import path
from django.conf.urls.static import static
from neighbour import settings
from django.contrib.auth import views as auth_views

app_name = 'business'
urlpatterns = [
    path('search', views.Search, name="search"),
    path('addbusiness/<str:username>/', views.AddBusiness, name='addbusiness'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)