from django.contrib import admin
from appname.models import I

class IAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_date', 'price')
    list_filter = ('author', 'publisher')
    search_fields = ('title',)
    ordering = ('publication_date',)

admin.site.register(I, IAdmin)
