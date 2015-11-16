from django.shortcuts import render
from forms import Registration , Login
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
# Create your views here.


def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username__iexact=form.cleaned_data['username'])
            except User.DoesNotExist:
                if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                    user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email']
                    )
                    return HttpResponseRedirect('success/')
                else:
                    form = Registration()
                    variables = RequestContext(request, {
                        'form': form
                        })
                    return render(request,
                        'register.html',
                        variables,
                    )
            form = Registration()
            variables = RequestContext(request, {
                'form': form
                })
            return render(request,
                'register.html',
                variables,
            )
    else:
        form = Registration()
        variables = RequestContext(request, {
            'form': form
            })
        return render(request,
            'register.html',
            variables,
        )

def register_success(request):
    return render(request,
        'success.html'
    )
    pass

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
        else:
            return HttpResponseRedirect('failed')
    else:
        form = Login()
        return render(request,
            'login.html',
            {'form': form});

def login_failed(request):
    return render(request,
        'failed.html'
    )
    pass
