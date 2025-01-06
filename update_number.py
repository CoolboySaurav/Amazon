#!/usr/bin/env python3
import os
import subprocess
from datetime import datetime

# Get the directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def read_number():
    """Reads the current number from number.txt."""
    with open('number.txt', 'r') as f:
        return int(f.read().strip())

def write_number(num):
    """Writes the updated number to number.txt."""
    with open('number.txt', 'w') as f:
        f.write(str(num))

def git_commit_and_push():
    """Commits and pushes changes to GitHub."""
    # Stage the changes
    subprocess.run(['git', 'add', 'number.txt'], check=True)

    # Create commit with current date
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    commit_message = f"Update number: {date}"
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)

    # Push the committed changes to GitHub
    subprocess.run(['git', 'push'], check=True)

def main():
    try:
        # Read, update, and write the number
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)

        # Commit and push the changes
        git_commit_and_push()

        print(f"Number successfully updated to {new_number}.")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
