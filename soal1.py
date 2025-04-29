import os

FILE1 = "nirvana1.txt"
FILE2 = "nirvana2.txt"

def compare_files():
    try:
        with open(FILE1, 'r') as f1, open(FILE2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
        
        max_len = max(len(lines1), len(lines2))
        differences = []
        
        for i in range(max_len):
            line1 = lines1[i].strip() if i < len(lines1) else ""
            line2 = lines2[i].strip() if i < len(lines2) else ""
            
            if line1 != line2:
                differences.append((i+1, line1, line2))
        
        if differences:
            print(f"Differences found between {FILE1} and {FILE2}:")
            for diff in differences:
                print(f"Line {diff[0]}:")
                print(f"  {FILE1}: {diff[1]}")
                print(f"  {FILE2}: {diff[2]}\n")
        else:
            print("Files are identical!")
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Current directory: {os.getcwd()}")
        print("Files in directory:")
        for f in os.listdir():
            print(f"  - {f}")

compare_files()