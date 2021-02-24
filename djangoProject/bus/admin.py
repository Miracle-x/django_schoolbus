from django.contrib import admin

# Register your models here.
from bus.models import Wxuserinfo,Schoolbusinfo,UserQue,Usercontact


class WxuserinfoAdmin(admin.ModelAdmin):
    list_display = ('userid','credit')  # list
    search_fields = ('userid',)

class UserQueAdmin(admin.ModelAdmin):
    list_display = ('schoolbus_id','user_id','quenumber','state')  # list
    search_fields = ('schoolbus_id','user_id',)

class SchoolbusinfoAdmin(admin.ModelAdmin):
    list_display = ('schoolbus_id', 'start_time', 'end_time', 'departure_time', 'isopened', 'capacity', 'campus')
    search_fields = ('schoolbus_id',)

admin.site.register(Wxuserinfo,WxuserinfoAdmin)
admin.site.register(UserQue,UserQueAdmin)
admin.site.register(Schoolbusinfo,SchoolbusinfoAdmin)
admin.site.register([Usercontact])