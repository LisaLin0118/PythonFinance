
#2string.py

# 2.1 Strings
# HINT: https://www.w3schools.com/python/python_strings.asp

txt = "Merry Christmas"


# 2.1.1 print the length of the string
# TODO: Write your code below

len(txt)

# 2.1.2 Print the first character of the string txt.
# TODO: Write your code below

print(txt[0])

# 2.1.3 Get the characters from index 1 to index 3 (err).
# TODO: Write your code below

print(txt[1:4])

# 2.1.4 Convert the value of txt to upper case and print it.
# TODO: Write your code below

upper_string = txt.upper()
print(upper_string)

# 2.1.5 Convert the value of txt to lower case and print it.
# TODO: Write your code below

lower_string = txt.lower()
print(lower_string)

# 2.1.6 Return the string without any whitespace at the beginning or the end.
x = " Hello World "
# TODO: Write your code below

nowhitespace_left = x.lstrip()
nowhitespace_right = x.rstrip()

print(nowhitespace_left)   
print(nowhitespace_right) 

# 2.1.7 Replace the character H with a J and print the result
y = "Hello"
# TODO: Write your code below

new_string = y.replace("H", "J")
print(new_string)


# 2.1.8 Insert the correct syntax to add a placeholder for the name parameter.
# TODO: Update the code below
name = 'John'
txt = "My name is {}"
print(txt.format(name))
