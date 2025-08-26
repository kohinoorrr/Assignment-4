try:
    file=open("sample.txt",'r+')
    reading_line1=file.readline()
    reading_line2=file.readline()
    print("Reading File Content:")
    print(reading_line1,reading_line2)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
