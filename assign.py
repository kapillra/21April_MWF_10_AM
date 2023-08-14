s = ''
for i in range(65, 91):
    s+=chr(i)
print(s)

l = []
start = 0
stop = 3
string = ''

for i in range(len(s)):
    
    if len(l) <= (len(s) // 3):
        l.append(s[start:stop]+'\n')
        start = stop
        stop = stop + 3
else:
    f = open('file.txt', 'w')
    f.writelines(l)

print(l)

# while True:
#     if len(string) // len(s) < 5:
#         string += s[start:stop]
#         start = stop
#         stop = stop + 4
#     else:

#         break
# print(string)

# with open("new_file.txt", 'a+') as file:
#     s = ''
#     for i in range(65, 91):
#         s+=chr(i)

#     l = []
#     start = 0
#     stop = 3
#     string = ''

#     for i in range(len(s)):
#         if len(l) <= (len(s) // 3):
#             file.write(s[start:stop]+'\n')
#             start = stop
#             stop = stop + 3