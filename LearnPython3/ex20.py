from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(),  end = "")

current_file = open(input_file, encoding='utf-8')

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tap.")

rewind(current_file)

rewind(current_file)

print("Let's print three lines:")

current_line =1 
print_a_line(current_line, current_file) 
'''readline() 函数返回文件中每行最后的 \n 。
又在 print 函数的结尾加上一个 end = " " 来避免给每行加上两个 \n 。  print(line_count, f.readline(),  end = "") '''

current_line += 1
print_a_line(current_line, current_file,)

current_line += 1
print_a_line(current_line, current_file)

current_file.close()