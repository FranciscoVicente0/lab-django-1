from django.shortcuts import render

def home_page_view(request):
    return render(request, 'website/home.html')

def sugestoes_page_view(request):
    return render(request, 'website/sugestoes.html')

def localizacoes_page_view(request):
    return render(request, 'website/localizacoes.html')