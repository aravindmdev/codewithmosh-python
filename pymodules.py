# Module - Group similar kind of methods and classes to one file
# Importing modules
from functions import greet  # give the functions you need to import. Dont give *
import functions  # this is also possible. Access the methods using function object
# when the module is in a sub folder wehave to put a file called __init__.py which willmake it as a package.
# from there we can import
from ecommerce import sales  # or from ecommerce.sales import sales_data
# whenever a file is run, the files which are impoted will be compiled to pycache file

print(dir(sales))  # lists the methods and attributes in the object
