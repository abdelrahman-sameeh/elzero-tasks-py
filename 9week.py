import os
# import json


# # for test

# data = {
#   "name": "abdelrahman",
#   "email": "abdelrahman.sameeh@gmail.com",
#   "state": "cairo",
#   "phone": "15"
# }

# file = open(os.path.join(os.getcwd(), 'test', 'python', f"{data.get('email')}.json"), 'a')
# json.dump(data, file, indent=2)
# file.close()

# try:
#   print('data')
#   os.remove(os.path.join(os.getcwd(), 'test', 'python', f"{data.get('email')}.json"))
# except Exception as err:
#   print(f'{err}')



# ------------------------------------ start tasks ------------------------------------

# # myFile=open('/home/abdelrahman/Desktop/python/assign.py', 'a')

# # for num in range(50):
# #   if num < 10:
# #     num = str(num+1).zfill(2)
# #   print(f'File {num} Created')
# #   if num!=50:
# #     file=open(f'/home/abdelrahman/Desktop/python/txt{num}.txt', 'a')
# #     file.write('this is a normal file')
# #     file.close()
# #   else:
# #     file=open(f'/home/abdelrahman/Desktop/python/special-file.txt', 'a')


# # myFile.close()

# # get current working directory 
# print(os.getcwd())
# # get path of current file
# print(os.path.abspath(__file__))
# # get path of directory of current file
# print(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------------------------------------

# file = open('/home/abdelrahman/Desktop/python/txt01.txt', 'a')
# for num in range(51):
#   file.write('\nAppended => Elzero Web School')


# ------------------------------------------------------------------------


# try:
#   file = open('/home/abdelrahman/Desktop/python/txt01.txt', 'r')
#   print(len(file.readlines()))
#   file.close()
  
#   file = open('/home/abdelrahman/Desktop/python/txt01.txt', 'r')
#   print(len(file.read().split()))
#   file.close()
  
#   file = open('/home/abdelrahman/Desktop/python/txt01.txt', 'r')
#   print(len(file.read()))
#   file.close()
  
#   file = open('/home/abdelrahman/Desktop/python/txt01.txt', 'r')
#   print(file.read().count('l'))
#   file.close()

# except Exception as e:
#   print(e)

