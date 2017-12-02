from django.conf.urls import url
from example import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$',views.AboutPageView.as_view()),
    url(r'^profile/',views.ProfilePageView),
    url(r'^login/$', auth_views.login,name='login'),
    url(r'^register/$', views.UserSignUp, name='register'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/'},name='logout'),

]