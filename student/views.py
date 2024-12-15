from django.shortcuts import render,redirect
from martial_arts import models
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages
def student_dashboard(request):
	uname = request.session.get('semail', None)
	reg=models.Reg.objects.get(emailid=uname)
	reg_id=reg.reg_id
	packages=models.Package.objects.raw("SELECT * FROM package AS p JOIN Arts AS a ON p.fk_arts_id=a.artsid")
	videos=models.VideoTips.objects.raw("select * from video_tips v join package p on v.fk_arts_id=p.fk_arts_id join booking b on b.fk_package_id=p.packgeid where b.fk_reg_id=%s",[reg_id])
	bookings=models.Booking.objects.raw("select * from package as p join booking as b on p.packgeid=b.fk_package_id join arts as a on p.fk_arts_id=a.artsid where b.fk_reg_id=%s",[reg_id])
	context={
    
    'plist':len(packages),
	'vlist':len(videos),
	'blist':len(bookings)
	}
	return render(request,"student/student.html",context)
def password_change(request):
    return render(request,"student/password_change.html")
def password_update(request):
    username=request.session['semail']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']
    if new_password==confirm_password:
        log=models.Login.objects.filter(username=username)
        log.update(password=new_password)
        return render(request,"home/index.html")
    else:
        return render(request,"student/password_change.html")
def view_profile(request):
	uname = request.session.get('semail', None)
	student=models.Reg.objects.get(emailid=uname)
	context={
	'stud':student
	}
	return render(request,"student/profile.html",context)

def edit_profile(request):
	uname = request.session.get('semail', None)
	student=models.Reg.objects.get(emailid=uname)
	context={
	'stud':student
	}
	return render(request,"student/edit_profile.html",context)

def update_profile(request):
	uname = request.session.get('semail', None)
	name=request.POST['name']
	gen=request.POST['gender']
	address=request.POST['addr']
	phno=request.POST['pno']
	dob=request.POST['dob']

	student=models.Reg.objects.get(emailid=uname)
	student.name=name
	student.gender=gen
	student.address=address
	student.phoneno=phno
	student.dob=dob
	student.save()
	return redirect("view_profile")

def feedback(request):
	uname = request.session.get('semail', None)
	feedbacks=models.Feedback.objects.filter(sender=uname)
	context={
	'sender':uname,
	'fe_li':feedbacks
	}
	return render(request,"student/feedback.html",context)

def save_feedback(request):
	subject=request.POST['sub']
	message=request.POST['msg']
	sender=request.POST['sender']

	feedback_date = timezone.now().date()

	obj_feedback=models.Feedback(subject=subject,message=message,sender=sender,date=feedback_date)
	obj_feedback.save()
	return redirect("feedback")

def show_packages_stud(request):
    uname = request.session.get('semail', None)
    reg = models.Reg.objects.get(emailid=uname)
    reg_id = reg.reg_id

    # Use filter instead of get to get a queryset
    bookings = models.Booking.objects.filter(fk_reg_id=reg_id)

    # Initialize is_booked to False
    is_booked = False

    if bookings.exists():  # Check if there are any bookings
        pack_id = bookings.first().fk_package_id  # Assuming you want the package ID of the first booking
        booking_count = bookings.count()

        # Update is_booked based on the booking count
        is_booked = booking_count > 0

    # Assuming you want to join Arts and Master tables to the Package table
    packages = models.Package.objects.raw("SELECT * FROM package AS p JOIN Arts AS a ON p.fk_arts_id=a.artsid")

    context = {
        'plist': packages,
        'is_booked': is_booked
    }

    return render(request, "student/packages_view.html", context)


# def show_packages_stud(request):
# 	uname = request.session.get('semail', None)
# 	reg=models.Reg.objects.get(emailid=uname)
# 	reg_id=reg.reg_id
# 	bookings=models.Booking.objects.get(fk_reg_id=reg_id)
# 	pack_id=bookings.fk_package_id
# 	packages=models.Package.objects.raw("select * from package as p join Arts as a on p.fk_arts_id=a.artsid join master as m on a.artsid=m.fk_art_id")
# 	booking_count =models.Booking.objects.filter(fk_package_id=pack_id, fk_reg_id=reg_id).count()
# 	if booking_count > 0:
# 		is_booked = True
# 	context={
# 	'plist':packages,
# 	'is_booked':is_booked
# 	}
# 	return render(request,"student/packages_view.html",context)

def view_pak_schedule(request,pid):
	schedules=models.Scheduling.objects.raw("select * from scheduling as s join package as p on s.fk_package_id=p.packgeid join arts as a on a.artsid=p.fk_arts_id where s.fk_package_id=%s",[pid])
	context={
	'slist':schedules
	}
	return render(request,"student/schedules.html",context)

def book_package(request,pid):
	uname = request.session.get('semail', None)
	reg=models.Reg.objects.get(emailid=uname)
	reg_id=reg.reg_id
	packages=models.Package.objects.get(packgeid=pid)
	pack_id=packages.packgeid
	arts_id=packages.fk_arts_id
	master=models.Master.objects.get(fk_art_id=arts_id)
	mid=master.master_id

	book_date = timezone.now().date()
	pack_count = models.Booking.objects.filter(fk_package_id=pack_id).count()
	if pack_count == 0:
		pack_book=models.Booking(fk_reg_id=reg_id,fk_master_id=mid,fk_package_id=pack_id,booking_date=book_date)
		pack_book.save()
		messages.success(request, 'Booked successfully!!!!')
	else:
		messages.warning(request, 'Cannot book package. Package Already booked.')

	return redirect("my_booking")


def my_booking(request):
	uname = request.session.get('semail', None)
	reg=models.Reg.objects.get(emailid=uname)
	reg_id=reg.reg_id
	packages=models.Package.objects.raw("select * from package as p join booking as b on p.packgeid=b.fk_package_id join arts as a on p.fk_arts_id=a.artsid where b.fk_reg_id=%s",[reg_id])
	context={
	'plist':packages
	}
	return render(request,"student/my_packages.html",context)

def fees(request):
	uname = request.session.get('semail', None)
	reg=models.Reg.objects.get(emailid=uname)
	sid=reg.reg_id
	fees=models.Studentfee.objects.raw("select * from package p join arts a on p.fk_arts_id=a.artsid join booking b on p.packgeid=b.fk_package_id join studentfee s on s.fk_book_id=b.bookid where b.fk_reg_id=%s",[sid])
	context={
	'fe_list':fees
	}
	# return HttpResponse(sid)
	return render(request,"student/fees.html",context)

def pay_amount(request,bid):
	fees=models.Studentfee.objects.get(fk_book_id=bid)
	bookid=fees.fk_book_id
	amount=fees.amount
	context={
	'cost':amount,
	'bookid':bookid
	}
	return render(request,"student/pay_fees.html",context)

def videos(request):
	uname = request.session.get('semail', None)
	reg=models.Reg.objects.get(emailid=uname)
	reg_id=reg.reg_id
	videos=models.VideoTips.objects.raw("select * from video_tips v join package p on v.fk_arts_id=p.fk_arts_id join booking b on b.fk_package_id=p.packgeid where b.fk_reg_id=%s",[reg_id])
	context={
	'vi_list':videos
	}
	return render(request,"student/videos.html",context)

def student_transaction(request):
    user = request.session.get('semail', None)
    students = models.Reg.objects.filter(emailid=user)

    
    if students.exists():
        cardname = request.POST["cname"]
        cardNumber = request.POST["cardno"]
        expdate = request.POST["edate"]
        cvv = request.POST["cvv"]
        totalamount = float(request.POST["amt"])
        bid=request.POST['bid']
        

        # Use get() instead of raw SQL query to retrieve bank_data
        try:
            bank_data = models.Bank.objects.get(name=cardname,card_number=cardNumber,expiry=expdate,cvv=cvv)
        except models.Bank.DoesNotExist:
            messages.error(request, 'Invalid Card')
            return redirect("transactions")

        if totalamount <= bank_data.amount:
            fk_client_email = user
            paid_date = timezone.now().date()
            pay_amount = totalamount
            bookid=bid
            status='paid'
            payment = models.Studentfee.objects.get(fk_book_id=bookid)
            payment.status=status
            payment.pay_date=paid_date
            payment.save()
            messages.success(request, 'Payment successfully completed')
        else:
            messages.error(request, 'Insufficient Fund')
    else:
        messages.error(request, 'Invalid Client')

    return redirect("fees")
	

