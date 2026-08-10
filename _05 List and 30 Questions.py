'''List :   is a collection of ordered , mutable item . it allow duplicates . create a list using squre braces[]

             
append(x)-
extend(iterable)- multiple item add
insert(i,x)- add at index
remove(x)- remove value
pop()- last item remove
pop(i)- index item remove
clear()0 
sort()
reverse()
index(x)
count(x)
 copy'''


# l1=[1,8,7,2,21,15]

# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

# l1.append(0)
# print(l1)

# l1.pop()
# l1.pop(2)
# print(l1)

# l1.remove(2)
# print(l1)

# print(l1.count(15))

# print(l1.index(15))
# print(l1.index(15,0))


# ddt = ["hello",11,1.2,True]
# print(ddt)

# l1.extend([20,30])
# print(l1)

'''
jo method list ko badalta hai- append,extend,insert, remove, clear, sort, reverse

jo method information ya koi item deta hai-  pop, index, count, copy

note- pop() ek exception hai - ye list ko modify bhi karta hai aur removed element ko return bhi karta hai '''


'''30 QUESTIONS
1 What happen when you do list1 = list2?
2 Difference between shallow copy and deep copy.
3 Find the largest element in a list 
4 Find the smallest element in a list
5 Find the second largest element in a list 
6 Find the second smallest element in a list 
7 Rever a list 
8 Removes duplicate
9 Count frequency of each element 
10 Find duplicate element 
11 Check wheter an element exists.
12 Sort a list in ascending order
13 Sort a list in descending order 
14 Merge two list 
15 Find common elements between two list 
16 Sum of all elements
17 Find odd numbers
18 Find even numbers
19 Remove all even number 
20 Find maximum repeated element

List Comprehension Question 
21 . Create a list of squares
22 Create a list of even number
23 Convert all strings to uppercase 
24 Remove empty string from a list


25 Reverse a list without using reverse()
26 Remove duplicate without using  set()
27 Find the second largest number 
'''

'''Q-1 What happen when you do list1 = list2?'''

'''"list1 = list2 creates a new reference to the same list object. It does not create a new copy of the list. Therefore, any modification made through one variable is reflected in the other. If a separate copy is required, use list2.copy() or slicing (list2[:])."
eg.
list2 = [10, 20, 30]
list1 = list2
list1.append(40)
print(list1)
print(list2)

[10, 20, 30, 40]
[10, 20, 30, 40]



list2 = [10, 20, 30]
list1 = list2.copy()
list1.append(40)
print(list1)
print(list2)

[10, 20, 30, 40]
[10, 20, 30]

'''

'''Q-2 Difference between shallow copy and deep copy'''


'''Q- 3 Find the largest element in a list '''

# list = [30,25,7,42,15]
# largest = list[0]
# for i in list:
#     if i>largest:
#         largest=i
# print("Largest number of list is : ",largest)

'''Q- 4 Find the smallest element in a list'''
# list = [30,25,7,42,15]
# smallest = list[0]
# for i in list:
#     if i<smallest:
#         smallest=i
# print(smallest)




'''Q-5 Find the second largest element in a list '''

# list = [30,25,7,42,15]
# largest = second_largest =  float('-inf') # or list[]

# for i in list:
#     if i>largest:
#         second_largest = largest
#         largest = i
#     elif i>second_largest and i!=largest:
#         second_largest = i
    
# print(second_largest)
# print(largest)

'''Q-6 Find the second smallest element in a list '''
# li = [30,25,7,42,15]
# smallest = sec_smallest = float('inf')

# for i in li:
#     if i<smallest:
#         sec_smallest = smallest
#         smallest=i
#     elif i<sec_smallest and smallest!=i:
#         sec_smallest=i
# if sec_smallest == float('inf'):
#     print("There is no second smallest element.")
# else:
#     print("Second smallest element is:", sec_smallest)


'''Q-7 Reverse a list '''
# li = [30,25,7,42,15]
# li.reverse()
# print(li)

# Alternative way to reverse a list without using reverse()
# li = [30,25,7,42,15]
# reversed_li = li[::-1]
# print(reversed_li)


'''Q-8 Removes duplicate'''
# li = [30,25,7,42,15,7,30,25,42,30,25]
# unique_li = []

# for i in li:
#     if i not in unique_li:
#         unique_li.append(i)

# print(unique_li)


'''Q-9 Count frequency of each element'''
# li = [30,25,7,42,15,7,30,25,42,30,25]
# freq = {}
# for i in li:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)



'''Q-10 Find duplicate element'''

# li = [30,25,7,42,15,7,30,25,42,30,25]
# freq = {}
# for i in li:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)
# duplicate = []
# for key,value in freq.items():
#     if value>1:
#         duplicate.append(key)
# print(duplicate)

'''Q-11 Check whether an element exists.'''


