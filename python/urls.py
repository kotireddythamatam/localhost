from django.urls import path
from . import views
urlpatterns = [
    # path('python',views.python),
    # path('basic_python',views.basic_python),
    # path('iq',views.python_interview_question),
    path('quiz',views.python_quiz),
    path('q',views.pyth_quiz),
]
