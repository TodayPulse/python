file = open("books.txt", "w")
file.write("The Hunger Games\n")
file.write("The Great Gatsby\n")
file.write("The Maze Runner\n")
file.close()

with open("diary.txt", "w") as file:
    file.write("About Me\n")
    file.write("Yesterday's club\n")
    file.write("All about the sun\n")

with open("diary.txt","r") as output_file:
    with open("books.txt","w") as input_file:

        titles = output_file.read().split("\n")
        titles.sort()

        input_file.write("\n".join(titles))