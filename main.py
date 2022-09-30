
import random
def CadastrarContato():
 while True:
    ID = random.randint(1000000,10000000)
    nome = input('Digite o nome de usuário:')
    email = input('Digite o email de usuário:')
    if('@'in email):
        print('Email validado com sucesso!')
    else:
        print('Cadastro cancelado pois o email não é valido')
        continue

    telefone = input('Digite o telefone de usuário:')
    try:
        agenda = open('agenda.txt','a')
        info = f'{ID}, {nome} ,{email},{telefone} \n'
        agenda.write(info)
        agenda.close()
        print('Contato cadastrado!')
        break
    except:
        print('Ocorreu um erro no cadastro')

def ProcurarContato():
   nome = input('Digite o nome do contato:').upper()
   agenda = open('agenda.txt','r')
   for contato in agenda:
    if nome in contato.split(";")[0].upper():
     print(contato)
   agenda.close()




def ListarContato():
    agenda = open('agenda.txt','r')
    for contato in agenda:
        print(contato)
    agenda.close()

def DeletarContato():
    deletado = input('Digite o usuário que deseja deletar:').lower()
    agenda = open('agenda.txt','r')
    aux = []
    aux2 = []
    for a in agenda:
        aux.append(a)
    for a in range(0,len(aux)):
     if deletado not in aux[a].lower():
        aux2.append(aux[a])
    agenda = open('agenda.txt','w')
    for a in aux2:
        agenda.write(a)
    print('O contato selecionado foi deletado!')




while True:
 print('=======Agenda Virtual=======')

 print('[1] Cadastrar um novo contato')
 print('[2] Procurar contato cadastrado ')
 print('[3] Listar os contatos')
 print('[4] Remover um contato')
 print('[5] Encerrar programa')
 print('===========================')

 opc = input('Qual das opções você deseja?')

 if(opc == '1'):
    CadastrarContato()
 elif(opc == '2'):
    ProcurarContato()
 elif(opc =='3'):
    ListarContato()
 elif(opc =='4'):
    DeletarContato()
 elif(opc == '5'):
  print('Encerrando agenda...')
  break

 else:
  print('Comando não reconhecido.')
  continue

