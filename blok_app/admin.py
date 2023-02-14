from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Maqola)
class MaqolAdmin(admin.ModelAdmin):
  list_display=('sarlavha','sana','maqola','rasm')
  
@admin.register(Intert)
class InterAdmin(admin.ModelAdmin):
  list_display=('sarlavha','sana','vedio')