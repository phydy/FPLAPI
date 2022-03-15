from django.contrib import admin

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('d_created', 'title', 'subject')
    list_display_links = ('d_created', 'title', 'subject')
    list_filter = ('d_created', 'title', 'subject')
    search_fields = ('d_created', 'title', 'subject') 
    fields = (
        'title',
        'subject',
        'body'
    )

admin.site.site_header = 'Site Admin'

# Register your models here.
