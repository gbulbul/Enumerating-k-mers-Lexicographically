bases=['A', 'C', 'G', 'T'] #
list_of_pairs = [(b1, b2) for b1 in bases for b2 in bases]
print(list_of_pairs)
import pandas as pd
df=pd.DataFrame(list_of_pairs)
#print(list(df[0]))
alphabet={1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 
15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
new_list_keys=[]
new_list_values=[]
for key1 in alphabet.keys():
    for key2 in alphabet.keys():
       for v in range(len(list(df[0]))-1):
            if list(df[0])[v+1]==alphabet[key1]:
                if list(df[0])[v]==alphabet[key2]:
                      new_list_keys.append(min(key1,key2))
                      new_list_values.append(min(alphabet[key1],alphabet[key2]))
                      print(new_list_keys,new_list_values)
ele=list(df[0])[-1]
#print(ele)
new_list_values.append(ele)
#print(new_list_values)
df[0]=new_list_values
df.sort_values(0)
#print(df)
mini_dict_values=['A','C','G','T']
def mini_dict_fun(mini_dict_values):
    mini_dict={}
    for i in range(len(mini_dict_values)):
        mini_dict[i]=mini_dict_values[i]
    return mini_dict
#print(mini_dict_fun(mini_dict_values))
mini_dict=mini_dict_fun(mini_dict_values)
class second_col:
    def second_col_arrange(mini_dict,df):
        new_list_vals_second_col=[]
        for k in range(0,len(df[1]),4):
            for v in range(len(mini_dict.items())):
                df[1][v+k]=mini_dict[v]
                new_list_vals_second_col.append(mini_dict[v])
        return new_list_vals_second_col
print(second_col.second_col_arrange(mini_dict,df))
df[1]=second_col.second_col_arrange(mini_dict,df)
print(df)
df['']=df[0] + df[1]
df = df.drop(columns=[0, 1])
print(df.to_string(index=False))