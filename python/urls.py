from django.urls import path
from . import views
urlpatterns = [
    path('python',views.python),
    path('basic_python',views.basic_python),
]
