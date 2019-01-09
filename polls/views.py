from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Blog

class IndexView(TemplateView):
    template_name = 'polls/base.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        posts = Blog.objects.all()

        ctx['posts'] = posts

        return ctx