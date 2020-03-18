result={}

def text_to_list (text_string):
    return text_string.split( )

def analysis(text_list):
    for i in text_list:
        if i in result:
            result[i]+=1
        else:
            result[i]=1

text_source=open(r'F:\Python\Lesson 5\Text.txt','r')
text_string=text_source.read().lower()
text_list=text_to_list(text_string)
analysis(text_list)

print(result)
