from django.shortcuts import render

# Create your views here.
def loginCSL(request):
    return render(request,'login_csl.html')

def CSL(request):
    return render(request,'CSL.html')

def cadastrarveiculos(request):
    return render(request,'cadastro_de_veiculos.html')

def cadastrousuarios(request):
    return render(request,'cadastra_de_usuario.html')

def autorizarveiculos(request):
    return render(request,'autorização_de_veículos.html')

def registros(request):
    return render(request,'registros_CSL.html')

def excluircsl(request):
    return render(request,'excluir_CSL.html')