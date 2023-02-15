import json
import getKeywords as gk


def load_data():
    content = ""
    with open('data.json', 'r', encoding='utf-8') as f:
        content = f.read()
    # print(content)
    test_data = json.loads(content)
    return test_data


def get_question(test_data, num):
    str1 = test_data[num]['question']+"\n"
    str1 += "Введите ответ в развернутой форме:"
    return str1
    
def check_answer(test_data, num, answer_text):
    result = 0
    if num < len(test_data):
        countIntersections=0
        keywords1=gk.getKeywords(answer_text)
        keywords2=test_data[num]['keyWords']
        for i1 in keywords1:
            for i2 in keywords2:
                if i1==i2:
                    countIntersections+=1
        result = countIntersections / len(keywords1) * 100
    return result


if __name__ == '__main__':
    test_data = load_data()
    quest = test_data[0]
