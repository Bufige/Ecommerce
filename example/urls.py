from django.conf.urls import url , include
from example import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name = 'home'),    
    url(r'^profile/',views.ProfilePageView,name='profile'),
    url(r'^login/$', views.UserLogin,name='login'),
    url(r'^register/$', views.UserSignUp, name='register'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/'},name='logout'),
    url(r'^addcart/(?P<id>[0-9]+)/$',views.AddCart,name='addcart'),
    url(r'^cart/$', views.CartPageView, name='cart'),
    url(r'^checkout/$',views.CheckOutPageView, name = 'checkout'),
    url(r'^success/', views.SuccessPageView, name='success'),
]