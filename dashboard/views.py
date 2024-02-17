from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, View

# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'


class LoginView(TemplateView):
    template_name = 'login.html'
    # form_class = LoginForm
    success_url = reverse_lazy('dashboard:home')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        # del request.session['sytem']
        # logout(request)
        return redirect(reverse('dashboard:login'))
