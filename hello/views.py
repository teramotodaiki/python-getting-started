from django.shortcuts import render
from django.http import HttpResponse
from .hiraganize import hiraganize

from .models import Greeting

# Create your views here.
def index(request):
    print("index")
    # return HttpResponse('Hello from Python!')
    query = request.GET.get("q", "飛沫")
    yomi = hiraganize(query)
    print(query, yomi)

    return render(request, "index.html", {"query": query, "yomi": yomi})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
