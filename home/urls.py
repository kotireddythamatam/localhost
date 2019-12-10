from django.urls import path
from home import views
urlpatterns = [
    path('home/',views.home),
    path('signup/',views.signup_view),
    path('login',views.login_view),
    path('to_mail',views.to_mail),
    path('otp_to_mail',views.otp_to_mail),
    path('change_password',views.change_password),
    path('link_to_mail',views.link_to_mail),
    path('mongodb',views.mongodb),
    path('logout',views.logout),
    path('check',views.check),

    path('django',views.django),
    path('restapi',views.restapi),
    path('html',views.html),
    path('css',views.css),
    path('js',views.js),
    path('bootstrap',views.bootstrap),
    path('mysql',views.mysql),
]
