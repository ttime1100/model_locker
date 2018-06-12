from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from . models import (
						Song, 
						SongInstance, 
						Artist, 
						Genre, 
						UserProfile, 
						Post, 
						ProfilePic, 
						PointOfInterest,
						Video,
					)
# Register your models here.
class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'position_map',)


    def position_map(self, instance):
        if instance.position is not None:
            return '<img src="http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s" width="%(width)s" height="%(height)s">' % {
                'latitude': instance.position.latitude,
                'longitude': instance.position.longitude,
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }
    position_map.allow_tags = True

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass





admin.site.register(Video, VideoAdmin)
admin.site.register(Song)
admin.site.register(SongInstance)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(PointOfInterest, PointOfInterestAdmin)
admin.site.register(ProfilePic)
