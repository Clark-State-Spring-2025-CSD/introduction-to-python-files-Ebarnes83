#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 
import math

def isPalindrome(s): 
    if (s == s[::-1] ): return True
    else: return False

def findPalindrome(): 
    list3=list() 
    for line in open("words.txt"): 
        list1 = line.strip() 
        list2 = list1.split() 
        for x in list2:
            if isPalindrome(x): 
                list3.append(x) 

    return list3 

palim_list = findPalindrome()

count = 0
for i in palim_list:
    count += 1

print(f"The number of palindromes: {count}")

