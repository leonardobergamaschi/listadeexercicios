print('Este programa irá solicitar as notas dos 4 bimestres e mostrar a média')

nota1 = float(input('Nota do 1º bimestre: '))
nota2 = float(input('Nota do 2º bimestre: '))
nota3 = float(input('Nota do 3º bimestre: '))
nota4 = float(input('Nota do 4º bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média anual é {media}')