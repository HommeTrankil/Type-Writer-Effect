from django.contrib import admin
from .models import typeWrite , txtStyle
# Register your models here.

class typeWriteAdmin(admin.ModelAdmin):

    list_display = ('title' , 'textStyle','pause')
    list_editable = ['textStyle','pause']



admin.site.register(typeWrite , typeWriteAdmin)

admin.site.register(txtStyle)



