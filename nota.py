nota1=float(input('Qual a nota do primeiro trimestre?'))
nota2=float(input('Qual a nota do segundo trimestre?'))
nota3=float(input('Qual a nota do terceiro trimestre?'))

medía=(nota1+ nota2+ nota3)/3

if(medía < 2):
    print('VOCÊ É UM MERDA')
elif(medía < 5):
    print('REPROVADO')
else:
    print('aprovado')



