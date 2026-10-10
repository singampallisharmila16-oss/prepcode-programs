words="hippopotamus"
vowels_count=0
con=0
vowels=["a","e","i","o","u"]
for i in vowels:
    vowels_count=vowels_count+words.count(i)
print(vowels_count)
con=len(words)-vowels_count
print(con)






