from django.shortcuts import render

def index(request):
    return render(request, 'gastos/index.html')

def add_gastos(request):
    return render(request, 'gastos/add_gasto.html')

def test_view(request):
    return render(request, 'test.html')
