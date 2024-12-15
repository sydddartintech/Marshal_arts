from django.shortcuts import render,redirect
from martial_arts import models
from martial_arts import models
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
def admin_dashboard(request):
  registrations=models.Reg.objects.raw("select * from reg")
  masters=models.Master.objects.raw("select * from master")
  packages=models.Package.objects.raw("select * from package" )
  booking=models.Booking.objects.raw("select * from booking")
  context={
    'slist':len(registrations),
    'mlist':len(masters),
    'plist':len(packages),
    'blist':len(booking) }
  return render(request,"admin/admin.html",context)
def change_password(request):
    return render(request,"admin/change_password.html")
def update_password(request):
    username=request.session['semail']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']
    if new_password==confirm_password:
        log=models.Login.objects.filter(username=username)
        log.update(password=new_password)
        return render(request,"home/index.html")
    else:
         return render(request,"admin/change_password.html")
def View_registration(request):
	stud=models.Reg.objects.all()
	context={
	"stud_list":stud
	}
	return render(request,"admin/show_registrations.html",context)

def show_arts(request):
	arts=models.Arts.objects.all()
	context={
	"arts_list":arts
	}
	return render(request,"arts/show_arts.html",context)
def add_arts(request):
	return render(request,"arts/add_arts.html")


def save_arts(request):
    art_name = request.POST['artsname']
    art_desc = request.POST['description']
    # art_image = request.FILES['image']
    

    if request.method == 'POST' and request.FILES['image']:
          picture=request.FILES['image']
          fss = FileSystemStorage()
          file = fss.save(picture.name,picture)
          art =models.Arts(artsname=art_name, description=art_desc, image=picture)
          art.save()
          # obj_product=models.Product(category_id=category_id,product_name=pro_name,price=pro_price,picture=picture)
          # obj_product.save()
          messages.success(request,'saved successfully!!!')
    else:
          messages.error("Please select file");

    return redirect('show_arts')

def edit_arts(request,aid):
  arts=models.Arts.objects.get(artsid=aid)
  context={
    'alist':arts
  }
  return render(request,"arts/edit_arts.html",context)

def update_arts(request): 
    arts_id=request.POST['aid']
    arts_name=request.POST['artsname'] 
    arts_desc=request.POST['description']
    
    obj_arts=models.Arts.objects.get(artsid=arts_id)
    obj_arts.artsname=arts_name
    obj_arts.description=arts_desc
   
    obj_arts.save()
    messages.success(request,'updated successfully!!!!')
    return redirect('show_arts')

def delete_arts(request,aid):
    
    arts = models.Arts.objects.get(artsid=aid)
    arts_id = arts.artsid
    details_count = models.Package.objects.filter(fk_arts_id=arts_id).count()

    if details_count == 0:
       
        arts.delete()
        messages.success(request, 'Deleted successfully!!!!')
    else:
        
        messages.warning(request, 'Cannot delete Arts. Associated Packages  exist.')

    return redirect('show_arts')

def show_masters(request):
    master_list=models.Master.objects.raw("select * from arts a join master m on a.artsid =m.fk_art_id")
    # masters=models.Master.objects.all()
    context={
    # "masters_list":masters,
    "mlist":master_list
    }
    return render(request,"master/show_master.html",context)

def add_master(request):
    arts=models.Arts.objects.all()
    context={
    "arts_list":arts
    }
    return render(request,"master/add_master.html",context)

def save_master(request):
    arts_name=request.POST['art_name']
    master_name=request.POST['name']
    master_gender=request.POST['gender']
    master_profile=request.POST['profile']
    master_pno=request.POST['pno']
    master_email=request.POST['email']
    master_password=request.POST['password']
    
    user_type='master'
    

    # status='active'
    log_info = models.Login.objects.filter(username=master_email)
    obj_reg=models.Master(fk_art_id=arts_name,full_name=master_name,profile=master_profile,phone=master_pno,email=master_email,gender=master_gender)
    if len(log_info)==0:
      log_info=models.Login(username=master_email,password=master_password,usertype=user_type)
      log_info.save()
      obj_reg.save()
    else:
         messages.success(request,'Email id already exists.. Try another one!!')   
         return redirect('add_advocates')
    return  redirect('add_master')

def edit_master(request,mid):
     masters_list=models.Master.objects.get(master_id=mid)
     arts_list=models.Arts.objects.all()

     context= {"master":masters_list, "arts":arts_list
      }
     return render(request,"master/edit_master.html",context)

def update_master(request): 
    master_id=request.POST['mid']
    master_name=request.POST['name'] 
    master_profile=request.POST['profile']
    master_pno=request.POST['pno']
    obj_master=models.Master.objects.get(master_id=master_id)
    obj_master.full_name=master_name
    obj_master.profile=master_profile
    obj_master.phone=master_pno
    obj_master.save()
    messages.success(request,'updated successfully!!!!')
    return redirect('show_masters')

def delete_master(request,mid):
    cust=models.Master.objects.get(master_id=mid)
    cust.delete()
    messages.success(request,'Deleted successfully!!!!')
    return redirect('show_masters')

def show_packages(request):
  package=models.Package.objects.raw("select * from package as p join arts as a on p.fk_arts_id=a.artsid")
  context={
  'p_list':package
  }
  return render(request,"admin/show_packages.html",context)

def add_packages(request):
  arts=models.Arts.objects.all()
  context={
  'arts_list':arts
  }
  return render(request,"admin/add_packages.html",context)

def save_package(request):
    title = request.POST['title']
    duration = request.POST['dur']
    cost = request.POST['cost']
    arts = request.POST['art_name']

    
    p_arts =models.Package.objects.filter(fk_arts_id=arts)
    
    if p_arts.exists():
        messages.success(request, 'Package Already Exists')
    else:
        
        package =models.Package(package_title=title,fk_arts_id=arts,duration=duration,cost=cost)
        package.save()
        return redirect("show_packages")

    
    return redirect("show_packages")

def delete_package(request,pid):
    
    packages = models.Package.objects.get(packgeid=pid)
        
    package_id = packages.packgeid
      
    sh_count = models.Scheduling.objects.filter(fk_package_id=package_id).count()

    if sh_count == 0:
        
        packages.delete()
        messages.success(request, 'Deleted successfully!!!!')
    else:
        
        messages.warning(request, 'Cannot delete package. Associated schedule  exist.')

    return redirect('show_packages')

def schedule(request,pid):
  package=models.Package.objects.get(packgeid=pid)
  package_id=package.packgeid
  schedule=models.Scheduling.objects.raw("select * from scheduling as s join package as p on s.fk_package_id=p.packgeid where s.fk_package_id=%s",[pid])
  context={
  'pack_id':package_id,
  'sh_list':schedule
  }
  return render(request,"admin/view_schedule.html",context)

def save_schedule(request):
  pid=request.POST['package_id']
  date=request.POST['date']
  time_from=request.POST['t1']
  time_to=request.POST['t2']

  obj_schedule=models.Scheduling(time_from=time_from,time_to=time_to,date=date,fk_package_id=pid)
  obj_schedule.save()
  return redirect("schedule",pid=pid)

def delete_schedule(request,sid):
  sch_list=models.Scheduling.objects.get(scheduleid=sid)
  pid=sch_list.fk_package_id
  sch_list.delete()
  return redirect("schedule",pid=pid)

def view_booking(request):
  bookings=models.Booking.objects.raw("select * from booking as b join package as p on b.fk_package_id=p.packgeid join arts as a on p.fk_arts_id=a.artsid join Reg as r on b.fk_reg_id=r.reg_id")
  context={
  'blist':bookings
  }
  return render(request,"admin/view_booking.html",context)

def fee_invoice(request,bid):
  booking=models.Booking.objects.get(bookid=bid)
  book_id=booking.bookid
  packages=models.Package.objects.raw("select * from booking  b join package p on b.fk_package_id=p.packgeid where b.bookid=%s",[bid])
  fees=models.Studentfee.objects.raw("select * from studentfee sf join booking b on (sf.fk_book_id=b.bookid) join reg r on (r.reg_id=fk_reg_id) where sf.fk_book_id=%s",[book_id])
  context={
  'plist':packages[0],
  'bookid':book_id,
  'fe_list':fees
  }
  return render(request,"admin/fee_invoice.html",context)
  # return HttpResponse(book_id)

def save_invoice(request):
  amount=request.POST['amt']
  due_date=request.POST['duedate']
  bookid=request.POST['bid']
  status='invoice'

  invoice=models.Studentfee(fk_book_id=bookid,amount=amount,due_date=due_date,status=status)
  invoice.save()
  return redirect("fee_invoice",bid=bookid)

def view_feedback(request):
  feedback=models.Feedback.objects.raw("select * from reg as r join feedback as f on r.emailid=f.sender")
  context={
  'fe_list':feedback
  }
  return render(request,"admin/view_feedback.html",context)

def view_video_tips(request):
  videos=models.VideoTips.objects.raw("select * from master as m join video_tips as v on m.fk_art_id=v.fk_arts_id join arts as a on a.artsid=v.fk_arts_id where m.fk_art_id=v.fk_arts_id")
  context={
  'vlist':videos
  }
  return render(request,"admin/view_video_tips.html",context)

def delete_video(request,vid):
	videos=models.VideoTips.objects.get(tips_id=vid)
	videos.delete()
	messages.success(request, 'Video tip delete successfully.')
	return redirect("video_tips_show")

