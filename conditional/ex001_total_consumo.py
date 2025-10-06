preco_hamburguer = 12
preco_batata_frita = 7
preco_refri = 5

qtd_haburguer = int(input('Quantos haburgueres você consumiu?'))
qtd_batata = int(input('Quantas batata você consumiu?'))
qt_refri = int(input('Quantos refrigerantes vocês consumiu?'))

total_consumo = ((preco_hamburguer*qtd_haburguer)+(qtd_batata*preco_batata_frita)+(preco_refri*qt_refri))

print(f'você consumiu {total_consumo}.')

