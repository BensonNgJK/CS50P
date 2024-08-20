# Ask user for inputs and convert to string
inputs = str(input("File name: "))

# Remove front/back spaces and lower case
inputs = inputs.strip().lower()

# Convert file extension to media type
if inputs.endswith(".gif"):
    print("image/gif")
elif inputs.endswith(".jpg") or inputs.endswith(".jpeg"):
    print("image/jpeg")
elif inputs.endswith(".png"):
    print("image/png")
elif inputs.endswith(".pdf"):
    print("application/pdf")
elif inputs.endswith(".txt"):
    print("text/plain")
elif inputs.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
