def preencherInventario(inventario):
    resposta = "S"
    while resposta == "S":
        equipamento = [input("Equipamento: "),
                    float(input("Valor: ")),
                    int(input("Número Serial:  ")),
                    input("Departamento: ")
                    ]
        inventario.append(equipamento)
        resposta = input("Digite \"S\" para continuar: ").upper()

def exibirInventario(inventario):
    for elemento in inventario:
        print ("Nome..: ", elemento[0])
        print ("Valor..: ", elemento[1])
        print ("Serial..: ", elemento[2])
        print ("E está sobre gestão do departamento de " + elemento[3])

def localizarPorNome(inventario):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    for elemento in inventario:
        if busca == elemento[0]:
            print('Valor...: ', elemento[1])
            print('Número de série...: ', elemento[2])

def depreciarPorNome(inventario):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in inventario:
        if depreciacao == elemento[0]:
            print('Valor antigo...: ', elemento[1])
            elemento[1] = elemento[1] * 0.9
            print('Novo valor...: ', elemento[1])

def excluirPorSerial(inventario):
    serial = int(input('\nDigite o número de série do equipamento que será excluído do sistema: '))
    for elemento in inventario:
        if elemento[2] == serial:
            inventario.remove(elemento)
    return "Itens Excluídos."       


def resumirValores(inventario):
    valores = []
    for elemento in inventario:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("Todos os equipamentos juntos tem o valor de...: ", sum(valores))