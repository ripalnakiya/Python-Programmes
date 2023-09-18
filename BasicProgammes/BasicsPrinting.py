# Will print the frutis in a single line with a space between them.
print("Apple", "Mango", "Grapes")
#Apple Mango Grapes

# Will print the frutis in a single line with a dash between them
# default value for sep is " " (space)
print("Apple", "Mango", "Grapes",sep="-")
print("Thank you")
#Apple-Mango-Grapes
#Thank you

# Will print the "Thank you" in the same line as fruits are printed
# default value for end is 'next line'
print("Apple", "Mango", "Grapes", sep="-", end=":")
print("Thank you") 
#Apple-Mango-Grapes:Thank you



fruit = "grapes"
season = "winter"
print(fruit, "grows in", season)

#format string : we can embed variables inside the string using the format string
print(f"{fruit} grows in {season}")

