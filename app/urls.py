from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    
    re_path(r'^$',views.index,name='index'),
    re_path(r'^new-hood/', views.create_hood, name='new-hood'),
    re_path(r'^join_hood/(?P<id>\w+)/', views.join_hood, name='join-hood'),
    re_path(r'^leave_hood/(?P<id>\w+)/', views.leave_hood, name='leave-hood'),
    re_path(r'^profile/(?P<id>\w+)/', views.profile, name='profile'),
    re_path(r'^update_profile/(?P<id>\w+)/', views.update_profile, name='update_profile'),
    re_path(r'^single_hood/(?P<id>\w+)/', views.single_hood, name='single-hood'),
    re_path(r'^add_post/(?P<id>\w+)/', views.hood_post, name='add-post'),
]   
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)