from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


##Tests for get_files_info.py##
"""
t1 = get_files_info("calculator",".")
t2 = get_files_info("calculator", "pkg")
t3 = get_files_info("calculator", "/bin")
t4 = get_files_info("calculator", "../")

print(f"Result for current directory:\n {t1}")
print(f"Result for 'pkg' directory:\n   {t2}")
print(f"Result for '/bin' directory:\n  {t3}")
print(f"Result for '../'' directory:\n  {t4}")


##Tests for get_file_content.py##
t1 = get_file_content("calculator", "main.py")
t2 = get_file_content("calculator", "pkg/calculator.py")
t3 = get_file_content("calculator", "/bin/cat")
t4 = get_file_content("calculator", "pkg/does_not_exist.py")

print(f"{t1}")
print(f"{t2}")
print(f"{t3}")
print(f"{t4}")
"""

t1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
t2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
t3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

print(f"{t1}")
print(f"{t2}")
print(f"{t3}")

