#var
n = 0
nota = []
somanotas = 0
media = 0
nome = str(input('Boas vindas, Digite seu nome:'))


#loop e processamento
for c in range(1, 5):
  n = int(input(f'Digite sua nota do {c}º bimestre: '))
  nota.append(n)
  somanotas = somanotas + n


media = somanotas/4


#saída
print('-' * 10)
if media >= 7:
  print(f'Parabéns, {nome}, você passou!')
else:
  print(f'Infelizmente, {nome}, você reprovou.')
print(f'Suas notas foram: {nota}, tendo média: {media}.')

	No código acima, é possível visualizar a estrutur
