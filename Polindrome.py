def palindrome(text):
    result  = ''   
    in_list = []
    for char in text:                     #Recorrer el string para crear una lista con cada caracter y remover los espacios.
        if char.isalpha():
            in_list.append(char)
        else: continue
    in_list_reversed = in_list[::-1]      #Clonar e invertir la lista.

    if in_list_reversed == in_list:       #Verificar si ambas listas coinciden
        result = 'Is a palindrome'
    else:
        result = 'Is not palindrome'
    return result


in_Text = input('Please enter the desired text to verify as palindrome\n\n==>').lower()

is_palindrome = palindrome(in_Text)
print (is_palindrome)

