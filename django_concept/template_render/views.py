from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        "name": "Sushanta Patra",
        "age": 31,
        "email": "sushanta@gmail.com"
    }
    return render(request, 'index.html', context)
