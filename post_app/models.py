from django.db import models

# Create your models here.

from postone.settings import PHOTO_SIZE_BIG, PHOTO_SIZE_SMALL, UPLOAD_PHOTO_BIG_PATH, UPLOAD_PHOTO_SMALL_PATH
from PIL import Image
from django.core.files.storage import FileSystemStorage


class Slider(models.Model):
    title = models.TextField(verbose_name="Описание изображения")
    img = models.ImageField(storage=FileSystemStorage(location=UPLOAD_PHOTO_PATH), null=True)
    order = models.IntegerField(null=True, blank=True, verbose_name="Порядок в очереди")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
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


class NewsPhotos(models.Model):
    news = models.ForeignKey(News)
    photo_bg = models.ImageField(storage=FileSystemStorage(location=UPLOAD_PHOTO_BIG_PATH), null=True, verbose_name="Фотография")
    photo_sm = models.ImageField(storage=FileSystemStorage(location=UPLOAD_PHOTO_SMALL_PATH), null=True, verbose_name="Превью", blank=True)

    class Meta:
        verbose_name = "Фотография для новости"
        verbose_name_plural = "Фотографии для новостей"


class GalleryPhotos(models.Model):
    photo_bg = models.ImageField(storage=FileSystemStorage(location=UPLOAD_PHOTO_BIG_PATH), null=True, verbose_name="Фотография")
    photo_sm = models.ImageField(storage=FileSystemStorage(location=UPLOAD_PHOTO_SMALL_PATH), null=True, verbose_name="Превью", blank=True)

    class Meta:
        verbose_name = "Фотография для галереи"
        verbose_name_plural = "Фотографии для галереи"


class Translation(models.Model):
    video_url = models.TextField(max_length=255, verbose_name="YouTube-ссылка")

    def __str__(self):
        return self.video_id

    def __unicode__(self):
        return self.video_id


class Review(models.Model):
    author_name = models.CharField(max_length=256, verbose_name="Автор")
    pub_date = models.DateField(verbose_name="Дата публикации")
    content = models.TextField(verbose_name="Содержание")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать на сайте?")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"