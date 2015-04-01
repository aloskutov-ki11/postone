# -*- coding: utf-8 -*-
from django.contrib import admin
from post_app.models import *
from django.contrib.auth.models import Group, User
from adminsortable.admin import SortableAdmin


class PhotosNewsInline(admin.TabularInline):
    model = NewsPhotos
    extra = 3

    fieldsets = [
        ('Фотография', {'fields': ['image']}),
    ]


class NewsAdminClass(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']

    fieldsets = [
        ('Заголовок новости', {'fields': ['title']}),
        ('Дата публикации', {'fields': ['pub_date']}),
        ('Содержание', {'fields': ['content']}),
    ]

    inlines = [PhotosNewsInline]


class ReviewAdminClass(admin.ModelAdmin):
    list_display = ('author_name', 'pub_date', 'content')
    list_filter = ['pub_date']

    fieldsets = [
        ('Автор', {'fields': ['author_name']}),
        ('Дата публикации', {'fields': ['pub_date']}),
        ('Отзыв', {'fields': ['content']}),
    ]


class SliderAdminClass(SortableAdmin):
    list_display = ('title', 'image_small_preview', 'order')
    readonly_fields = ('image_big_preview',)


admin.site.register(GalleryPhotos)
admin.site.register(News, NewsAdminClass)
admin.site.register(Slider, SliderAdminClass)
admin.site.register(Translation)
admin.site.register(Review, ReviewAdminClass)

admin.site.unregister(User)
admin.site.unregister(Group)