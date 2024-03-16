"""
URL configuration for baroque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from barapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.display),
    path('pro1',views.profile1),
    path('pro2',views.profile2),
    path('pro3',views.profile3),
    path('log',views.back),
    path('login',views.log),
    path('user_reg',views.ureg),
    path('pro_reg',views.preg),
    path('waiting', views.loginwait),
    path('lout', views.logout),
    path('2', views.display2),
    path('reservation.html',views.display1),
    path('index.html#section_1',views.backhome),
    path('foodmenu',views.fmenu),
    path('drinksmenu',views.dmenu),
    path('reserve',views.book),
    path('pay',views.payment),
    path('loc',views.location),
    # path('#section_5',views.feedback),
    path('passchange',views.forgot),
    path('index',views.backhome),
    path('index1',views.backhome1),
    path('ufeed',views.userfeedback1),
    path('cfeed',views.feedback1),
    path('locbar', views.loc),
    path('forgot', views.change),
    path('find',views.addphnemail),



    # ADMIN SECTION - -------------------------------------------------------------

    # path('adash1',views.admindash1),
    path('adash',views.admindash),
    path('users',views.viewusers),
    path('providers',views.viewpros),
    path('promanage', views.promanage),
    path('deleting',views.delete),
    path('commonfeedback', views.commonfeed),
    path('userfeedback', views.userfeed),
    path('pdash',views.prodash),
    path('acceptingpro', views.proaccept),
    path('deletingpro', views.proreject),
    path('sendmessage', views.sendmessage),
    path('promessage', views.promessage),


    # PROVIDER SECTION -------------------------------------------------------------

    path('calen', views.calendar),
    path('userspro', views.viewuserspro),
    path('userfeedpro',views.usersfeedpro),
    path('dmenuedit',views.drinksedit),
    # path('dmenuedit',views.drinkseditr),
    # path('dmenuedit',views.drinkseditv),
    path('fmenuedit',views.foodsedit),
    # path('fmenuedit',views.foodseditveg),
    path('msg', views.admessage),
    path('bookingsview', views.bookview),
    path('dmenuview',views.drinkview),
    path('fmenuview',views.foodview),
    path('newdrinkswhis',views.newdrinkaddwhis),
    path('daddwhis',views.drinkaddwhis),
    path('newdrinksrum',views.newdrinkaddrum),
    path('daddrum', views.drinkaddrum),
    path('newdrinksvod',views.newdrinkaddvod),
    path('daddvod', views.drinkaddvod),
    path('newfoodsnon',views.newfoodaddnon),
    path('faddnon',views.foodaddnon),
    path('newfoodsveg',views.newfoodaddveg),
    path('faddveg', views.foodaddveg),
    path('deldrinkwhis',views.deletedrinkwhis),
    path('deldrinkrum',views.deletedrinkrum),
    path('deldrinkvod',views.deletedrinkvod),
    path('delfoodnon',views.deletefoodnon),
    path('delfoodveg',views.deletefoodveg),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)