from django.conf import urls
from . import views

urlpatterns = [
    url('^$', views.gallery, name = 'gallery')
]