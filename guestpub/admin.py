from django.contrib import admin
from guestpub.models import Pub, Message, Review



class ReviewInline(admin.TabularInline):
    model = Review


class PubAdmin(admin.ModelAdmin):
    list_display = ('title', 'show_review_number', 'phone','show_pubimage','created_at', 'modified_at' )
    inlines = [ReviewInline, ]

    def show_pubimage(self, obj):
        return '<a href="%s"><img src="%s" width="200px"/></a>' % (obj.placeurl, obj.imageurl)

    def show_review_number(self, obj):
        return '%d' % (obj.review_set.all().count())

    show_pubimage.allow_tags = True

admin.site.register(Pub, PubAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('username', 'sender_tel', 'receiver_tel', 'result','message')

admin.site.register(Message, MessageAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pub',  'num_rate','msg', 'time')

admin.site.register(Review, ReviewAdmin)
