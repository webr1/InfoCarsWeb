from django.urls import path
from .views import car_detail,about_us,home_page,LoginView,LoginCustomView,SignUp,LogoutView_1
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home_page, name='home'),
    path('sign/',SignUp.as_view(),name='signup'),
    path('login/',LoginCustomView.as_view(),name="login") ,
    path('detail/<int:id>/', car_detail, name='detail'),
    path('aboutus/',about_us,name="about"),
    path('logout/',LogoutView_1.as_view(),name="logout")
]