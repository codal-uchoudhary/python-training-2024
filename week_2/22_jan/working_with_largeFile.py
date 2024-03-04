# we take a chunk of source file and write in the file2


source_file = open("demo4.txt", "r")  # source file (big text file)
#
file2 = open("write.txt", "w")

chunk_size = 10 * 10

while True:
    chunk = source_file.read(chunk_size)
    if not chunk:
        break
    file2.write(chunk)
    file2.write("___________")
