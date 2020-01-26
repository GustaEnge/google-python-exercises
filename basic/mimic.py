import unidecode,random

#dict_mimic = {"":""}
dict_mimic = {}


def openFile(path):
    f = open(path, "rt", newline=None)
    unicode_s = f.read()
    s = unidecode.unidecode(unicode_s) #Remove the diacritics by converting a plain text into unicode (utf-8), it seems that doesn't need a conversion u"<unicode_s>" anymore to use unidecode method
    mimic(s.lower())
    print(mimic_dict(dict_mimic,10))
    f.close()


def mimic(s):
    global dict_mimic
    list_punct = ['.', ',', '?', '!', ':', ';', '-', '_', '[', ']', '{', '}', '(', ')', '"', "'"]
    list_terms = s.split()
    index_term = 0
    list_terms = list(map(lambda x: x.strip("".join(list_punct)), list_terms)) #removing all the punctuations into the text
    #print(list_terms)
    for each_w in range(len(list_terms)):
        if list_terms[each_w] not in dict_mimic and each_w < len(list_terms) - 1:
            index_term = list_terms.index(list_terms[each_w])
            dict_mimic[list_terms[each_w]] = [list_terms[index_term + 1]]
            for j in range(index_term + 1, len(list_terms) - 1):
                if list_terms[j] == list_terms[each_w]:
                    dict_mimic[list_terms[each_w]] += [list_terms[j + 1]]
        elif list_terms[each_w] not in dict_mimic and each_w == len(list_terms) - 1:
            dict_mimic[list_terms[each_w]] = [""]
    return dict_mimic

def mimic_dict(dict,number):
    text = ""
    for i in range(number):
        guess_key = random.choice(list(dict.keys()))
        guess_value = random.choice(dict[guess_key])
        text += " "+guess_value
    return text

def main():
    #input_var = input("Enter the path to access the file: ")
    #input_var = r"C:\Users\gustavo.cunha\Desktop\Pessoal\texto_mimic.txt"
    input_var = r"C:\Users\gustavo.cunha\Desktop\Pessoal\recursos_3.txt"
    openFile(input_var)

if __name__ == "__main__":
    main()