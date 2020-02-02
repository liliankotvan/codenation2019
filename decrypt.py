import string
import hashlib

#criando a função
def decrypt(key, message):
    #colocando todas as letras em minúsculo
    message = message.lower()
    #alfabeto em minúsculo
    alpha = string.lowercase
    print alpha
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

#main para chamar a função e imprimir o resultado
if __name__ == '__main__':
    key = 10
    message = 'zvkxc kbo gybdrvocc, led zvkxxsxq sc ofobidrsxq. ngsqrd n. oscoxrygob'
    decrypted = decrypt(key, message)
    print(decrypted)
    #imprimindo o  do resumo criptográfico do texto decriptado
    hash_decrypted = hashlib.sha1(decrypted).hexdigest()
    print hash_decrypted
