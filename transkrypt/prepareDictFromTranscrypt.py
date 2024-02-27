import ast
import jieba
from pypinyin import lazy_pinyin, Style
#from translate import Translator // tutaj cos nie dziala nie tlumczy tylko wypisuje to samo slowo probuje dalej
from googletrans import Translator
import jieba.posseg as pseg



def getHSKvoccab():

    hsk1= ast.literal_eval(open(r"C:\Users\PC\Desktop\Uczelnia\projekty\HSK\hsk1_array.txt", "r", encoding="utf-8").read())
    hsk2= ast.literal_eval(open(r"C:\Users\PC\Desktop\Uczelnia\projekty\HSK\hsk2_array.txt", "r", encoding="utf-8").read())
    hsk3= ast.literal_eval(open(r"C:\Users\PC\Desktop\Uczelnia\projekty\HSK\hsk3_array.txt", "r", encoding="utf-8").read())
    hsk4= ast.literal_eval(open(r"C:\Users\PC\Desktop\Uczelnia\projekty\HSK\hsk4_array.txt", "r", encoding="utf-8").read())
    hsk5= ast.literal_eval(open(r"C:\Users\PC\Desktop\Uczelnia\projekty\HSK\hsk5_array.txt", "r", encoding="utf-8").read())
    hsk6= ast.literal_eval(open(r"C:\Users\PC\Desktop\Uczelnia\projekty\HSK\hsk6_array.txt", "r", encoding="utf-8").read())

    print(len(hsk1))
    print(len(hsk2))
    print(len(hsk3))
    print(len(hsk4))
    print(len(hsk5))
    print(len(hsk6))

    return hsk1, hsk2, hsk3, hsk4, hsk5, hsk6
def getTranskrypt(path):
    tr= ast.literal_eval(open("patriotyzmTranskrypt.txt", "r", encoding="utf-8").read())
    return tr
def getHSKLevel(word):

    if word in hsk1:
        return 1
    elif word in hsk2:
        return 2
    elif word in hsk3:
        return 3
    elif word in hsk4:
        return 4
    elif word in hsk5:
        return 5
    elif word in hsk6:
        return 6
    else:
        return 789
def getDefinition(word):
    translator= Translator()
    print("robie definicje")
    definition= translator.translate(word, src='zh-cn', dest='en')
    #print("slowo:", word, "definicja: ", definition.text)
    return definition.text



final_dict= {}

hsk1, hsk2, hsk3, hsk4, hsk5, hsk6= getHSKvoccab()
transkrypt= getTranskrypt("patriotyzmTranskrypt.txt")

for key in transkrypt:
    s= []
    form_classes= []

    line= transkrypt[key]
    segments= jieba.posseg.cut(line)
    for character, form_class in segments:
        s.append(character)
        form_classes.append(form_class)

    #segmented_line= list(jieba.cut(line))
    line_pinyin= lazy_pinyin(line, style=Style.TONE3)

    l= 0
    pinyin_for_each_word= []
    def_for_each_word= []
    hsk_for_each_word= []
    for i in range(len(s)):
        n= len(s[i])
        pinyin= line_pinyin[l:l+n]
        l +=n

        hsk_level= getHSKLevel(s[i])
        print(s[i], hsk_level)
        try:
            definition= getDefinition(s[i])
        except:
            definition= "jakis eror"
        print("slowo: ", s[i], " def: ", definition)

        pinyin_for_each_word.append(pinyin)
        
        def_for_each_word.append(definition)
      
            
        hsk_for_each_word.append(hsk_level)

    final_dict[key]= [s, pinyin_for_each_word, def_for_each_word, hsk_for_each_word, form_classes]

print(final_dict)
f= open("transkrypt_dict.txt", "a", encoding="utf-8")
f.write(str(final_dict))
f.close()
#print(final_dict[27])



