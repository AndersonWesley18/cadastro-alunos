import os

class Aluno:
    def __init__(self, nome, nascimento, idade, nome_pai, nome_mae, endereco, bairro, cidade, estado, pais):
        self.nome=nome
        self.nascimento=nascimento
        self.idade = idade
        self.nome_pai = nome_pai
        self.nome_mae = nome_mae
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais  
    def from_line(self, line):
        dados=line.split(",")
        self.nome = dados[0]
        self.nascimento=dados[1]
        self.idade = dados[2]
        self.nome_pai = dados[3]
        self.nome_mae = dados[4]
        self.endereco = dados[5]
        self.bairro = dados[6]
        self.cidade = dados[7]
        self.estado = dados[8]
        self.pais = dados[9]      
    def to_string(self):
        return ",".join([self.nome, self.nascimento, self.idade, self.nome_pai, self.nome_mae, self.endereco, self.bairro, self.cidade, self.estado, self.pais,"\n"])
    def to_json(self):
        return ("\n\"aluno\":{\n  \"nome\":\""+self.nome+"\""+
        "\n  \"nascimento\":\""+self.nascimento+"\""+
        "\n  \"idade\":\""+self.idade+"\""+
        "\n  \"nome_pai\":\""+self.nome_pai+"\""+
        "\n  \"nome_mae\":\""+self.nome_mae+"\""+
        "\n  \"endereco\":\""+self.endereco+"\""+
        "\n  \"bairro\":\""+self.bairro+"\""+
        "\n  \"cidade\":\""+self.cidade+"\""+
        "\n  \"estado\":\""+self.estado+"\""+
        "\n  \"pais\":\""+self.pais+"\""+
        "\n},")    
        
aluno=Aluno("","","","","","","","","","")
path_cadastro=os.getcwd()+"/cadastro-alunos.txt"
path_json=os.getcwd()+"/json.txt"

def mostar_bv():
    print("-"*30+"\nBem-vindo\nSistema de cadastro de alunos\n"+"-"*30)

def mostrar_menu():
    print("-"*10+"\nMenu\n"+"-"*10+
    "\n1- Cadastrar aluno"+
    "\n2- Exclusão de cadastro"+
    "\n3- Imprimir lista"+
    "\n4- Exportar para arquivo(JSON)"+
    "\n5- Encerrar sistema\n"
    )

def cadastrar_aluno():
    aluno.nome=input('Qual o nome do aluno? > ') 
    aluno.nascimento=input('Qual a data de nascimento do aluno? > ')
    aluno.idade =input('Qual a idade do aluno? > ')
    aluno.nome_pai =input('Qual o nome do pai do aluno? > ')
    aluno.nome_mae =input('Qual o nome da mãe do aluno? > ')
    aluno.endereco =input('Qual o endereço do aluno? > ')
    aluno.bairro =input('Qual o bairro do aluno? > ')
    aluno.cidade =input('Qual a cidade do aluno? > ')
    aluno.estado =input('Qual o estado do aluno? > ')
    aluno.pais =input('Qual o pais do aluno? > ')
    print('\nSalvando novo aluno\n')
    if not os.path.exists(path_cadastro):
        with open(path_cadastro, 'w'): pass
    f =open(path_cadastro,"r+")
    f.readlines()
    f.write(aluno.to_string())
    f.close
    print('\nAluno cadastrado com sucesso!!!\n')

def deletar_aluno():
    nome=(input("Quem você quer remover? > "))
    with open(path_cadastro,"r") as f:
        lines = f.readlines()
        with open(path_cadastro, "w") as f:
            for line in lines:
                if line.strip("\n").split(",",1)[0] != nome:
                    f.write(line)
        f.close()            
       
    print('\nDeletando aluno\n')



def imprimir_lista():
    print('\nImprimindo lista de alunos\n')
    try:
        lista_alunos=[]
        f =open(path_cadastro,"r")
        for l in f.readlines():
            a=Aluno("","","","","","","","","","")
            a.from_line(l)
            lista_alunos.append(a)    
        f.close()
        for a in sorted(lista_alunos, key=lambda aluno: aluno.nome):
            print(a.to_string())
    except Exception as ex:
        print('Ocorreu um erro > ' + str(ex))

def exportar_json():
    f=open(path_cadastro,"r")
    json=open(path_json,"w")
    json.write("{[")
    for l in f.readlines():
        aluno.from_line(l)
        json.write(aluno.to_json())
    json.write("\n]}")
    json.close()
    f.close()    

    print('Exportando\n')


def __init__():
    mostar_bv()
    while(True):
        mostrar_menu()
        try:
            opcao=int(input("Escolha uma opção > "))
            if(opcao==1):
                cadastrar_aluno()
            elif(opcao==2):
                deletar_aluno()
            elif(opcao==3):
                imprimir_lista()
            elif(opcao==4):
                exportar_json()
            elif(opcao==5):
                break
            else:
                print('Opção inválida\n')
        except Exception as ex:
            print('Caractere inválido')
        
       
                            

     


__init__()

