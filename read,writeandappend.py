file_read=open('sample.txt','r')
print(file_read.read())
file_read.close()

file_write=open('sample.txt','w')
file_write.write(" I am using write mode so now this will be replacing the original texts")
file_write.close()

file_append=open('sample.txt','a')
file_append.write("This is appending in the text , whatever i wrote in the write one and this will be added not replaced")
file_append.close()
