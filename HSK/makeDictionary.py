#chinskie: 19968 : 40959
#spacja to 32
#65-90 DUZE litery
#91-96 znaki specjalne
#97-122 małe litery


hsk2= []
f = open("hsk6.txt", "r", encoding='utf-8')

for text in f:
  word= ""
  for char in range(len(text)):
    if ord(text[char]) >= 19968 and ord(text[char]) <=40959:
        word= word + text[char]
        if ord(text[char+1]) == 32 or ord(text[char+1]) == 65372  or ord(text[char+1])== 65288:
            hsk2.append(word)
            break
f.close()   
print(len(hsk2))

f = open("hsk6_array.txt", "a", encoding='utf-8')
f.write(str(hsk2))
f.close()

#print("kreska: ",ord("（"))
#print("pierwszy", chr(19968))
#print("ostatni", chr(40959))