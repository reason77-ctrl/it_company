from django.contrib import admin
from tinymce.widgets import TinyMCE

from .models import *
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display=['title','img','date_time']
    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }
admin.site.register(Service,ServiceAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name','email','date_time']
    list_display_links = ['full_name','email']
admin.site.register(Contact,ContactAdmin)

class SliderAdmin(admin.ModelAdmin):
    list_display = ['name','img','status','date_time']
admin.site.register(Slider,SliderAdmin)


class TechsAdmin(admin.ModelAdmin):
    list_display = ['name','logo_img','date_time']
admin.site.register(Techs,TechsAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title','date_time']
    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }
admin.site.register(About,AboutAdmin)


class Connect_FormAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','date_time']

admin.site.register(Connect_Form,Connect_FormAdmin)