from django.shortcuts import render
from .models import Registration_Model
from .forms import Registration_Form
from django.http import HttpResponse,HttpResponseRedirect
import smtplib
from django.conf import settings
import random
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.

def check(request):
    return render(request,'maindummy.html')


# @login_required
def home(request):
    if request.session.has_key('email_id'):
        return render(request,'home/home.html')
    # return render(request,'home/login.html')
    return HttpResponseRedirect('/localhost/login')

def django(request):
    if request.session.has_key('email_id'):
        return render(request,'home/django.html')
    return HttpResponseRedirect('/localhost/login')


def restapi(request):
    if request.session.has_key('email_id'):
        return render(request,'home/restapi.html')
    return HttpResponseRedirect('/localhost/login')

def html(request):
    if request.session.has_key('email_id'):
        return render(request,'home/html.html')
    return HttpResponseRedirect('/localhost/login')

def css(request):
    if request.session.has_key('email_id'):
        return render(request,'home/css.html')
    return HttpResponseRedirect('/localhost/login')

def js(request):
    if request.session.has_key('email_id'):
        return render(request,'home/js.html')
    return HttpResponseRedirect('/localhost/login')

def bootstrap(request):
    if request.session.has_key('email_id'):
        return render(request,'home/bootstrap.html')
    return HttpResponseRedirect('/localhost/login')

def mysql(request):
    if request.session.has_key('email_id'):
        return render(request,'home/mysql.html')
    return HttpResponseRedirect('/localhost/login')

def mongodb(request):
    if request.session.has_key('email_id'):
        return render(request,'home/mongodb.html')
    return HttpResponseRedirect('/localhost/login')

def logout(request):
    del request.session['email_id']
    return HttpResponseRedirect('/localhost/login')

def signup_view(request):
    if request.method == "GET":
        form = Registration_Form()
        return render(request,'home/signup.html',{'form':form})
    elif request.method == "POST":
        form = Registration_Form(request.POST)
        if form.is_valid():
            model_obj = Registration_Model(
            first_name = form.cleaned_data['First_name'],
            last_name = form.cleaned_data['Last_name'],
            email_id = form.cleaned_data['Email_id'],
            phone_number = form.cleaned_data['Phone_number'],
            password = form.cleaned_data['Password'],
            conform_password = form.cleaned_data['Conform_password'],
            gender = form.cleaned_data.get('Gender'),
            age = form.cleaned_data.get('Age'),
            date_of_birth = form.cleaned_data.get('Date_of_birth'),
            qualification = form.cleaned_data.get('Qualification')
            )
            model_obj.save()
            # return HttpResponse('Your registration is successfull')
            return HttpResponseRedirect('/localhost/home')
        # return HttpResponse('form invalid')
        return render(request,'home/signup.html',{'form':form})

def login_view(request):
    if request.method == "GET":
        return render(request,'home/login.html')
    elif request.method == "POST":
        un = request.POST['e']
        pw = request.POST.get('p')
        model_obj = Registration_Model.objects.filter(email_id = un,password = pw)
        if model_obj:
            request.session['email_id'] = un
            request.session.set_expiry(600)
            return HttpResponseRedirect('/localhost/home')
        else:
            return render(request,'home/login.html')

em = ""
obj_id = 0
def to_mail(request):
    if request.method == "GET":
        return render(request,'home/to_mail.html')
    elif request.method == "POST":
        global em
        em = request.POST.get('e')
        model_obj = Registration_Model.objects.get(email_id = em)
        global obj_id
        obj_id = model_obj.id
        if model_obj:
            return render(request,'home/links.html')
        return HttpResponse('send proper mail')

def otp_to_mail(request):
    if request.method == "GET":
        otp = random.randrange(100000,999999)
        mail = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        subject = 'from django'
        message = 'otp:'+str(otp)
        To = [em,]
        send_mail(subject,message,settings.EMAIL_HOST_USER,To,fail_silently=True)
        response = render(request,'home/otp.html')
        response.set_cookie('otp',otp)
        return response
    elif request.method == "POST":
        user_otp = request.POST['otp']
        print(request.COOKIES['otp'])
        print(user_otp)
        if request.COOKIES['otp'] == user_otp:
            return HttpResponseRedirect('/localhost/change_password')
        return HttpResponse('otp not matched')

def change_password(request):
    if request.method == "GET":
        return render(request,'home/change_password.html')
    elif request.method == "POST":
        p1 = request.POST['p1']
        p2 = request.POST.get('p2')
        if p1 == p2:
            model_obj = Registration_Model.objects.get(id=obj_id)
            model_obj.password = p1
            model_obj.conform_password = p2
            model_obj.save()
            return HttpResponse('password changed')
        else:
            return HttpResponse('two fields must be same')

def link_to_mail(request):
    if request.method == "GET":
        mail = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        subject = 'from smtp'
        message = "Link : " + "http://127.0.0.1:8080/localhost/change_password"
        To = [em,]
        send_mail(subject,message,settings.EMAIL_HOST_USER,To,fail_silently=True)
        return HttpResponse('plese click on link')
