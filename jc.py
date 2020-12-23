from tkinter import *
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 

#root = Tk()

#inp1=Entry(root)
#inp1.insert()
#inp1.pack()
#ref1=Entry(root)
#ref1.pack()
input_ans = input("enter the user input")
ref_ans = input("enter the ref ans")



def data_processing(str):
    
    str=str.lower().strip()
    #removing stopwords(the,them,are,is...)
    stop_w = set(stopwords.words('english'))
    tokens = word_tokenize(str)
    list1 = []

    for x in tokens:
        if x not in stop_w:
            list1.append(x)
    #print(list1)        
    #stemming(for inflections) ie friend and friends are considered as friend(retains only the stem)
    ps = PorterStemmer()
    psl = []
    for w in list1:
       psl.append(ps.stem(w))
    psl = list(dict.fromkeys(psl))   


    return psl       


input_list = data_processing(input_ans)  #list after data processing
reference_list = data_processing(ref_ans)

#print( input_list)
#print(reference_list)

def jacc():
    #input_ans = inp1.get()
    #ref_ans = ref1.get()
    input_list = data_processing(input_ans)
    reference_list = data_processing(ref_ans)

    #print( input_list)
    #print(reference_list)

    intersection = len(list(set(input_list).intersection(reference_list)))
    union = (len(input_list) + len(reference_list)) - intersection
    #print(intersection)
    #print(union)
    j_value = float(intersection) / union
    #label_in = Label(root,text = j_value )
    #label_in.pack()
    return j_value

print(jacc())    

#button = Button(root,text = "FINISH", command=jacc) 
#button.pack()   

#root.mainloop()

#start writing your code