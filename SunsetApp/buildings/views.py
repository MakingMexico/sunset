from django.shortcuts import render
from buildings.models import *
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class CreateBuilding(CreateView):
    model = Building
    template_name = "building_form.html"
    fields = ['name',
              'image',
              'description',
              'city', ]

    success_url = '/'

    @method_decorator(login_required(login_url="/"))
    def dispatch(self, *args, **kwargs):
        return super(CreateBuilding, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        user_django = User.objects.get(id=self.request.user.id)
        form.instance.owner = user_django
        return super(CreateImage, self).form_valid(form)
