def reverse(text):
    reversed = ''
    for i in range(len(text)):
        reversed += text[len(text) - i - 1]
    return reversed