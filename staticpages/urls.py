from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    url(r'^$', views.landing, name='landing'),
]


app_name = 'staticpages'