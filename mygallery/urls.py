from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$', views.gallery, name = 'gallery'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'^category/(\d+)', views.category, name='category'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^locations/$', views.image_location, name='image_location'),
    url(r'^copy/(\d+)', views.copy_image, name='copy')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)