#Informaçoes em inglês, Ex: Brazil, 1980, Female, Summer..
import csv
import matplotlib.pyplot as plt    

with open ('athlete_events.csv','r') as csv_file:
  arq=csv.reader(csv_file)

  next(arq)
  
  pais=input('Defina o país de pesquisa:')
  ano_olimp_=int(input('A partir de que ano você quer os dados ?:'))
  sexo=input('Defina o sexo dos participantes (Male/Female ): ')
  ano_olimp = 2016 - ano_olimp_
  tipo_olimp=input('Olimpiada de verão (Summer) ou inverno (Winter) ?:')

  medalhas=dict()
  qtd_medalhas=list()
  medalhas['Ouro']=0
  medalhas['Prata']=0
  medalhas['Bronze']=0

#MASCULINO
  if sexo == 'Male':
    for linha in arq:
      if str(linha[2]) == 'M' and str(linha[6]) == pais and int(linha[9]) >= ano_olimp and       str(linha[10]) == tipo_olimp and str(linha[14]) != 'NA':
    
        if str(linha[14]) == 'Gold':
          medalhas['Ouro']=medalhas['Ouro']+1
        elif str(linha[14]) == 'Silver':
          medalhas['Prata']=medalhas['Prata']+1
        elif str(linha[14]) == 'Bronze':
          medalhas['Bronze']=medalhas['Bronze']+1

#QUANTIDADE DE MEDALHAS (OURO, PRATA E BRONZE)

    for medalha in medalhas.values():
      qtd_medalhas.append(medalha)
    print(qtd_medalhas)

#Feminino

  elif sexo == 'Female':
    for linha in arq:
      if str(linha[2]) == 'F' and str(linha[6]) == pais and int(linha[9]) >= ano_olimp and       str(linha[10]) == tipo_olimp and str(linha[14]) != 'NA':
    
        if str(linha[14]) == 'Gold':
          medalhas['Ouro']=medalhas['Ouro']+1
        elif str(linha[14]) == 'Silver':
          medalhas['Prata']=medalhas['Prata']+1
        elif str(linha[14]) == 'Bronze':
          medalhas['Bronze']=medalhas['Bronze']+1

#QUANTIDADE DE MEDALHAS (OURO, PRATA E BRONZE)

    for medalha in medalhas.values():
      qtd_medalhas.append(medalha)
    print(qtd_medalhas)