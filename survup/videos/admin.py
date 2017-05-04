from django.contrib import admin

from .models import Video



class VideoAdmin(admin.ModelAdmin):
	list_filter = ['updated', 'timestamp']
	list_display = ['title', 'updated', 'timestamp']
	search_fields = ['title', 'embed_code']
	readonly_fields = ['updated', 'timestamp', 'short_title']
	class Meta:
			model = Video 

	def short_title(self, obj):
	    return obj.title[:3]		

admin.site.register(Video, VideoAdmin)
