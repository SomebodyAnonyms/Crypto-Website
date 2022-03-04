from django.shortcuts import render
from django.views.generic import ListView
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


# Create your views here.
class MainView(ListView):
    template_name = "Home/index.html"
    model = Body_Parts

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['List_News'] = List_News.objects.filter(status=True).order_by("position")
        context['List_News_Items'] = List_News.objects.filter(status=True).count()
        context['Header_Logo_Text'] = Header_Logo_Text.objects.filter(status=True)
        context['Header_Items_Left'] = Header_Items_Left.objects.filter(status=True).order_by("position")
        context['Header_Items_Right'] = Header_Items_Right.objects.filter(status=True).order_by("-position")
        context['Body_Parts'] = Body_Parts.objects.filter(status=True).order_by("position")
        context['Footer_Logo'] = Footer_Logo.objects.filter(status=True)
        context['Footer_Logo_Text'] = Footer_Logo_Text.objects.filter(status=True)
        context['Footer_Social_Icons'] = Footer_Social_Icons.objects.filter(status=True).order_by("position")
        context['Footer_Categories'] = Footer_Categories.objects.filter(status=True, parent__isnull=True).order_by("position")
        context['Footer_Description'] = Footer_Description.objects.filter(status=True)
        context['Footer_Copyright'] = Footer_Copyright.objects.filter(status=True)
        return context
