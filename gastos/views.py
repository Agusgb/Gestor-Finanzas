from django.shortcuts import render

def index(request):
    return render(request, 'gastos/index.html')

def add_gastos(request):
    return render(request, 'gastos/add_gasto.html')

