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
    return z

#sen = 'apple banana dogs at chair1234 bob!#%&'
sen = 'apple4783^ dogs at banana chair1234 bob!#$* defensive'
#sen = 'apple4783 dogs at char12345677 bob@ bob'
print("The longest word given is:" ,(longestword(sen)))