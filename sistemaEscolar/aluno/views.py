from django.shortcuts import render


# Create your views here.
def resposta(request):

    return render (request, 'paginas/main.html')