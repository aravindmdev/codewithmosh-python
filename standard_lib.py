from pathlib import Path

# r - raw string - no need to escape the back slash
Path(r"C:\Program Files\Microsoft")
Path()  # Current folder

# Path class
path = Path("ecommerce/__ini__.py")  # Object will have this path
path.exists()  # checks if the file or folder exist.
path.is_file()  # checks whether its a file
path.is_dir()  # checks whether its a directory
print(path.name)  # file name
print(path.stem)  # without extension
print(path.suffix)  # extension alone
print(path.parent)  # parent folder
path = path.with_name("file.txt")  # creates a new path
print(path)
path = path.with_suffix(".txt")  # creates a new path with extension changed
print(path)

path = Path("ecommerce")
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce")

for p in path.iterdir():
    print(p)  # will list files and folders
