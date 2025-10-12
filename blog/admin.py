from django.contrib import admin
from blog.models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title' ,'counted_views','status','published_date','created_date')
    list_filter = ['status', 'author']
    search_fields = ('title', 'content')


class CommentAdmin(admin.ModelAdmin):
        date_hierarchy = 'created_date'
        list_display = ('post' ,'subject','email','message','created_date')
        list_filter = ['approved', 'post']
        search_fields = ('name', 'post')


# Register your models here.
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)