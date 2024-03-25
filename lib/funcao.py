from database import salas, equipamentos

def mostrar_s():
    print(salas)
    funcao_sala()

def criar_s():
    nome_sala = input("/n Qual o nome da sala? ")
    if equipamentos:
        max_id = max(conta["id"] for conta in equipamentos)
    else:
        max_id = 0
    numero_sala = int(input("/n Qual o numero da sala ?")) 

    nova_sala = {
            "id": max_id + 1,
            "numero": numero_sala,
            "nome": nome_sala
        }   
    equipamentos.append(nova_sala)

    funcao_sala()

def atualizar_s():
    print()

def deletar_s():
    print()

# equipamentos

def mostrar_e():
    print(equipamentos)
    funcao_equipamento()

def criar_e():
    tipo_e = input("/n Qual o tipo do novo equipamento")
    if equipamentos:
        max_id = max(conta["id"] for conta in equipamentos)
    else:
        max_id = 0
    if equipamentos:
        max_tomabamento = max(conta["tombamento"] for conta in equipamentos)
    else:
        max_tomabamento = 0
    sala_e = int(input("/n Qual o id da sala ?")) 

    novo_equipamento = {
            "id": max_id + 1,
            "tombamento": max_tomabamento + 1,
            "tipo": tipo_e,
            "sala_id": sala_e
        }   
    equipamentos.append(novo_equipamento)

    funcao_equipamento()

def atualizar_e():
    idatualizar_e = int(input("\nQual o índice da despesa que você deseja atualizar? "))

    equip_p_atualizar = None
    for equipamento in equipamentos: 
        if equipamento["id"] == idatualizar_e:
            equip_p_atualizar = equipamento
            break
    
    if equip_p_atualizar == None:
        print("Valor não encontrado!")
    else:
        tipo_ne = input("\nQual o novo tipo? ")
        salaid_ne = int(input("\nQual o novo id da sala? "))
        
        equip_p_atualizar["sala_id"] = salaid_ne
        equip_p_atualizar["tipo"] = tipo_ne

    funcao_equipamento()

def deletar_e():
    id_para_deletar = int(input("\nId que você deseja deletar: "))
    
    for equipamento in equipamentos: 
        if equipamento["id"] == id_para_deletar:
            equipamentos.remove(equipamento)
            print("Equipamento removido com sucesso.")
            break
    else:
        print("Equipamento não encontrado.")
    funcao_equipamento()

def buscar_e():
    id_p_buscar = int(input("\nQual o índice que você deseja buscar ?"))

    for equipamento in equipamentos: 
        if equipamento["id"] == id_p_buscar:
            print(equipamento)
            
            break

    funcao_equipamento()
def mudar_sala_e():
    id_p_mudarDeSala = int(input("\nQual o índice que você deseja trocar ?"))

    for equipamento in equipamentos: 
        if equipamento["id"] == id_p_mudarDeSala:
            int_mudar_sala = int(input("Qual a sala que você vai mudar ?"))
            equipamento["sala_id"] = int_mudar_sala
            
            break
    funcao_equipamento()

def funcao_sala():
    print("""
    Visualizar lista [1]
    Adicionar [2]
    Atualizar [3]
    Deletar [4]
    Sair [5]
    """)
    indice = int(input(': '))
    if indice == 1:
        mostrar_s()

    elif indice == 2:
        criar_s()

    elif indice == 3:
        atualizar_s()

    elif indice == 4:
        deletar_s()
    elif indice == 5:
        print("\nSaindo...")
    else:
        print("\nO valor inserido é inválido.")

def funcao_equipamento():
    print("""
    Visualizar lista [1]
    Adicionar [2]
    Atualizar [3]
    Deletar [4]
    Buscar [5]
    Trocar de sala [6]
    Sair [7]
    """)
    indice = int(input(': '))
    if indice == 1:
        mostrar_e()

    elif indice == 2:
        criar_e()

    elif indice == 3:
        atualizar_e()

    elif indice == 4:
        deletar_e()

    elif indice == 5:
        buscar_e()

    elif indice == 6:
        mudar_sala_e()

    elif indice == 7:
        print("\nSaindo...")
    else:
        print("\nO valor inserido é inválido.")