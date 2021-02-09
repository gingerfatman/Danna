s = 'Today was a lovely day. I took a trip to the beach.'

num = 0

for letter in s: 
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        num = num + 1
   
msg = 'This sentence has {} vowels.'
print(msg.format(num))





