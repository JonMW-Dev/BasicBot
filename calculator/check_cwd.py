import os
print("CWD:", os.getcwd())
print("Contents of CWD:")
for item in sorted(os.listdir(".")):
    print(" ", item, "(dir)" if os.path.isdir(item) else "(file)")
