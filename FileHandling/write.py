# f = open(r"C:\Users\Rishab Raj\Desktop\Python3\FileHandling\demo.txt","w")
# # f.write("Hello, World!")
# # f.write("\n Welcome to Delhi!")
# f.write("\n Thrilling adventure to Noida!")

# f.close()

# r+ = read and write mode (Overwrite from starting of the file)
# w+ = write and read mode (overwrites the file)
# a+ = append and read (does not overwrite the file) End of the file
# f = open(r"C:\Users\Rishab Raj\Desktop\Python3\FileHandling\demo.txt","a+")
# f.write("abc")
# f.close()



# With Syntax
with open(r"C:\Users\Rishab Raj\Desktop\Python3\FileHandling\demo.txt","a") as f:
  # data = f.read()
  f.write("\nAppending the word.")
  # print(data)