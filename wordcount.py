"""Count words in file."""
new_file = open("test.txt")
dictionary_t = {}
for line in new_file:
    line = line.rstrip()
    word = line.split(" ")
    for item in word:
      #print("----------->",word)
      dictionary_t[item] = dictionary_t.get(item, 0) +1
      #print(dictionary_t)

for key,value in dictionary_t.items():
   print(f'{key} {value}')  





# put your code here.
