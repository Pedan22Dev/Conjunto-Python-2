#Inventario
equipamentos = []
valores = []
departamentos = []
seriais = []
resposta = "S"
loopVar = ""
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()


busca = input("\nDigite o nome do equipamento que deseja buscar no inventário: ")

for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print ("Valor..: ", valores[indice])
        print ("Serial..: ", seriais[indice])
        print ("E está sobre gestão do departamento de " + departamentos[indice])
        