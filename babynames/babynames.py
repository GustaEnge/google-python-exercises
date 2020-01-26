import os
import os.path
import re

def openFile(filename, action):
    s = ""
    list_ranking = []
    try:
        with open(filename,"rt",newline=None) as f:
            list_ranking = extract_names(f.read())
            print(list_ranking)
            f.close()
            if action == '--summary':
                write_file(list_ranking)
    except:
        print("Couldn't find any file in this path.")

def extract_names(file):
    dict_win = {}
    full_list = []
    list_win = []
    year = int(re.findall(r"([0-9]*)</h3>",file)[0])
    beginning_anchor_term = file.find("h3")
    ending_anchor_term = file[beginning_anchor_term:].find("</table>")
    str_var = file[beginning_anchor_term:ending_anchor_term]
    name_rank = re.findall(r'(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)',str_var)
    for name in name_rank:
        dict_win[name[1]] = name[0]
        dict_win[name[2]] = name[0]
    list_win = list(dict_win.keys())
    list_win.sort()
    full_list.append(year)
    for i in range(len(list_win)):
        full_list.append(str(list_win[i]+" "+dict_win[list_win[i]]))
    return full_list

def write_file(list_var):
    current_path = r"C:\Users\gustavo.cunha\Desktop\Pessoal\google-python-exercises\babynames\summary"+f'{list_var[0]}'+'.txt'

    if os.path.isfile(current_path):
        os.remove(current_path)
    w = open(r"C:\Users\gustavo.cunha\Desktop\Pessoal\google-python-exercises\babynames\summary" + f'{list_var[0]}' + '.txt',"w")
    for each in list_var:
        print(each, end="\n", file=w)
        # print("".join(map(str, stretch) for stretch in list_var), end="\n") upcoming improvement using Generator

    w.close()

#here a function that runs every single file  and release an overall of the most used names based on search
def main():
    
    #input_var = input("Insert the path: ")
    #input_var = r"C:\Users\gustavo.cunha\Desktop\Pessoal\texto_mimic.txt"
    year_summary = input("Enter the year you would like to see the most used names and --summary for retrieving the ranking into a new file: ").split()
    input_var = str(r"C:\Users\gustavo.cunha\Desktop\Pessoal\google-python-exercises\babynames\baby"+f'{year_summary[0]}'+".html")
    openFile(input_var,year_summary[1].lower())


if __name__ == "__main__":
    main()
