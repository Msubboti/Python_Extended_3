import re
import string

def count_func(file):
    file = open(file, 'r')
    file_string = file.read().lower()
    match=sorted(re.findall(r'\b[a-z]{3,15}\b', file_string))
    n_match=sorted(list(set(match)))
    s=tuple(map(lambda x: match.count(x), n_match))
    result=dict(zip(n_match, s))
    res=list(map(lambda x: print(x, result[x]), result))
    return res
    
r=count_func('english_words.txt')
