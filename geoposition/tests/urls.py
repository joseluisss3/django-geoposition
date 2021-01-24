from django.conf.urls import include, url
from django.contrib import admin

from example import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.poi_list),
    url(r'^admin/', include(admin.site.urls)),
]
