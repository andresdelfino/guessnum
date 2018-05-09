import numberguesser


min_n = 1
max_n = 100

max_n_dec_len = len(str(max_n))

ng = numberguesser.NumberGuesser(min_n, max_n)

print(f'Piense en un número entre {min_n} y {max_n}, ambos incluidos.')

for table in ng.get_tables():
    print()
    line_width = 0
    for n in table:
        if line_width != 0:
            print(' ', end='')
            line_width += 1
        print(str(n).rjust(max_n_dec_len), end='')
        line_width += max_n_dec_len
        if line_width + 1 + max_n_dec_len > 72:
            print()
            line_width = 0
    print('\n')

    response = None
    while response not in ('S', 'N'):
        response = input('¿Está su número en la lista? [S/N]: ').upper()

    ng.store_response(response == 'S')

print()

try:
    guess = ng.guess_number()
except numberguesser.InvalidAnswers:
    print('No respondió correctamente las preguntas.')
else:
    print('Pensó en el número:', guess)
