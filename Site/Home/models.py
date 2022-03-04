from django.db import models
from django.utils.html import format_html
from django.template.defaultfilters import truncatechars


# Managers
class Footer_Categories_Manager(models.Manager):
    def enable_childs(self):
        return self.filter(status=True)


# Create your models here.
class List_News(models.Model):
    position = models.IntegerField(verbose_name="Position:")
    image = models.ImageField(
        upload_to="images/List_News", verbose_name="Image")
    title = models.TextField(max_length=5000, verbose_name="Title:")
    text = models.TextField(max_length=5000, verbose_name="Description:")
    slug = models.SlugField(max_length=5000, unique=True, verbose_name="Slug:")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "List News"
        verbose_name_plural = "List News"

    def image_html_format(self):
        return format_html(f"<img width=50; height=50; style='border-radius: 5px;' src='{self.image.url}'>")
    image_html_format.short_description = "Image"

    def short_title(self):
        return truncatechars(self.title, 100)
    
    def short_text(self):
        return truncatechars(self.text, 100)




class Header_Logo_Text(models.Model):
    part_one = models.CharField(max_length=5000, verbose_name="Part One:")
    part_two = models.CharField(max_length=5000, verbose_name="Part Two:")
    slug = models.CharField(max_length=5000, unique=True, verbose_name="Slug:")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "Header Logo Text"
        verbose_name_plural = "Header Logo Texts"

    def __str__(self):
        return self.part_one


class Header_Items_Left(models.Model):
    position = models.IntegerField(verbose_name="Position:")
    title = models.CharField(max_length=5000, verbose_name="Title:")
    slug = models.CharField(max_length=5000, unique=True, verbose_name="Slug:")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "Header Item Left"
        verbose_name_plural = "Header Items Left"

    def __str__(self):
        return self.title


class Header_Items_Right(models.Model):
    position = models.IntegerField(verbose_name="Position:")
    title = models.CharField(max_length=5000, verbose_name="Title:")
    slug = models.CharField(max_length=5000, unique=True, verbose_name="Slug:")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "Header Item Right"
        verbose_name_plural = "Header Items Right"

    def __str__(self):
        return self.title


class Body_Parts(models.Model):
    position = models.IntegerField(verbose_name="Position:")
    image = models.ImageField(
        upload_to="images/Body_Parts", verbose_name="Image")
    title = models.CharField(max_length=5000, verbose_name="Title:")
    text = models.TextField(max_length=5000, verbose_name="Description:")
    button = models.CharField(max_length=5000, verbose_name="Button Text:")
    slug = models.SlugField(max_length=5000, unique=True, verbose_name="Slug:")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "Body Part"
        verbose_name_plural = "Body Parts"

    def image_html_format(self):
        return format_html(f"<img width=50; height=50; style='border-radius: 5px;' src='{self.image.url}'>")
    image_html_format.short_description = "Image"

    def short_text(self):
        return truncatechars(self.text, 100)


class Footer_Logo(models.Model):
    image = models.ImageField(
        upload_to="images/Footer_Logo", verbose_name="Image")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "Footer Logo"
        verbose_name_plural = "Footer Logos"

    def image_html_format(self):
        return format_html(f"<img width=50; height=50; style='border-radius: 5px;' src='{self.image.url}'>")
    image_html_format.short_description = "Image"


class Footer_Logo_Text(models.Model):
    text = models.TextField(max_length=5000, verbose_name="Text:")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "Footer Logo Text"
        verbose_name_plural = "Footer Logo Texts"

    def __str__(self):
        return self.text


class Footer_Social_Icons(models.Model):
    position = models.IntegerField(verbose_name="Position:")
    name = models.CharField(max_length=5000, verbose_name="Name:")
    link = models.CharField(max_length=5000, verbose_name="Page Link:")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "Footer Social Icon"
        verbose_name_plural = "Footer Social Icons"

    def __str__(self):
        return self.name


class Footer_Categories(models.Model):
    position = models.IntegerField(verbose_name="Position:")
    parent = models.ForeignKey('self', blank=True, on_delete=models.SET_NULL, null=True, related_name='children', verbose_name="Parent:")
    title = models.CharField(max_length=5000, verbose_name="Title:")
    slug = models.SlugField(max_length=5000, unique=True, verbose_name="Slug:")
    status = models.BooleanField(default=True, verbose_name="Enable")

    class Meta:
        verbose_name = "Footer Category"
        verbose_name_plural = "Footer Categories"

    def __str__(self):
        return self.title

    objects = Footer_Categories_Manager()


class Footer_Description(models.Model):
    text = models.TextField(max_length=5000, verbose_name="Description:")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "Footer Description"
        verbose_name_plural = "Footer Descriptions"

    def __str__(self):
        return self.text
    
    def short_text(self):
        return truncatechars(self.text, 100)


class Footer_Copyright(models.Model):
    text = models.TextField(max_length=5000, verbose_name="Copyright:")
    status = models.BooleanField(default=False, verbose_name="Enable")

    class Meta:
        verbose_name = "Footer Copyright"
        verbose_name_plural = "Footer Copyrights"

    def __str__(self):
        return self.text
