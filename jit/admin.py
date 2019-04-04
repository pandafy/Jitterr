from django.contrib import admin
from .models import Jit
# Register your models here
# 
class JitAdmin(admin.ModelAdmin):
	list_display = ('id','date',)
	list_display_links = ('id','date')
	search_fields = ('id','date','value')
	list_per_page = 25

admin.site.register(Jit,JitAdmin)
