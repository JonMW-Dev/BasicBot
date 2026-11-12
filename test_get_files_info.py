# test_get_files_info.py | Date: 12-11-2026 | Author: Jonathan Windle

from functions.get_files_info import get_files_info
def main():
	print("Testing: \"calculator\", \".\" ")
	print(f"\t{get_files_info("calculator", ".")}\n") # expect valid

	print("Testing: \"calculator\", \"pkg\" ")
	print(f"\t{get_files_info("calculator", "pkg")}\n") # expect valid

	print("Testing: \"calculator\", \"/bin\" ")
	print(f"\t{get_files_info("calculator", "/bin")}\n") # expect valid

	print("Testing: \"calculator\", \"../\" ")
	print(f"\t{get_files_info("calculator", "../")}\n") # expect valid
	
	# tests expected to fail
	# print("Testing: \"calculator\", \"/bin\" ")
	# print(f"\t{get_files_info("calculator", "/bin")}\n")

	# print("Testing: \"calculator\", \"../\" ")
	# print(f"\t{get_files_info("calculator", "../")}\n")

	# print("Testing: \"calculator\", \"main.py\" ")
	# print(f"\t{get_files_info("calculator", "main.py")}\n")

	# print(f"\nAll tests passed")
	
	return 

main()

