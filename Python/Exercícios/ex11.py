lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
print('Sua parede tem dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}'.format(lar, alt,area)) 
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.2f}L de tinta.'.format(tinta))
