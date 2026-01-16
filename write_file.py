file = open("sample.txt", "w")

text = input("Enter text to write into file:\n ")
file.write(text)

file.close()
print("File written successfully")
