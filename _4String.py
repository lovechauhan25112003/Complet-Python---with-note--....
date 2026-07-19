'''String-- string is a sequence of character enclosed in quets and it is a data type in python 
three way to initialize the string
1. Single Quotes String -> a='Love "Kumar ,Sir'
2. Double Quotes String -> b=" Love's Party "
3. Three Quoted String  -> c=Love's Party hai 
'''

#Operation 
text  = "Python"

"concatenation"
# t = text+" hello"
# print(t)

"Repeatition"
# print(text*3)

"Indexing :"
# print(text[1])

"Slicing "
# print(text[1:3])

"length"
# print(len(text))

"Membership"
# print('p' in text)   #False  
# print('P' in text)   #True



'''  -----------------------String Methods-------------------------------------  '''
s="  Hello world    "

"upper()"
# print(s.upper())

'''lower()'''
# print(s.lower())


'''strip():remove back  space from beginning and ending '''
# print(s.strip())


'''replace(old words, new wordds'''
# print(s.replace("Hello","Python"))

'''split() - convert into list  as string splict '''
# print(s.split())

'''f-String (String Interpolation):f-String let u insert variable directly into string (python-3.6)'''
# name="Alice"
# age=24
# print(f"My name is {name} and i am {age} year old")

'''endwith("word/spelling")'''
# p = '''I am python  because i am high level lang and interpreted and general purpose programming
#       language and emphasize on code readablity with the use of simple and clean syntax'''
# print(p.endswith('tax'))   #True

'''count(string.count("i"))'''
# p = "hey i am python and you i am also py and "
# print(p.count("a"))  #5
# print(p.count("and"))  #2 3

'''capitalize()'''
# a="hello sir"
# print(a.capitalize())  #Hello sir


'''find(word)'''
# a="i am not python "
# print(a.find("am")) #2
# print(a.find("kk")) #-1

'''Escape Sequence Character:
\n-new line
\t-tab
\'-single quote
\\-backslash
etc'''



'''STRING QUIESTION 

-1 Reverse a string without using reverse().
-2 Reverse each word in a sentence.
-3 Check whether a string is palindrome.
-4 Find the longes palindrom in a string.
-5 Count vowels
-6 Count consonants.
-7 Count words in a sentence .
-8 Find dupliate character.
-9 Find the first non-repeating characterr .
-10 Find the first repeating character
-11 Remove duplicate characters. 
-12 Check if two string are anagrams.
-13 Capitalize the first letter of every word
-14 Reverse words in a sentence 
-15 Remove extra spaces.
-16 Find the longest word in a sentence
-17 Find the sortest word 
-18 Count occurrences of a specific character
-19. Check wheter one string is a substring of another 
-20 Compress a string (aabbcc-a3b2c2)
-21 Find all duplicate words in a sentence 
'''