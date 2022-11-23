import os
FILENAME = '/Users/rupesh2020/python_py/newfile.txt'
file_stats = os.stat(FILENAME)
print("size of file {} is - {} bytes".format(FILENAME, file_stats.st_size))
