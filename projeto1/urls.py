
from django.contrib import admin

from django.conf.urls import url

from agenda import views
from biblioteca import views

urlpatterns = [
    url(r'r^$',views.index, name='index'),
    url(r'^$',views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
