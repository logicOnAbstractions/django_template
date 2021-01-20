from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


class LoginView(generic.View):
    template_name = 'myapp/login.html'
    redirect_field_name = 'listview'

    def get(self, request):                                                 # GET - return the form for login
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):                                                # POST - we're receiving data from the page, validate it.
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user    = authenticate(request ,username=username, password=password)
        if user:        # auth succeeded, proceed
            login(request,user)
            return HttpResponseRedirect('/listview')
        else:
            context = {'form':form}
            return render(request, self.template_name, context)


class IndexView(LoginRequiredMixin ,generic.View):
    template_name = 'myapp/index.html'
    context_object_name = 'dummy'
    login_url = 'login/'

    def get(self, request):
        return render(request, self.template_name)


class DummyIndexView(generic.View):
    template_name = 'myapp/index.html'
    def get(self, request):
        return render(request, self.template_name)


class MyListView(generic.ListView):
    template_name = 'myapp/mylistview.html'
    model = MyObjects
    context_object_name = 'objects'


class ListElementView(generic.DetailView):
    model = MyObjects
    template_name = 'myapp/list_element.html'

class ObjectCreate(generic.CreateView):
    template_name = 'myapp/createlistelement.html'
    model = MyObjects
    fields = ["name"]

    def get_success_url(self):
        return reverse('myapp:mylistview')

