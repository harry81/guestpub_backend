from django.contrib import admin
from guestpub.models import Pub, Message, Comment



class CommentInline(admin.TabularInline):
    model = Comment


class PubAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_comment_number', 'phone','show_pubimage','created_at', 'modified_at' )
    inlines = [CommentInline, ]

    def show_pubimage(self, obj):
        return '<a href="%s"><img src="%s" width="200px"/></a>' % (obj.placeurl, obj.imageurl)

    def show_comment_number(self, obj):
        return '%d' % (obj.comment_set.all().count())

    show_pubimage.allow_tags = True

admin.site.register(Pub, PubAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('username', 'sender_tel', 'receiver_tel', 'result','message', 'created')

admin.site.register(Message, MessageAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pub',  'num_rate','msg', 'time')

admin.site.register(Comment, CommentAdmin)
