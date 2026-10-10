s="helloworld123"
v=sum(s.count(i)for i in "aeiou")
d=sum(i.isdigit()for i in s)
print("vowels:",v)
print("digits:",d)