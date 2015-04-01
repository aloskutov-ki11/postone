# -*- coding: utf-8 -*-
from django.db import models
from adminsortable.models import Sortable
from django.dispatch import receiver
import os
from django.db.models.signals import pre_save, post_save, pre_delete
import datetime


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


class Document(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название документа", blank=True)
    description = models.TextField(verbose_name="Описание документа", blank=True)
    document = models.FileField(verbose_name="Документ")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class Resource(models.Model):
    url = models.CharField(max_length=256, verbose_name="Ссылка на ресурс")
    description = models.CharField(max_length=256, verbose_name="Описание ресурса", blank=True)

    def __str__(self):
        return self.url

    def __unicode__(self):
        return self.url

    class Meta:
        verbose_name = "Ресурс"
        verbose_name_plural = "Ресурсы"


#-------------------------------------------------------------------------------
class Reward(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название награды")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"


class GuardGroup(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название группы")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ('name', )


class GuardGroupScheduleItem(models.Model):
    title = models.CharField(max_length=256, verbose_name="Событие")
    time = models.TimeField(verbose_name="Время начала")
    group = models.ForeignKey(GuardGroup, verbose_name="Группа")

    def is_active(self):
        now = datetime.datetime.now().time()
        try:
            cur = GuardGroupScheduleItem.objects.filter(time__lte=now,
                                                    group=self.group).reverse()[0]
        except IndexError:
            # на случай между 00:00 и первым событием
            cur = GuardGroupScheduleItem.objects.filter(group=self.group)[0]
        return self == cur

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ('time', )


class Person(models.Model):
    fio = models.CharField(max_length=256, verbose_name="ФИО")
    school = models.CharField(max_length=256, verbose_name="Школа")
    photo = models.ImageField(verbose_name="Фотография", blank=True)
    rewards = models.ManyToManyField(Reward, verbose_name="Награды", blank=True, null=True)
    group = models.ForeignKey(GuardGroup, verbose_name="Группа", blank=True, null=True)

    def __str__(self):
        return self.fio

    def __unicode__(self):
        return self.fio

    class Meta:
        verbose_name = "Постовец"
        verbose_name_plural = "Постовцы"




@receiver(pre_save, sender=Document)
def set_document_name(sender, instance, **kwargs):
    if not instance.name:
         instance.name = os.path.basename(instance.document.name)