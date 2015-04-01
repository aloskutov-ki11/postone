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


class GuardGroupScheduleItemInline(admin.TabularInline):
    model = GuardGroupScheduleItem
    extra = 12

    fieldsets = [
        ('Событие', {'fields': ['title']}),
        ('Время начала', {'fields': ['time']}),
    ]


class GuardGroupAdminClass(admin.ModelAdmin):
    list_display = ('name',)

    fieldsets = [
        ('Название группы', {'fields': ['name']}),
    ]

    inlines = [GuardGroupScheduleItemInline]


admin.site.register(GalleryPhotos)
admin.site.register(News, NewsAdminClass)
admin.site.register(GuardGroup, GuardGroupAdminClass)
admin.site.register(Slider, SliderAdminClass)
admin.site.register(Translation)
admin.site.register(Review, ReviewAdminClass)

admin.site.register(Document)
admin.site.register(Resource)

admin.site.register(Person)
admin.site.register(Reward)

admin.site.unregister(User)
admin.site.unregister(Group)