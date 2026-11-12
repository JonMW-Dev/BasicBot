# tests the get_file_content.py module
from functions.get_file_content import get_file_content
def main():
    print("Testing lorem.txt in calculator")
    
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}\n")


    result = get_file_content("calculator", "main.py")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}\n")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}\n")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}\n")
    print(result)
    
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}\n")
    print(result)




main()