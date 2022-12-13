from django.contrib import admin
from applications.posts.models import Category, Image, Post, Comment, Rating, Like

class ImageAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 10

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin
    ]
    list_display = ['id', 'title', 'post_count_like']
    
    def post_count_like(self, obj):
        return obj.likes.filter(like=True).count()

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Image)