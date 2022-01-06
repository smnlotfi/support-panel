from django.contrib import admin
from .models import user_voipecode

# Register your models here.
class voipeadmin(admin.ModelAdmin):
    list_display=('id','voipe_code')

admin.site.register(user_voipecode)
