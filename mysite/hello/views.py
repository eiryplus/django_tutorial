from datetime import datetime

from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from . import forms, models


def hello_world(request):
    return HttpResponse('Hello World!')


def hello_template(request):
    d = {
        'hour': datetime.now().hour,
        'message': 'Sample message',
    }
    return render(request, 'hello/index.html', d)


def hello_if(request):
    d = {
        'is_visible': False,
        'empty_str': '',
    }
    return render(request, 'hello/if.html', d)


def hello_for(request):
    d = {
        'objects': range(10),
    }
    return render(request, 'hello/for.html', d)


def hello_get_query(request):
    d = {
        'your_name': request.GET.get('your_name')
    }
    return render(request, 'hello/get_query.html', d)


def hello_forms(request):
    form = forms.HelloForm(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    d = {
        'form': form,
        'message': message,
    }
    return render(request, 'hello/forms.html', d)


def hello_sample_forms(request):
    d = {
        'form': forms.SampleForm(),
    }
    return render(request, 'hello/form_samples.html', d)


def hello_models(request):
    form = forms.HelloForm(request.POST or None)
    if form.is_valid():
        models.Hello.objects.create(**form.cleaned_data)
        return redirect('hello:hello_models')
    d = {
        'form': form,
        'hello_qs': models.Hello.objects.all().order_by('-id')
    }
    return render(request, 'hello/models.html', d)
