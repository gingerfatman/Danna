s = 'Today was a lovely day. I took a trip to the beach.'

num = 0

for letter in s: 
    if letter == 'a':
        num = num + 1
    elif letter == 'e':
        num = num + 1
    elif letter == 'i':
        num = num + 1
    elif letter == 'o':
        num = num + 1
    elif letter == 'u':
        num = num + 1
    else: 
        continue

msg = 'This sentence has {} vowels.'
print(msg.format(num))




