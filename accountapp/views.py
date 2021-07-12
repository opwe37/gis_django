import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    hello_world_list = HelloWorld.objects.all()

    if request.method == 'POST':
        tmp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = tmp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

    return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})