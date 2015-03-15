from django.contrib import admin
from guestpub.models import Pub, Message


class PubAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone','show_pubimage', 'modified_at' )

    def show_pubimage(self, obj):
        return '<a href="%s"><img src="%s" width="200px"/></a>' % (obj.placeurl, obj.imageurl)

    show_pubimage.allow_tags = True

admin.site.register(Pub, PubAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('username', 'sender_tel', 'receiver_tel', 'result','message', 'created')

admin.site.register(Message, MessageAdmin)
