from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, FormView
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm


class UserCreate(CreateView):
    model = User
    template_name = "regis.html"
    fields = ['first_name',
              'last_name',
              'email',
              'username',
              'password', ]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        return redirect("/login")


class UserLogin(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/list_image"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_success_url())
        else:
            return super(UserLogin, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(UserLogin, self).form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('/')
