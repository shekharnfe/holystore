from django.contrib import admin
from picproject.models import picproj,Category,Customer,Product,Order,Profile,contactus
from django.contrib.auth.models import User
#from django.conf.locale.es import formats as es_formats

#es_formats.DATETIME_FORMAT = "d M Y H:i:s"

class picadmin(admin.ModelAdmin):
    pic_display=('pic_image')

admin.site.register(picproj,picadmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)
admin.site.register(contactus)
# Register your models here.

# mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile
# Extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username","first_name","last_name","email"] 
    inlines = [ProfileInline] 
#Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User , UserAdmin)