import ast
import operator
from itertools import islice

def getTranskrypt():
    tr= ast.literal_eval(open("transkrypt_dict.txt", "r", encoding="utf-8").read())
    return tr
def make_hsk_histogram():
    transkrypt= getTranskrypt()
    #print(transkrypt)
    hsk_histogram= {}
    for key in transkrypt:
        line= transkrypt[key][3]
        for level in line:
            if level not in hsk_histogram:
                hsk_histogram[level] =1
            else:
                hsk_histogram[level] +=1
    return hsk_histogram

   
 #print(hsk_histogram)
def find_key_words():
    transkrypt= getTranskrypt()

    key_words= {}
    characters_to_omit= [' ', '这个', '一个' ] #uzupełnic na bazie przyszych tekstow
    form_classes_to_omit= ['uj', 'uz', 'r', 'w', 'm', 'nr', 'c'] #dostosowac na bazie przyszluch tekstow

    for key in transkrypt:
        
        line= transkrypt[key][0]
        
        i= 0
        for character in line:
            hsk= transkrypt[key][3][i]
            character_form_class= ""
            i+= 1
            if hsk == 1 or character_form_class in form_classes_to_omit  or character in characters_to_omit:
                continue

            #print(hsk)
            if character not in key_words:
                key_words[character]= 1
            else:
                key_words[character]+= 1
            

    top_10_key_words= dict(sorted(key_words.items(), key=operator.itemgetter(1), reverse=True))
    top_10_key_words= dict(islice(top_10_key_words.items(), 10))

    return top_10_key_words





print(find_key_words())
f= open("hsk_histogram_episode1.txt", "a", encoding="utf-8")
f.write(str(make_hsk_histogram()))
f.close() 