
import sys

# Exit and print an error message if user does not specify a name.
if len(sys.argv) < 2:
    print("Error: Missing NAME. Please run as 'python question10.py <NAME>`")
    sys.exit(1) 

# Define NAME and print statement.
NAME = sys.argv[1] 
print(f"Hello {NAME}")