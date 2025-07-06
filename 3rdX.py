def longestword(sen):
    contenders = ''
    for x in sen:
        if x != ' ':
            if x.isalpha():
                contenders += x
                #go to next letter
                continue
        contenders += ','
    z = max(contenders.split(','), key=len)
    #covert Z to list to access indexing
    char_list = list(z)
    for y in range(1, len(char_list)):
        if ((y+1)%3)  == 0:
            char_list[y] = 'X'
        else:
            continue
    restrung = ''.join(char_list)
    return restrung
    


sen = 'appleblah1$%34! banana chairzyxwvutsr diamond$(&%*(@%))'
print("The longest word given is:", (longestword(sen)))