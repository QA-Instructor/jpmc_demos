# File IO

# open a new file for writing
with open('demo_file.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is a demo file.\n")

# open the file for reading
with open('demo_file.txt', 'r') as f:
    for line in f:
        # print(line)
        print(line.strip())  # strip() removes the newline character


# append to the file
with open('demo_file.txt', 'a') as f:
    f.write("Appending a new line to the file.\n")

    