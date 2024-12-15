from django.shortcuts import render,redirect
from martial_arts import models
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.contrib import messages
# Create your views here.
def master_dashboard(request):
	mid = request.session.get('master_id', None)
	registrations=models.Reg.objects.raw("select * from reg as r join booking as b on r.reg_id=b.fk_reg_id where b.fk_master_id=%s",[mid])
	vtips=models.VideoTips.objects.raw("select * from master as m join video_tips as v on m.fk_art_id=v.fk_arts_id where m.master_id=%s",[mid])
	feedback=models.Feedback.objects.raw("select * from Feedback")
	context={
		'rlist':len(registrations),
		'vlist':len(vtips),
		'flist':len(feedback)
	}
	return render(request,"master_dashboard/master.html",context)

def change_pass(request):
    return render(request,"admin/change_password.html")
def update_pass(request):
    username=request.session['semail']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']
    if new_password==confirm_password:
        log=models.Login.objects.filter(username=username)
        log.update(password=new_password)
        return render(request,"home/index.html")
    else:
         return render(request,"admin/change_password.html")
def master_profile(request):
	mid = request.session.get('master_id', None)
	master=models.Master.objects.raw("select * from master as m join arts as a on m.fk_art_id=a.artsid where m.master_id=%s",[mid])
	context={
	'profile':master[0]
	}
	return render(request,"master_dashboard/my_profile.html",context)
def edit_prof(request):
	mid = request.session.get('master_id', None)
	prof=models.Master.objects.get(master_id=mid)
	context={
	'profile':prof
	}
	return render(request,"master_dashboard/edit_prof.html",context)

def update_prof(request):
	uname = request.session.get('semail', None)
	name=request.POST['name']
	gen=request.POST['gender']
	address=request.POST['addr']
	phno=request.POST['pno']
	

	master=models.Master.objects.get(email=uname)
	master.full_name=name
	master.gender=gen
	master.profile=address
	master.phone=phno
	
	master.save()
	return redirect("master_profile")

def view_students(request):
	mid = request.session.get('master_id', None)
	students=models.Reg.objects.raw("select * from reg as r join booking as b on r.reg_id=b.fk_reg_id join package as p on p.packgeid=b.fk_package_id join arts as a on a.artsid=p.fk_arts_id join master as m on m.master_id=b.fk_master_id where m.master_id=%s",[mid])
	context={
	'st_list':students
	}
	return render(request,"master_dashboard/students_view.html",context)

def feedback_view(request):
	feedback=models.Feedback.objects.raw("SELECT * FROM feedback f INNER JOIN reg r ON f.sender=r.emailid;")
	context={
	'flist':feedback
	}
	return render(request,"master_dashboard/feedback_view.html",context)

def video_tips_show(request):
	mid = request.session.get('master_id', None)
	videos=models.VideoTips.objects.raw("select * from master as m join video_tips as v on m.fk_art_id=v.fk_arts_id where m.master_id=%s",[mid])

	arts=models.Arts.objects.all()
	context={
	'alist':arts,
	'vlist':videos
	}
	return render(request,"master_dashboard/video_tips.html",context)

# def add_video(request):
# 	mid = request.session.get('master_id', None)
# 	title=request.POST['title']
# 	description=request.POST['desc']
# 	linkid=request.POST['link']
# 	arts=request.POST['arts']
	

# 	art_count = models.Master.objects.filter(fk_art_id=arts, master_id=mid).count()
# 	if art_count > 0:
# 		videos=models.VideoTips(title=title,description=description,video_url=linkid,fk_arts_id=arts)
# 		videos.save()
# 		return redirect("video_tips_show")

# 	else:
# 		return redirect("video_tips_show")
def new_video(request):
	arts=models.Arts.objects.all()
	context={
	'alist':arts
	}
	return render(request,"master_dashboard/video_tips_add.html",context)

def add_video(request):
    mid = request.session.get('master_id', None)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('desc')
        linkid = request.POST.get('link')
        arts = request.POST.get('arts')

        art_count = models.Master.objects.filter(fk_art_id=arts, master_id=mid).count()

        if art_count > 0:
            video = models.VideoTips(title=title, description=description, video_url=linkid, fk_arts_id=arts)
            video.save()
            messages.success(request, 'Video tip added successfully.')
            return redirect("video_tips_show")
        else:
            messages.error(request, 'You do not have permission to add video tips for this art.')
            return redirect("video_tips_show")

    return redirect("video_tips_show")

def delete_video(request,vid):
	videos=models.VideoTips.objects.get(tips_id=vid)
	videos.delete()
	messages.success(request, 'Video tip delete successfully.')
	return redirect("video_tips_show")

	