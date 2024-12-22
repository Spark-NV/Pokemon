import os

# Set the path to the folder containing your images
folder_path = "C:\\Users\\Spark\\Desktop\\f\\Pokemon\\imagesHQ"

# Base URL for the GitHub repository
base_url = "https://github.com/Spark-NV/Pokemon/blob/main/imagesHQ/"

# Create or open the links.txt file to write the links
with open("links.txt", "w") as file:
    # Iterate through all the files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image (you can expand the extensions as needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Write the formatted URL to the file
            file.write(f"{base_url}{filename}?raw=true\n")

print("links.txt has been generated successfully!")
