# convert string hex color to int RGB tuple

# "#a325e9"
# (163, 37, 233)

def main():
    color = input("Enter the Hex code: ")
    rgb = convert(color)
    print(f"RGB value is {rgb}")

def convert(color):
    c1 = color[1:3] # Slicing the color
    c2 = color[3:5]
    c3 = color[5:7]

    #The int(a, 16) converts a string of hex value to integer value
    r = int(c1, 16)
    g = int(c2, 16)
    b = int(c3, 16)

    rgb = (r, g, b) # Creating a tuple of individual RGB values
    return rgb


if __name__ == "__main__":
    main()