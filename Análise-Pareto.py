#Programa que faz a Analise de Pareto de um conjunto de dados
#Prof Luiz
#Fatec Ferraz de Vasconcelos
#Programador:
#Cláudio Rodrigues 2920482211022


arquivo = open("dados.txt","r")#chama o arquivo

#listas vazias
Lista1=[] 
Lista1=arquivo.readlines()
Lista2=[]
Lista3=[]
Lista4=[]
Lista5=[]
Lista6=[]
Lista7=[]
Total=0 #Contador para verificar o número de elementos
FrAcumulada = 0.00 #Variavel usada para calcular a Frequência Acumulada

#Atrela o arquivo à uma lista vazia em seguida o arquivo é lido e colocado de forma limpa no programa
for i in Lista1:
    Lista2.append(i.rstrip())
    Total=Total+1
#print(Lista2)

#Coloca em uma nova lista, um exemplar de cada elemento
for i in Lista2:
    if i not in Lista3:
        Lista3.append(i)

#Conta a quatidade de repetições de cada elemento
for i in Lista3:
    Lista4.append(Lista2.count(i))

print('\n{:<14} {:>11} {:>9} {:>16}'.format('Ocorrências', 'Nr de Ocorrências', 'FR(%)', 'FR acumulada\n'))

#Organiza os defetios e suas quatidades em uma lista vazia e organiza em ordem decrescente
for i in range(0, len(Lista3)):
    Lista5.append([Lista3[i],Lista4[i]]) 
Lista5=sorted(Lista5,key=lambda i : i [1], reverse=True)

#Calcula a Frequência e adiciona a Lista6
for i in range(0,len(Lista4)):
    Lista6.append(((Lista5[i][1])/Total)*100)

#Cria um loop para calcular a Frequência Acumulada e printar todas as informações em formato de tabela
for i in range(0,len(Lista4)):
    FrAcumulada += Lista6[i]
    print(f"{Lista3[i]:>5}{Lista4[i]:>19}{Lista6[i]:>17.2f}%{FrAcumulada:>13.2f}%")
print('{:>7} {:>16} {:>16}%'.format('Total', Total, FrAcumulada))
print ("\nFim do programa!")