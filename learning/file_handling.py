try:
# append or edit
# with open("./file/newFile.txt", "a") as file:
# write
    with open("file/newFile.txt", "w") as file:
    # file.write("Welcome to the new lesson")
        file.writelines(["learning awesome stuffs", "\nand its cool here", "wow! i love this"])
except FileNotFoundError as e:
    print("file not found!", e)