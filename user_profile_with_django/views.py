from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def custom_page_not_found_view(request):
    return render(request, '404.html')
