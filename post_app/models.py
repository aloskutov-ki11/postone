# -*- coding: utf-8 -*-
from django.db import models
from adminsortable.models import Sortable


class Slider(Sortable):
    title = models.TextField(verbose_name="Описание изображения")
    image = models.ImageField(verbose_name="Изображение", null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def image_small_preview(self):
        return u'<img src="{}" width="100"/>'.format(
            self.image.url)

    image_small_preview.short_description = u'Изображение'
    image_small_preview.allow_tags = True

    def image_big_preview(self):
        return u'<img src="{}" width="400"/>'.format(
            self.image.url)

    image_big_preview.short_description = u'Просмотр'
    image_big_preview.allow_tags = True

    class Meta(Sortable.Meta):
        verbose_name = "Изображение для слайдера"
        verbose_name_plural = "Изображения для слайдера"


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name="Заголовок новости")
    pub_date = models.DateField(verbose_name="Дата публикации")
    content = models.TextField(verbose_name="Содержание новости")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-pub_date']


class NewsPhotos(models.Model):
    news = models.ForeignKey(News)
    image = models.ImageField(verbose_name="Фотография", null=True)

    class Meta:
        verbose_name = "Фотография для новости"
        verbose_name_plural = "Фотографии для новостей"


class GalleryPhotos(models.Model):
    image = models.ImageField(verbose_name="Фотография", null=True)

    class Meta:
        verbose_name = "Фотография для галереи"
        verbose_name_plural = "Фотографии для галереи"


class Translation(models.Model):
    video_url = models.CharField(max_length=255, verbose_name="YouTube-ссылка")

    def __str__(self):
        return self.video_url

    def __unicode__(self):
        return self.video_url

    class Meta:
        verbose_name = "YouTube-ссылка"
        verbose_name_plural = "YouTube-ссылки"


class Review(models.Model):
    author_name = models.CharField(max_length=256, verbose_name="Автор")
    pub_date = models.DateField(verbose_name="Дата публикации")
    content = models.TextField(verbose_name="Содержание")

    def __str__(self):
        return self.author_name

    def __unicode__(self):
        return self.author_name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"