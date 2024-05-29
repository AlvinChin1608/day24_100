# day24_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner stage and later on intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

---------

**Enhancing the Snake Game with File Operations**
In my Snake Game project, I have added the capability to open and write to a file to track the high score. This enhancement ensures that the game can store and retrieve the highest score achieved, even after the game is closed and reopened. Here’s a brief snippet demonstrating this feature:
```python
def update_high_score(new_score):
    with open('high_score.txt', 'w') as file:
        file.write(str(new_score))
```
By integrating file operations into the game, players can enjoy a more engaging experience with persistent high scores.

-----------

**Files in Python**
Python allows you to open, read, write, and close files using built-in functions. Whether you're dealing with text files or binary files, Python provides a straightforward interface to handle file operations. Here’s a simple example of how to open a file for reading:
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```
In this example, the with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.

**Absolute vs Relative Paths**
Paths specify the location of files or directories in the file system. There are two types of paths:

- Absolute Path: An absolute path provides the complete location of a file or directory from the root of the file system. It is independent of the current working directory.
```python
absolute_path = '/home/user/documents/example.txt'

```
- Relative Path: A relative path specifies the location of a file or directory in relation to the current working directory. It is shorter and more portable than an absolute path.
```python
relative_path = 'documents/example.txt'
```
