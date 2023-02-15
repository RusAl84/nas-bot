import nltk
import pymorphy2
import string

def remove_digit(str1):
    str2 = ''
    for c in str1:
        if c not in ('0', "1", '2', '3', '4', '5', '6', '7', '8', '9', '«', '»', '–', "\""):
            str2 = str2 + c
    return str2

def remove_punctuation(str1):
    str2 = ''
    pattern = string.punctuation
    for c in str1:
        if c not in pattern:
            str2 = str2 + c
        else:
            str2 = str2 + ""
    return str2
    
def getKeywords(str1):
    mas=[]
    morph = pymorphy2.MorphAnalyzer()
    for i in str1.split():
        if len(i)>2:
            p = morph.parse(i)[0]
            str2=p.normal_form
            str2 =remove_digit(str2)
            str2 =remove_punctuation(str2)
            mas.append(str2)
    set2 = set()
    for item in mas:
        if not "nan" in str(item).replace(" nan ", " "):
            set2.add(str(item).replace(" nan ", " "))
    mas = list(set2)
    mas.sort()
    return(mas)

if __name__ == '__main__':
    nltk.download('stopwords')
    nltk.download('punkt')
    str1="Ежи – это небольшие животные с иголками, вес которых редко превышает 1 килограмм."
    str1="Точная наука, первоначально исследовавшая количественные отношения и пространственные формы."
    str1="Область естествознания: наука о наиболее общих законах природы, о материи, её структуре, движении и правилах трансформации."
    mas=getKeywords(str1)
    str2=""
    for i in mas:
        str2+=f", \"{i}\""
    str2=f"[{str2[2:]}]"
    print(str2)
    
