from django.shortcuts import render


def index(request):
    """homepage"""

    return render(request, 'index.html')
