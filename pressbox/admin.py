from django.contrib import admin
from pressbox.models import PressItem, PressImage, PressCategory
from pressbox.forms import PressItemForm

class PressImageInline(admin.StackedInline):
    extra = 2
    max_num = 8
    model = PressImage


class PressItemAdmin(admin.ModelAdmin):
    model = PressItem    
    form = PressItemForm
    prepopulated_fields = {'slug':("title",),}
    
    search_fields = ('title',)
    list_display = ('title', 'published_on','is_active')
    inlines = [
      PressImageInline
    ]

class PressCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("title",),}

admin.site.register(PressItem, PressItemAdmin)
admin.site.register(PressImage)
admin.site.register(PressCategory, PressCategoryAdmin)