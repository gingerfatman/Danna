s = 'Today was a lovely day. I took a trip to the beach.'

num = 0

for letter in s.lower(): 
    if letter in 'aeiou':
        num += 1
   
print(f'This sentence has {num} vowels.')

