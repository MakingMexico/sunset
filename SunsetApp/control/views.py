from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(TemplateView):
    template_name = "index.html"


class HomeView(TemplateView):
    template_name = "home.html"

    @method_decorator(login_required(login_url="/"))
    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
