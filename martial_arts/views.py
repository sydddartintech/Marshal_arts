from django.shortcuts import render,redirect
from django.utils import timezone
from martial_arts import models
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.sessions.models import Session
import random
from martial_arts.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
def home(request):
    return render(request,"home/index.html")
def about(request):
    return render(request,"home/about.html")
def login(request):
    # request.session.flush()
    return render(request,"login/login.html")
def check_login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    log_info = models.Login.objects.filter(username=username,password=password)
    for info in log_info:
    
        if info.username==username and info.password==password:
            if info.usertype=='admin':
                request.session['semail']=info.username
                request.session['usertype']=info.usertype
                return redirect("../administrator/admin_dashboard")
            
            elif info.usertype=='student':
                request.session['semail']=info.username
                request.session['usertype']=info.usertype
                return redirect("../student/student_dashboard")

            elif info.usertype == 'master':
                    request.session['semail'] = info.username
                    master_list=models.Master.objects.filter(email=info.username)
                    if(len(master_list)>0):
                        masters= master_list[0];
                        request.session['master_id'] = masters.master_id
                        request.session['usertype'] = info.usertype
                        request.session['name'] = masters.full_name
                        return redirect("../master/master_dashboard")
                    else:
                        messages.error(request,'Master  not Found')
                        return redirect('login')
    messages.error(request,'Invalid Data')
    return redirect('login')
def register(request):
    # request.session.flush()
    return render(request,"registration/register.html")
def student(request):
    student_name=request.POST['name']
    student_pno=request.POST['phone']
    student_gender=request.POST['gender']
    student_address=request.POST['address']
    student_dob=request.POST['dob']
    # student_dob_date = timezone.datetime.strptime(student_dob, '%Y-%m-%d').date()
    
    student_email=request.POST['email']
    student_password=request.POST['password']
    user_type='student'
    current_date = timezone.now().date()
    log_info = models.Login.objects.filter(username=student_email)
    obj_reg=models.Reg(name=student_name,address=student_address,phoneno=student_pno,gender=student_gender,emailid=student_email,dob=student_dob,usertype=user_type,doj=current_date)
    # status='active'
    if len(log_info)==0:
        log_info=models.Login(username=student_email,password=student_password,usertype=user_type)
        log_info.save()
        obj_reg.save()
    else:
         messages.success(request,'Email id already exists.. Try another one!!')   
         return redirect('register')
    return  redirect('login')
def logout(request):
    Session.objects.all().delete()
    return redirect('home')
def forgot(request):
    return render(request,"login/forgot.html")
def email_verify(request):
    if request.method=='POST':
        username=request.POST.get('username')
        log_info=models.Login.objects.filter(username=username)
        for info in log_info:
          if info.username==username:
               otp=str(random.randint(1000,9999))
               request.session['otp']=otp
               request.session['otpemail']=info.username
               subject='PASSWORD RESETTING FOR TALENT HUNT PROGRAM MANAGEMENT'
               message="Your OTP is:"+otp
               email_id=request.session['otpemail']
               send_mail(subject,message,EMAIL_HOST_USER,[email_id],fail_silently=False)
               return render(request,'login/val_otp.html')
          else:
              messages.error(request,'Invalid Email Address')
              return redirect("forgot")
    messages.error(request,'Invalid Email Address')
    return redirect("forgot")
def val_otp(request):
    if request.method == "POST":
        otp_now = request.POST.get('otp_code')
        otp = request.session['otp']
        if otp_now == otp:
           return render(request, "login/newpassword.html")
        else:
         messages.error(request, 'Invalid OTP')

    messages.error(request, 'Invalid Data Entered')
        
    return render(request, "login/val_otp.html")
def newpassword(request):
    new_password=request.POST['newpassword']
    confirm_password=request.POST['confirmpassword']
    username=request.session['semail']
    if new_password==confirm_password:
      log=models.Login.objects.filter(username=username)
      log.update(password=new_password)
    return redirect('login')