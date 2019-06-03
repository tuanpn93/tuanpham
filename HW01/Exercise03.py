s = 'Hi John, welcome to python programming for beginner!'

print('a. Check if "python" exists in s : ', "python" in s)

position = s.find("John")
s1 = s[position:position + 4]
print('b. Extract the word "John" from s : ', s1)

print('c. Count character "o" in s : ', s.count("o"))

print('d. Count how many word s : ', len(s.split()))