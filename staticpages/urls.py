from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    #url(r'^login2/', views.login2, name='login2'),
    #url(r'^dashboard/', views.dashboard, name='dashboard'),
    #url(r'^register/', views.register, name='register'),
    #url(r'^forgot/', views.forgot, name='forgot'),
    #url(r'^charts/', views.charts, name='charts'),
    #url(r'^tables/', views.tables, name='tables'),
    #url(r'^testapi/', views.testapi, name='testapi'),
    
    
]


app_name = 'staticpages'