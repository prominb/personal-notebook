
# list1 = ['Вася', 'Петя', 'Маша', 'Саша', 'Петя']
# list2 = ['Вася', 'Петя']

# set1 = set(list1)
# set2 = set(list2)
# list3 = list( set1.difference(set2) )
# print(list3)


engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers           # union
engineering_management = engineers & managers            # intersection
fulltime_management = managers - engineers - programmers # difference
print (fulltime_management)