import os

folder_path = input(" Enter the folder path where your .txt files are stored: ").strip()

if not os.path.isdir(folder_path):
    print(" The folder path you entered does not exist. Please check and try again.")
    exit()

files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

if not files:
    print("No .txt files found in the given folder.")
    exit()

files.sort()

print("\n Existing .txt files in the folder:")
for i, file in enumerate(files, start=1):
    print(f"{i}. {file}")

try:
    choice = int(input("\n Enter the number of the file you want to rename: "))
    if choice < 1 or choice > len(files):
        print("Invalid choice. Please run the script again.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

selected_file = files[choice - 1]

new_name = input(f"✏ Enter the new name for '{selected_file}' (without extension): ").strip()
if not new_name:
    print("New name cannot be empty.")
    exit()

new_name = f"{new_name}.txt"

old_path = os.path.join(folder_path, selected_file)
new_path = os.path.join(folder_path, new_name)

if os.path.exists(new_path):
    print(f"A file named '{new_name}' already exists. Rename aborted.")
else:
    os.rename(old_path, new_path)
    print(f"File renamed: {selected_file} → {new_name}")
