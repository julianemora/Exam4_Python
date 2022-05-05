#!/usr/bin/env python3

import pandas as pd 
def substrings_possible_function(string_of_letters,k): #function for possible substrings
    '''sub_str_possible function input is the text file defined and a k value,
    output is minimum number of possible substrings
    '''
    assert k>0,'k cannot by negative'
    for letter in string_of_letters:
        assert letter in ["A","G","T","C"], 'characters can only be AGTC'
    substring_possible= len(string_of_letters)- k +1 #formula for calculating possible substrings
    total_combos= 4**k
    return(min(substring_possible,total_combos))

def observed_substrings_function(string_of_letters,k): #function for observed substrings
    '''observed_substrings function input is the text file and a k value,
    output is the number of observed substrings that are unique
    '''
    newlst=[]
    assert k > 0, 'k cannot be negative'
    for letter in string_of_letters:
        assert letter in ["A","G","T","C"], 'characters can only be AGTC'
    observed_substrings= [string_of_letters[i:i+(k)] for i in range(0,len(string_of_letters),1)] #formula for all substrings
    for i in range(0,len(observed_substrings)):
        if(len(observed_substrings) ==k): #lenth of the substrings must be equal to k value
            observed_substrings.pop()
    for item in observed_substrings:
        if len(item) ==k:
            newlst.append(item) #adding each substring that is the length of k to a new list
    unique_set=set(newlst)
    unique_list=list([unique_set])
    for x in unique_list:
        return (len(x))

def create_df(string_of_letters): #creating a dataframe with k value, possible substrings, and observed substrings
    '''create_df function input is text file defined,
        output is a table with each k value for the length of line specified, possible substrings, and observed substrings
    '''
    poslist=[]
    obslist=[]
    kvalues=[]
    for k in range(1,len(string_of_letters)+1):
        obskmers=(observed_substrings_function(string_of_letters,k))
        obslist.append(obskmers)
    for k in range(1,len(string_of_letters)+1):
        poskmers=(substrings_possible_function(string_of_letters,k))
        poslist.append(poskmers)
    for k in range(1,len(string_of_letters)+1):
        kvalues.append(k)
    data={'k': kvalues,
          'observed kmers':obslist,
          'possible kmers':poslist}
    df=pd.DataFrame(data)
    return (df)

def ling_complx(string_of_letters):
    '''ling_complx function input is file defined,
    output is the sum of observed substrings divided by possible substrings
    '''
    obslist_ling=[]
    poslist_ling=[]
    for k in range(1,len(string_of_letters)+1):
        obskmers_ling= observed_substrings_function(string_of_letters,k)
        obslist_ling.append(obskmers_ling)
    for k in range(1,len(string_of_letters)+1):
        poskmers_ling=substrings_possible_function(string_of_letters,k)
        poslist_ling.append(poskmers_ling)
    return((sum(obslist_ling))/(sum(poslist_ling)))

myfile = 'listofstrings.txt' #this is the text file with the sequences
with open(myfile, "r") as f:
    for eachline in f:
        eachline = eachline.strip()
        print(eachline)
        print(create_df(eachline))
        print(ling_complx(eachline))