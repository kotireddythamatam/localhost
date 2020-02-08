from django.contrib import admin
from .models import Python_Interview_Question_Answer,Quiz
# Register your models here.
class Adminanswer(admin.ModelAdmin):
    list_display = ['question','answer']

admin.site.register(Python_Interview_Question_Answer,Adminanswer)

class Adminquiz(admin.ModelAdmin):
    list_display = ['quiz_question','option_a','option_b','option_c','option_d','answer']
admin.site.register(Quiz,Adminquiz)
