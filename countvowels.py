s = 'Today was a lovely day. I took a trip to the beach.'.lower()


a = s.count('a')
e = s.count('e')
i = s.count('i')
o = s.count('o')
u = s.count('u')

num = a + e + i + o + u

msg = 'This sentence has {} vowels.'
print(msg.format(num))




