from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from AppPortaria.models import Usuario, Veiculo, Movimento
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.views.generic.list import ListView


# Create your views here.
def home(request):
    return render(request,'index.html')

def loginPortaria(request):
    if request.method == "GET":
        return render(request,'login_portaria.html')
    
    else:
        cpfForm = request.POST.get('cpf-form')
        senha = request.POST.get('senha-form')
        
        user_exists = Usuario.objects.filter(cpf=cpfForm).exists()
        # auth.authenticate(request, cpf=cpfForm, senha=senha)
        user=None
        if  user_exists:
            user = auth.authenticate(request, username=cpfForm, password=senha)
            if  user is not None:
                login(request,  user_exists)
                #return HttpResponse('LOGADO')
                print('logado')
                #return redirect('') #aqui vc redireciona o usuario para a pagina.
            else:
                #return HttpResponse('USUARIO NAO EXISTE')
                print('nao existe else')



def portaria(request):
    return render( request,'portaria.html')






def registrar_portaria(request):
   if request.method == 'POST':
       try:
            placa = request.POST.get('placa')
            veiculo = Veiculo.objects.get(placa=placa)
            print(veiculo.id)
            if request.POST.get('km_entrada') == "":
                km_entrada=0
            else:
                km_entrada = request.POST.get('km_entrada')
            
            if request.POST.get('km_saida') == "":
                    km_saida=0
            else:
                km_saida = request.POST.get('km_saida')
                
                
            if request.POST.get('entrada') == "":
                entrada=0
            else:
                entrada = request.POST.get('entrada')
            
            if request.POST.get('saida') == "":
                    saida=0
            else:
                saida = request.POST.get('saida')
            
            objmovimento = Movimento.objects.create(veiculo=veiculo,km_entrada=km_entrada,km_saida=km_saida, entrada=entrada, saida=saida)
            return render( request,'Registrar.html')
       except ObjectDoesNotExist:
           return render( request,'Registrar.html',{"msg":"A placa não está cadastrada!"})
           
       
       
       
       
   
   return render(request,'Registrar.html',)

def registrosPortaria(request):
    movimentos = Movimento.objects.all()
    veiculos = Veiculo.objects.all()
    return render(request, 'registros_portaria.html', {'movimentos': movimentos, 'veiculos': veiculos})



def excluirPortaria(request):
    return render( request,'excluir_portaria.html')




def cadastrarVisitantes(request):
    if request.method == 'POST':
        try:
            print("cadastrei")
            placa = request.POST.get('placa')
            nome_condutor = request.POST.get('nome_condutor')
            cor_veiculo = request.POST.get('cor_veiculo')
            tipo_veiculo = request.POST.get('tipo_veiculo')
            modelo_veiculo = request.POST.get('modelo_veiculo')
            objveiculo = Veiculo(tipo=tipo_veiculo, cor=cor_veiculo, placa=placa, nome_do_condutor=nome_condutor, categoria="Visitante", modelo=modelo_veiculo, veiculo_institucional=False)
            objveiculo.save()
            
            dados = {"placa": placa, "veiculo_institucional": False}
            return render(request, 'Registrar.html', dados)
        except IntegrityError:
            return render(request, 'cadastrarvisitantes.html', {"msg":"A placa informada já está cadastrada!"})
        
    else:
        print("carreguei formulario")
        return render(request, 'cadastrarvisitantes.html')
      
    
    
    