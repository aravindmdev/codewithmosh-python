import sqlite3
import json
import csv
from zipfile import ZipFile
import shutil
from pathlib import Path
from time import ctime

# # r - raw string - no need to escape the back slash
# Path(r"C:\Program Files\Microsoft")
# Path()  # Current folder
# # will go to the ecommerce sub folder in the current folder
# Path("ecommerce/__init__.py")
# # combine path objects
# Path() / Path("ecommerce")
# # Combine with strings
# Path() / "ecommerce" / "__inti__.py"
# # Gets the home directory of the current user
# Path.home()

# # Path class
# path = Path("ecommerce/__ini__.py")  # Object will have this path
# path.exists()  # checks if the file or folder exist.
# path.is_file()  # checks whether its a file
# path.is_dir()  # checks whether its a directory
# print(path.name)  # file name
# print(path.stem)  # without extension
# print(path.suffix)  # extension alone
# print(path.parent)  # parent folder
# path = path.with_name("file.txt")  # creates a new path
# print(path)
# path = path.with_suffix(".txt")  # creates a new path with extension changed
# print(path)

# path = Path("ecommerce")
# # path.mkdir()
# # path.rmdir()
# # path.rename("ecommerce")

# for p in path.iterdir():
#     print(p)  # will list files and folders

# # the above on in list. Bt returns Posixpath/Windowspath objects
# paths = [p for p in path.iterdir()]

# # to get only the directories.
# paths = [p for p in path.iterdir() if p.is_dir()]

# # .iterdir cannot be used for pattern searching and subfolders
# py_files = [p for p in path.glob("*.py")]  # for pattern searching
# py_files = [p for p in path.rglob("*.py")]  # to search sub folders too

# # Working with files

# path = Path("ecommerce/__init__.py")

# path.unlink()  # remove the file.
# path.stat()  # gets the info of file. the time is platform dependent
# # to get human readable time from time import ctime
# print(ctime(path.stat().st_ctime))

# path.read_bytes()  # read in binary
# path.read_text()  # read and get it in a text
# path.write_bytes("...")  # write in binary
# path.write_text(".....")  # read and get it in a text

# # to copy a file - but not ideal
# source = Path("ecommerce/__init__.py")
# target = Path() / "__init__.py"
# target.write_text(source.read_text())  # copying file but not ideal
# # easy way import shutil
# shutil.copy(source, target)

# # Working with zip files
# # from zipfile import ZipFile

# # create a zip file
# with ZipFile("files.zip", "w") as zip:
#     # gets all the files in ecommerce folder
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)

# # Read and extract from a zip file
# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("ecommerce/__init_.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")  # Extract all the files to the extract folder

# # Working with CSV files
# # import csv
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "product_price"])
#     writer.writerow([1000, 1, 50])
#     writer.writerow([1001, 2, 60])

# with open("data.csv", "w") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# # Working with JSON files
# # import json
# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 12, "title": "Baby's day out", "year": 1990}
# ]
# data = json.dumps(movies)  # converts to JSON data
# Path("movies.json").write_text(data)  # writes to the file

# r_data = Path("movies.json").read_text()
# r_movies = json.loads(r_data)  # converts to array of dictionary
# print(movies[0]["title"])

# Working with SQLite DB
# import sqlite3
# movies = json.loads(Path("movies.json").read_text())
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)

# Working with timestamps
# import time
import time
