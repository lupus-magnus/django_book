# O usuario deve digitar uma palavra que sera a resposta de um jogo da forca.
# Em seguida, informe o tamanho da palavra e peca para adivinhar a primeira letra, a segunda, etc.
# Errando 6 vezes, o jogo acaba
# Acertando a palavra, o jogo acaba também.
import time

resposta = input("Qual será a palavra escondida?\t")
resposta = resposta.upper()
lifes_remaining = 6
discovering_letter = 0
encrypted = "#" * len(resposta)

# time.sleep(0.5)
print("3...")
# time.sleep(1)
print("2...")
# time.sleep(1)
print("1...")
# time.sleep(1)

print("Vamos nessa!\n\n")

while (lifes_remaining > 0) and (discovering_letter < len(encrypted)):

    msg = (
        f"A palavra é: {encrypted}\nVocê tem {lifes_remaining} tentativas restantes.\n"
    )
    time.sleep(1)
    print(msg)
    time.sleep(1)
    new_try = input("E aí, algum palpite de letra?\t").upper()

    if resposta[discovering_letter] == new_try:
        # mudamos encrypted pra lista pra poder mudar a letra e depois voltamos pra string
        print("\nBoa! Você acertou uma letra!\n")
        encrypted_array = []
        for char in encrypted:
            encrypted_array.append(char)
        # print("encrypted_array:", encrypted_array)
        encrypted_array[discovering_letter] = new_try
        # print("encrypted_array after saying that equals new_try char", encrypted_array)
        encrypted = (" ".join(encrypted_array)).replace(" ", "")
        # print("encrypted after join and replace:", encrypted)
        discovering_letter += 1
        if discovering_letter >= len(encrypted):
            print("AEEEEEEEEE! Parabéns! Você venceu!")
    else:
        lifes_remaining -= 1
        print("Ops, acho que não hein.\n")

print("HAHAHA Você perdeu :P")
