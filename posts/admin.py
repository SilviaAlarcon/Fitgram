from django.contrib import admin
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('pk', 'title', 'created', 'modified')
    list_display_links=('pk', 'created')
    list_editable= ('title',)
    search_fields = (
        'created',
        'modified'
    )
    list_filter = (
        'title',
        'created'
    )

    #Evitar que ciertos campos sean editables
    readonly_fields = ('created', 'modified')
