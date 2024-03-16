from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
from django.contrib import messages


# COMMON SECTION********************************************************************************************************

def display(request):
    return render(request,'common/index1.html')

def ureg(re):
    if re.method == 'POST':
        a = re.POST['a2']
        b = re.POST['a3']
        c = re.POST['a4']
        u = re.POST['a5']
        e = re.POST['a6']
        d = userreg.objects.create(name=a,email=b,phn_no=c,uname=u)
        d.save()
        d1 = login.objects.create(uname=u,pwd=e,status=1)
        d1.save()
        return render(re,"common/login.html")
    else:
        return render(re,'common/reg.html')

def preg(re):
    if re.method == 'POST':
        a = re.POST['a2']
        b = re.POST['a3']
        c = re.FILES['a4']
        u = re.POST['a5']
        e = re.POST['a6']
        f = re.POST['a7']
        g = re.POST['a8']
        h = re.POST['a9']
        d = proreg.objects.create(barname=a,email=b,license=c,uname=u,location=f,address=g,phone=h,action="p")
        d.save()
        d1 = login.objects.create(uname=u, pwd=e, status=2,action='pending')
        d1.save()
        messages.info(re, 'Please wait for the Approval & Check after sometime')
        return render(re,'common/wait.html')
    else:
        return render(re,'common/preg.html')

def loginwait(re):
    return render(re,'common/wait.html')


def profile1(re):
    if 'a_id' in re.session:
        return render(re,'admin/adminindex.html')
    else:
        return render(re,'common/login.html')

def profile2(re):
    if 'u_id' in re.session:
        y = re.session['u_id']
        d = userreg.objects.filter(uname=y)
        return render(re,'usermod/search.html', {'r': d})
    else:
        return render(re,'common/login.html')


def profile3(re):
    if 'p_id' in re.session:
        z = re.session['p_id']
        d = proreg.objects.filter(uname=z)
        return render(re,'providermod/proindex.html', {'r': d})
    else:
        return render(re,'common/login.html')


def log(re):
    if re.method == 'POST':
        u = re.POST['a5']
        p = re.POST['a6']
        try:
            d = login.objects.get(uname=u)
            if d.pwd == p:
                if d.status == '1':
                    re.session['u_id'] = u
                    return redirect(profile2)
                elif d.status == '2':
                    x = proreg.objects.get(uname=u)
                    if x.action=='Confirm':
                        re.session['p_id'] = u
                        return redirect(profile3)
                    else:
                        messages.info(re,'Please wait for the Approval & Check after sometime')
                        return render(re,'common/wait.html')
                else:
                    re.session['a_id'] = u
                    return redirect(profile1)
            else:
                return HttpResponse("incorrect password")
        except Exception:
            return HttpResponse("incoreect username")
    else:
        return render(re,'common/login.html')
def back(request):
    return render(request,'common/login.html')


def logout(re):
    if 'id' in re.session:
        re.session.flush()
        return render(re,'common/login.html')
    else:
        return render(re,'common/login.html')

def feedback1(re):
    if re.method == 'POST':
        a = re.POST['name']
        b = re.POST['email']
        c = re.POST['message']
        x = feedback.objects.create(name=a,email=b,message=c)
        x.save()
        return render(re,"common/index1.html")
    else:
        return render(re,'common/index1.html')

def forgot(re):
    return render(re, 'common/forgot.html')

def backhome1(re):
    return render(re, 'common/index1.html')

def change(re):
    if re.method == 'POST':
        x = re.POST['a5']
        y = re.POST['n3']
        z = re.POST['n4']
        try:
            d = login.objects.filter(uname=x)
            if y == z:
                d.update(pwd=y)
                return HttpResponse("<script>alert('Success');window.location='forgot'</script>")
            else:
                return HttpResponse("<script>alert('Try Again');window.location='forgot'</script>")
        except Exception:
            return HttpResponse("<script>alert('User Not Found');window.location='forgot'</script>")
    else:
        return render(re,'common/forgot.html')


# USER SECTION**********************************************************************************************************

def display2(request):
    return render(request,'usermod/index.html')
def display1(request):
    return render(request,'usermod/reservation.html')


def backhome(request):
    return render(request,'usermod/index.html')

def fmenu(re):
    return render(re,'usermod/foodmenu.html')

def dmenu(re):
    return render(re,'usermod/drinksmenu.html')

def book(re):
    if re.method == 'POST':
        a = re.POST['a1']
        b = re.POST['a2']
        c = re.POST['a3']
        d = re.POST['a4']
        e = re.POST['a5']
        f = re.POST['a6']
        x = tbooking.objects.create(name=a,phn_no=b,date=c,time=d,no_of_people=e,comments=f)
        x.save()
        return render(re,'usermod/payment.html')
    else:
        return render(re,'usermod/reservation.html')

def payment(re):
    return render(re,'usermod/payment.html')

def location(re):
    return render(re,'usermod/search.html')

def userfeedback1(re):
    if re.method == 'POST':
        a = re.POST['name']
        b = re.POST['email']
        c = re.POST['message']
        x = userfeedback.objects.create(name=a,email=b,message=c)
        x.save()
        return render(re,"usermod/index.html")
    else:
        return render(re,'usermod/index.html')

def backhome(re):
    return render(re,'usermod/index.html')

def feeds(re):
    return render(re,'usermod/index.html')

def loc(re):
    if re.method == 'POST':
        x = re.post['loc']
        d = proreg.objects.filter(location=x)
        return render(re, 'usermod/search.html', {'r': d})

def addphnemail(re):
    if re.method == 'POST':
        x = re.post['a8']
        y = re.post['a9']
        z = re.post['a3']                                                                    #  where to find us.......................
        d = proreg.objects.filter(address=x)
        d1 = proreg.objects.filter(phone=y,email=z)
        # d2 = proreg.objects.filter(email=z)
        return render(re,'usermod/index.html',{'r': d,'r1': d1})




# ADMIN SECTION ************************************************************************************************************


# def admindash1(re):
#     return render(re,'adminindex11.html')

def admindash(re):
    return render(re,'admin/adminindex.html')


def promanage(re):
    d = proreg.objects.filter(action="p")
    return render(re,'admin/promanage.html',{'r':d})

def delete(re):
    if re.method == 'POST':
        z= re.POST['name']
        d=proreg.objects.filter(uname=z)
        d1=login.objects.filter(uname=z)
        d.delete()
        d1.delete()
        return redirect(viewpros)
    else:
        return render(re, 'admin/providers.html')

def userfeed(re):
    d = userfeedback.objects.all()
    return render(re,'admin/userfeedback.html',{'r':d})

def commonfeed(re):
    d = feedback.objects.all()
    return render(re,'admin/commonfeedback.html',{'r':d})

def viewusers(re):
    d = userreg.objects.all()
    return render(re,'admin/users.html',{'r':d})

def viewpros(re):
    d = proreg.objects.filter(action='Confirm')
    return render(re,'admin/providers.html',{'r':d})

def sendmessage(re):
    if re.method == 'POST':
        # a = re.POST['puname']
        b = re.POST['message']
        x = adminmessage.objects.create( message=b)
        x.save()
        return redirect(promessage)
    else:
        return render(re, 'admin/message.html')

def promessage(re):
    d = proreg.objects.all()
    return render(re, 'admin/message.html', {'r': d})



def proaccept(request):     #accepting pro
    if request.method == "POST":
        r = request.POST['n1']
        d = proreg.objects.filter(uname=r)
        d.update(action="Confirm")
        # d1=login.objects.filter(id=r)
        # d1.update(action="Confirm")
        return HttpResponse("<script>alert('Accepted');window.location='promanage'</script>")
    else:
        return redirect(promanage)


def proreject(request):     #deleting pro request
    if request.method == "POST":
        r = request.POST['n1']
        d = proreg.objects.filter(uname=r)
        d.delete()
        d1=login.objects.filter(uname=r)
        d1.delete()
        return HttpResponse("<script>alert('Rejected');window.location='promanage'</script>")
    else:
        return redirect(promanage)



# PROVIDER SECTION  **************************************************************************************************

def prodash(re):
    return render(re,'providermod/proindex.html')

def calendar(re):
    return render(re,'providermod/calendar.html')

def viewuserspro(re):
    d = userreg.objects.all()
    return render(re,'providermod/pro_userview.html',{'r':d})

def usersfeedpro(re):
    d = userfeedback.objects.all()
    return render(re,'providermod/pro_userfeed.html',{'r':d})

def drinksedit(re):
    d = drinksaddwhis.objects.all()
    d1 = drinksaddrum.objects.all()
    d2 = drinksaddvod.objects.all()
    return render(re, 'providermod/drinksmenuedit.html',{'r':d,'r1':d1,'r2':d2})

# def drinkseditr(re):
#
#     return render(re, 'providermod/drinksmenuedit.html',{'r':d})
#
# def drinkseditv(re):
#
#     return render(re, 'providermod/drinksmenuedit.html',{'r':d})

def foodsedit(re):
    d = foodsaddnon.objects.all()
    d1 = foodsaddveg.objects.all()
    return render(re, 'providermod/foodmenuedit.html',{'r':d,'r1':d1})

# def foodseditveg(re):
#     d = foodsaddveg.objects.all()
#     return render(re, 'providermod/foodmenuedit.html',{'r':d})

def admessage(re):
    d = adminmessage.objects.all()
    return render(re, 'providermod/messages.html',{'r':d})

def bookview(re):
    d = tbooking.objects.all()
    return render(re, 'providermod/bookingsview.html',{'r':d})

def drinkview(re):
    return render(re, 'providermod/drinkmenuview.html')

def foodview(re):
    return render(re, 'providermod/foodmenuview.html')

def newdrinkaddwhis(re):
    if re.method == 'POST':
        a = re.POST['bname']
        b = re.POST['variant']
        c = re.POST['detail']
        d = re.FILES['image']
        x = drinksaddwhis.objects.create(brandname=a,variant=b,detail=c,image=d)
        x.save()
        return redirect(drinksedit)
    else:
        return render(re, 'providermod/drinksmenuedit.html')


def drinkaddwhis(re):
    return render(re, 'providermod/newdrinkw.html')

def newdrinkaddrum(re):
    if re.method == 'POST':
        a = re.POST['bname']
        b = re.POST['variant']
        c = re.POST['detail']
        d = re.FILES['image']
        x = drinksaddrum.objects.create(brandname=a,variant=b,detail=c,image=d)
        x.save()
        return redirect(drinksedit)
    else:
        return render(re, 'providermod/drinksmenuedit.html')


def drinkaddrum(re):
    return render(re, 'providermod/newdrinkr.html')

def newdrinkaddvod(re):
    if re.method == 'POST':
        a = re.POST['bname']
        b = re.POST['variant']
        c = re.POST['detail']
        d = re.FILES['image']
        x = drinksaddvod.objects.create(brandname=a,variant=b,detail=c,image=d)
        x.save()
        return redirect(drinksedit)
    else:
        return render(re, 'providermod/drinksmenuedit.html')


def drinkaddvod(re):
    return render(re, 'providermod/newdrinkv.html')


def newfoodaddnon(re):
    if re.method == 'POST':
        a = re.POST['fname']
        b = re.POST['price']
        c = re.POST['detail']
        x = foodsaddnon.objects.create(foodname=a,price=b,detail=c)
        x.save()
        return render(re, 'providermod/newfoodnon.html')
    else:
        return render(re, 'providermod/foodmenuedit.html')


def foodaddnon(re):
    return render(re, 'providermod/newfoodnon.html')

def newfoodaddveg(re):
    if re.method == 'POST':
        a = re.POST['fname']
        b = re.POST['price']
        c = re.POST['detail']
        x = foodsaddveg.objects.create(foodname=a,price=b,detail=c)
        x.save()
        return render(re, 'providermod/newfoodveg.html')
    else:
        return render(re, 'providermod/foodmenuedit.html')

def foodaddveg(re):
    return render(re, 'providermod/newfoodveg.html')

def deletefoodnon(re):
    if re.method == 'POST':
        z= re.POST['fname']
        d= foodsaddnon.objects.filter(foodname=z)
        d.delete()
        return redirect(foodsedit)

def deletefoodveg(re):
    if re.method == 'POST':
        z = re.POST['fname']
        d = foodsaddveg.objects.filter(foodname=z)
        d.delete()
        return redirect(foodsedit)

def deletedrinkwhis(re):
    if re.method == 'POST':
        z = re.POST['bname']
        d = drinksaddwhis.objects.filter(brandname=z)
        d.delete()
        return redirect(drinksedit)

def deletedrinkrum(re):
    if re.method == 'POST':
        z = re.POST['bname']
        d = drinksaddrum.objects.filter(brandname=z)
        d.delete()
        return redirect(drinksedit)

def deletedrinkvod(re):
    if re.method == 'POST':
        z = re.POST['bname']
        print(z)
        d = drinksaddvod.objects.filter(brandname=z)
        d.delete()
        return redirect(drinksedit)




