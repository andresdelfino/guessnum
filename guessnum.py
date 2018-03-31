max_n = 100

max_n_dec_len = len(str(max_n))
max_n_bin_len = len(bin(max_n)[2:])

bin_list = []
for n in range(1, max_n + 1):
    bin_list.append(bin(n)[2:].rjust(max_n_bin_len, '0'))

print(f'Piense en un número entre 1 y {max_n}, ambos incluidos.')

guess = []
for position in range(max_n_bin_len - 1, -1, -1):
    print()

    bit_list = []
    for n in bin_list:
        if n[position] == '1':
            bit_list.append(n)

    line_width = 0
    for n in bit_list:
        if line_width != 0:
            print(' ', end='')
            line_width += 1
        print(str(int(n, 2)).rjust(max_n_dec_len), end='')
        line_width += max_n_dec_len
        if line_width + 1 + max_n_dec_len > 72:
            print()
            line_width = 0
    print('\n')

    response = ''
    while response not in ('S', 'N'):
        response = input('¿Está su número en la lista? [S/N]: ').upper()

    if response == 'S':
        guess.append('1')
    else:
        guess.append('0')

print()

guess = int(''.join(reversed(guess)), 2)

if 1 <= guess <= max_n:
    print('Pensó en el número:', guess)
else:
    print('No respondió correctamente las preguntas.')
