texto = "Esta "
print(texto + " esta é uma string")

result = texto * 4 + " esta é uma " + " string " * 6
print (result)
print("=" * 30)

texto2 = "Esta é uma string"
# da posiçao 0 ate 4
print(texto2[0:4])
print(texto2[7:10])
print(texto2[-6:])
print(texto2[:6])
# de 2 em 2 ate 10
print(texto2[0:10:2])
# ate o final de 2 em 2
print(texto2[::2])
# invertida
print(texto2[::-1])

print('dois prints \n na mesma linha', end='')
print('continua o texto na mesma linha')