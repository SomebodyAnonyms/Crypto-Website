from django.contrib import admin
from .models import (
    List_News,
    Header_Logo_Text,
    Header_Items_Left,
    Header_Items_Right,
    Body_Parts,
    Footer_Logo,
    Footer_Logo_Text,
    Footer_Social_Icons,
    Footer_Categories,
    Footer_Description,
    Footer_Copyright,
)


# Register your models here.
# List_News
class List_News_Admin(admin.ModelAdmin):
    list_display = ["position", "image_html_format", "short_title", "short_text", "slug", "status"]
    list_filter = ["status"]
    search_fields = ["position", "title", "text", "slug"]
    ordering = ["-status"]


admin.site.register(List_News, List_News_Admin)


# Header_Logo_Text
class Header_Logo_Text_Admin(admin.ModelAdmin):
    list_display = ["part_one", "part_two", "slug", "status"]
    list_filter = ["status"]
    search_fields = ["part_one", "part_two", "slug"]
    ordering = ["-status"]


admin.site.register(Header_Logo_Text, Header_Logo_Text_Admin)


# Header_Items_Left
class Header_Items_Left_Admin(admin.ModelAdmin):
    list_display = ["position", "title", "slug", "status"]
    list_filter = ["status"]
    search_fields = ["position", "title", "slug"]
    ordering = ["-status", "position"]


admin.site.register(Header_Items_Left, Header_Items_Left_Admin)


# Header_Items_Right
class Header_Items_Right_Admin(admin.ModelAdmin):
    list_display = ["position", "title", "slug", "status"]
    list_filter = ["status"]
    search_fields = ["position", "title", "slug"]
    ordering = ["-status", "position"]


admin.site.register(Header_Items_Right, Header_Items_Right_Admin)


# Body_Parts
class Body_Parts_Admin(admin.ModelAdmin):
    list_display = ["position", "image_html_format", "title", "short_text", "button", "slug", "status"]
    list_filter = ["status"]
    search_fields = ["position", "title", "text", "button", "slug"]
    ordering = ["-status", "position"]


admin.site.register(Body_Parts, Body_Parts_Admin)


# Footer_Logo
class Footer_Logo_Admin(admin.ModelAdmin):
    list_display = ["image_html_format", "status"]
    list_filter = ["status"]
    ordering = ["-status"]


admin.site.register(Footer_Logo, Footer_Logo_Admin)


# Footer_Logo_Text
class Footer_Logo_Text_Admin(admin.ModelAdmin):
    list_display = ["text", "status"]
    list_filter = ["status"]
    search_fields = ["text"]
    ordering = ["-status"]


admin.site.register(Footer_Logo_Text, Footer_Logo_Text_Admin)


# Footer_Social_Icons
class Footer_Social_Icons_Admin(admin.ModelAdmin):
    list_display = ["position", "name", "link", "status"]
    list_filter = ["status"]
    search_fields = ["position", "name", "link"]
    ordering = ["-status", "position"]


admin.site.register(Footer_Social_Icons, Footer_Social_Icons_Admin)


# Footer_Categories
class Footer_Categories_Admin(admin.ModelAdmin):
    list_display = ["position", "title", "parent", "slug", "status"]
    list_filter = ["status", "parent"]
    search_fields = ["position", "title", "slug"]
    ordering = ["-status", "-parent", "position"]


admin.site.register(Footer_Categories, Footer_Categories_Admin)


# Footer_Description
class Footer_Description_Admin(admin.ModelAdmin):
    list_display = ["short_text", "status"]
    list_filter = ["status"]
    search_fields = ["text"]
    ordering = ["-status"]


admin.site.register(Footer_Description, Footer_Description_Admin)


# Footer_Copyright
class Footer_Copyright_Admin(admin.ModelAdmin):
    list_display = ["text", "status"]
    list_filter = ["status"]
    search_fields = ["text"]
    ordering = ["-status"]


admin.site.register(Footer_Copyright, Footer_Copyright_Admin)
