import os

folder = "C:/Users/Ripal/OneDrive/Desktop/Project IGI/Presentation/Literature Review/Research Paper Summery/"

# iterate all files from a directory
for file_name in os.listdir(folder):

    # Construct old file name
    source = folder + file_name

    # Get hold of previous file number
    num = str(file_name[13])
    if file_name[14] != '.':
        num = num + str(file_name[14])

    # Adding the count to the new file name and extension
    final_name = "Paper Summery " + num + ".pdf"
    destination = folder + final_name

    print(f"{file_name} to {final_name}")

    # Renaming the file
    os.rename(source, destination)

print('All Files Renamed')