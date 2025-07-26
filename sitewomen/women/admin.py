from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from .models import Women, Category, TagPost


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Незамужем')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        return queryset.filter(husband__isnull=True)
    

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'photos', "post_photo", 'content', 'cat', 'husband', 'tags', )
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = ("post_photo", )
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat', )
    list_display_links = ('title', )
    ordering = ('time_create', 'title', )
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ('set_published', 'set_draft', )
    search_fields = ('title', 'cat__name', )
    list_filter = (MarriedFilter, 'cat__name', 'is_published', )
    filter_horizontal = ('tags', )
    filter_vertical = ('tags', )
    save_on_top = True

    @admin.display(description='Изображение', ordering='content')
    def post_photo(self, women: Women):
        if women.photos:
            return mark_safe(f'<img src="{women.photos.url}" width=50')
        return "Без фото"

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей', messages.SUCCESS)

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, qeuryset):
        count = qeuryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'Снято с публикации {count} записей', messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ("tag", "slug")