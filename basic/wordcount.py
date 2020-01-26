import re #import a module to handle Regular Expressions (RegEx)

dic_content = {}
def openFile(path):
    s = ""
    f = open(path,"rt",newline=None)
    #s = f.readlines()
    s = f.read()
    #print(*print_words(s.lower()), sep="\n")
    print('\n'.join(' '.join(map(str, sl)) for sl in print_words(s.lower())))
    print('___The top 20 most common words__')
    print('\n'.join(' '.join(map(str, sl)) for sl in print_top()))
    f.close()

def print_words(s):
    global dic_content
    element = ""
    ordered_list = []
    list_punct = ['.', ',', '?', '!', ':', ';', '-', '_', '[', ']', '{', '}', '(', ')','"',"'"]
    for i in s:
        if i in list_punct:
            if i not in dic_content:
                dic_content[i] = 1
            else:
                dic_content[i] += 1
    list_words = s.split()
    for i in list_words:
        element = i.strip("".join(list_punct))
        if element not in dic_content:
            dic_content[element] = 1
        else:
            dic_content[element] += 1
    ordered_list = sorted(dic_content.items())
    return ordered_list
        #list_punct.append(re.split('\w',i))
        #each_element = re.split('\d',element)
        #each_element.append(element.split())


def print_top():
    twentyList = sorted(dic_content.items(),key=tuplaOrdenada,reverse=True)[0:20]
    return twentyList

def tuplaOrdenada(t):
    return t[1];
def main():
    input_var = input("Enter the path to access the file: ")
    openFile(input_var)

if __name__ == '__main__':
    main()
