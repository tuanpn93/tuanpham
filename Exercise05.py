l = [23, 4.3, 4.2, 31, 'python', 1, 5.3, 9, 1.7]

print('l = [23, 4.3, 4.2, 31, \'python\', 1, 5.3, 9, 1.7]')

l.remove("python")
print('a. Remove item "python" in list : ', l)

l.sort()
print('b. Sort list by ascending : ', l)
l.sort(reverse=True)
print('   Sort list by descending : ', l)

print('c. Check if number 4.2 is in l : ', 4.2 in l)
