# Test driver for run_python_file.py module
from functions.run_python_file import run_python_file
def main():
    print("Testing run_python_file.py module")

    result = run_python_file("calculator", "main.py")
    print(f"run_python_file result: {result}\n")

    run_python_file("calculator", "main.py", ["3 + 5"]) #(should run the calculator... which gives a kinda nasty rendered result)
    print(f"run_python_file result: {result}\n")
    run_python_file("calculator", "tests.py") #(should run the calculator's tests successfully)
    print(f"run_python_file result: {result}\n")
    run_python_file("calculator", "../main.py") #(this should return an error)
    print(f"run_python_file result: {result}\n")
    run_python_file("calculator", "nonexistent.py") #(this should return an error)
    print(f"run_python_file result: {result}\n")
    run_python_file("calculator", "lorem.txt") #(this should return an error)



    return

main()
