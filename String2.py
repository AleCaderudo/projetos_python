#O .strip() retira os espaços ates e depois da variavel, mas n os do meio
nome = input("Digite o seu nome: ").strip()
print(f"\nNome Maiusculo: {nome.upper()}\n\nNome em minusculo: {nome.lower()}\n" )
print(f"Nome sem espaços no meio: {len(nome) - nome.count(" ")}\n")
print(f"Quantas letras tem o primeiro nome: {nome.find(" ")}\n")
separa = nome.split()
print(f"Sepra 2: {separa[0], len(separa[0])}")

