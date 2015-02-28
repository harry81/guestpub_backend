from django.contrib import admin
from guestpub.models import Pub


class PubAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone','show_pubimage','created_at', 'modified_at' )

    def show_pubimage(self, obj):
        return '<a href="%s"><img src="%s" width="200px"/></a>' % (obj.placeUrl, obj.imageUrl)

    show_pubimage.allow_tags = True

admin.site.register(Pub, PubAdmin)


