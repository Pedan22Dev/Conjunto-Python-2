from functionDef import *

meuInventario=[]
print('Preenchendo')
preencherInventario(meuInventario)
print('Exibindo')
exibirInventario(meuInventario)

print('Buscando...')
localizarPorNome(meuInventario)
print('Alterando...')
depreciarPorNome(meuInventario)
print('Alterado.')

print('Excluindo...')
print(excluirPorSerial(meuInventario))
exibirInventario(meuInventario)

print('Resumindo valores...')
resumirValores(meuInventario)