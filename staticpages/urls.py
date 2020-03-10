from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^forgot/', views.forgot, name='forgot'),
    url(r'^charts/', views.charts, name='charts'),
    url(r'^tables/', views.tables, name='tables'),
    
]


app_name = 'staticpages'