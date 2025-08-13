from functions.get_files_info import get_files_info

t1 = get_files_info("calculator",".")
t2 = get_files_info("calculator", "pkg")
t3 = get_files_info("calculator", "/bin")
t4 = get_files_info("calculator", "../")

print(f"Result for current directory:\n {t1}")
print(f"Result for 'pkg' directory:\n   {t2}")
print(f"Result for '/bin' directory:\n  {t3}")
print(f"Result for '../'' directory:\n  {t4}")


