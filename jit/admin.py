from django.contrib import admin
from .models import Jit, Jit_Likedby
# Register your models here
# 
class JitAdmin(admin.ModelAdmin):
	list_display = ('id','date',)
	list_display_links = ('id','date')
	search_fields = ('id','date','value')
	list_per_page = 25

class JitLikeAdmin(admin.ModelAdmin):
	list_display = ('user_id_id','jit_id_id')

admin.site.register(Jit,JitAdmin)
admin.site.register(Jit_Likedby,JitLikeAdmin)
