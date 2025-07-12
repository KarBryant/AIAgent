# tests.py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from functions import get_file_content


#print(get_file_content("calculator", "main"))
#print(get_file_content("calculator","lorem.txt"))


#print(get_files_info("calculator", "."))
#print(get_files_info("calculator", "pkg"))
#print(get_files_info("calculator", "/bin"))
#print(get_files_info("calculator", "../"))

print(get_file_content(".", "main.py"))
print(get_file_content(".", "pkg/calculator.py"))
print(get_file_content(".", "/bin/cat"))