"""
Here is method 1

whenever you open a file, you need to close it.
So it will not use unnecessary resource
"""

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

"""
Method 2

using a different way to open the file using "with"
so it automatically close when we are done

essentially the same as above and we dont have to
remember to close it. 
"""
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# To write
"""
The open mode by default is set to read only mode, so we cannot write

To fix this, we need change the mode to w (write), the w will delete and replace with the new text
"""
# with open("my_file.txt", mode = "w") as file:
#     file.write("New text.")

"""
But let's say we do not want to delete and write, just want to add to it, 
then, change mode from "w" to "a" as append
"""

with open("my_file.txt", mode = "a") as file:
    file.write("\nNew text.")

"""
NOTE: if you open a file that does not exist, it will automatically create for you
But it ONLY works when you are in the "w" write mode
"""

with open("../new_file.txt", mode = "w") as file:
    file.write("\nNew text.")

"""
File path directory
- Absolute Path (this comes from naming where the root storage
(/Users/alvinchin/Desktop/Pycharm/.... etc) similar to how I cd using Terminal


- Relative path (from working directory, ../new_file.txt is to move one step forward 
2 level forward would be ../../
and my_file.txt because we are working in the same directory)
"""