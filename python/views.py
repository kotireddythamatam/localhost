from django.shortcuts import render
from .models import Python_Interview_Question_Answer,Quiz
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
# def python(request):
#     return render(request,'python/python.html')

# def basic_python(request):
#     return render(request,'python/basic_python.html')

# def python_interview_question(request):
#     model_obj = Python_Interview_Question_Answer.objects.all()
#     return render(request,'python/iq.html',{'iq':model_obj})

def python_quiz(request):
    if request.method == "GET":
        model_obj = Quiz.objects.all()
        print(model_obj)
        return render(request,'python/quiz.html',{'quiz':model_obj})
    elif request.method == "POST":
        print(request.POST)
        score = 0
        for i in range(1,4):
            form = request.POST.get(i)
            print(form[i][0])
            model_obj = Quiz.objects.get(answer=form[i][0])
            if model_obj:
                score +=1
                return HttpResponse(score)

id = 1
def pyth_quiz(request):
    while True:
        if request.method == "GET":
            id = 1
            print('id GET: ',id)
            model_obj = Quiz.objects.get(id=id)
            return render(request,'python/qqq.html',{'data':model_obj})
        elif request.method == "POST":
            id = 1
            print('id POST: ',id)
            pk = str(id)
            form = request.POST.get(pk)
            model_obj = Quiz.objects.get(id=id)
            if model_obj.answer == form:
                return HttpResponseRedirect('/localhost/q')
            id
            id += 1
            return HttpResponseRedirect('/localhost/q')
    return HttpResponse('ok')


        # print(request.POST['q'])
        # form = request.POST['2q']
        # model_obj = Quiz.objects.filter(answer=form)
        # if model_obj:
        #     return HttpResponse('successful')
        # return HttpResponse('failed')
