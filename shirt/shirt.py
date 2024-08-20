# Import required libraries/functions
import sys
from PIL import Image
from PIL import ImageOps
from os.path import splitext

# define function to verify command-line arguments
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        valid_ext = [".jpg", ".jpeg", ".png"]
        in_ext = splitext(sys.argv[1])
        out_ext = splitext(sys.argv[2])
        if in_ext[1] not in valid_ext:
            sys.exit("Invalid input")
        elif out_ext[1] not in valid_ext:
            sys.exit("Invalid output")
        elif in_ext[1] != out_ext[1]:
            sys.exit("Input and output have different extensions")
        else:
            try:
                convert()
            except FileNotFoundError:
                sys.exit("Input does not exist")

# define function to convert image
def convert():
    with Image.open(sys.argv[1]) as photo, Image.open("shirt.png") as shirt:
        size = shirt.size
        photo = ImageOps.fit(photo, size)
        photo.paste(shirt, shirt)
        photo.save(sys.argv[2])

# run main function in the same program
if __name__ == "__main__":
    main()
