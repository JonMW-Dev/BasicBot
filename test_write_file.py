# test driver for the write_file.py module
from functions.write_file import write_file
def main():
    print("Testing write_file.py module")

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"write_file result: {result}\n")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"write_file result: {result}\n")
    result = write_file("calculator", "/tmp/temp.text", "this should not be allowed")
    print(f"write_file result: {result}\n")

    return

main()
