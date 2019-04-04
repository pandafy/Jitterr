from django.contrib import admin

# Register your models here.
from .models import FrontendUsers

class FrontendUsersAdmin(admin.ModelAdmin):
	list_display = ('id','username',)
	list_display_links = ('id','username')
	search_fields = ('id','username','bio')
	list_per_page = 25

admin.site.register(FrontendUsers,FrontendUsersAdmin)