from django.contrib import admin

# Register your models here.
from.models import login
admin.site.register(login)
from.models import userreg
admin.site.register(userreg)
from.models import proreg
admin.site.register(proreg)
from.models import tbooking
admin.site.register(tbooking)
from.models import feedback
admin.site.register(feedback)
from.models import userfeedback
admin.site.register(userfeedback)
from.models import drinksaddwhis
admin.site.register(drinksaddwhis)
from.models import drinksaddrum
admin.site.register(drinksaddrum)
from.models import drinksaddvod
admin.site.register(drinksaddvod)
from.models import foodsaddnon
admin.site.register(foodsaddnon)
from.models import foodsaddveg
admin.site.register(foodsaddveg)
from.models import adminmessage
admin.site.register(adminmessage)