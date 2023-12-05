

##      Concatenation - Joining two or more strings      ##
str1 = "Hello, "
str2 = "World!"
combined_str = str1 + str2
print(combined_str)
# Output: "Hello, World!"


##      Slicing - Extracting a part of a string:      ##
str = "Hello, World!"
sliced_str = str[7:12]
print(sliced_str)
# Output: "World"


##      Splitting a String - Breaking a string into a list of substrings      ##
str = "one,two,three"
split_str = str.split(",")
print(split_str)  # Output: ['one', 'two', 'three']


##      Reversing a String      ##
str = "Hello"
reversed_str = str[::-1]
print(reversed_str)
# Output: "olleH"


##      Replacing text      ##
str = "H e l l o N o S p a c e s"
str.replace(' ', '')
# Output: "HelloNoSpaces"


##      Joining a List of Strings      ##
words = ["Hello", "World"]
joined_str = "<3".join(words)
print(joined_str)
# Output: "Hello<3World"


##      Uppercase/Lowercase Conversion      ##
str = "Hello, World!"
print(str.lower())
# Output: "hello, world!"
print(str.upper())
# Output: "HELLO, WORLD!"


##      Replacing Substrings      ##
str = "Hello, World!"
replaced_str = str.replace("World", "Python")
print(replaced_str)
# Output: "Hello, Python!"


##      Stripping Whitespace (from both ends of a string)      ##
str = "   Hello, World!   "
stripped_str = str.strip()
print(stripped_str)
# Output: "Hello, World!"


##      Checking if a String Starts/Ends With a Substring      ##
str = "Hello, World!"
print(str.startswith("Hello"))
# Output: True
print(str.endswith("Python"))
# Output: False


##      Finding Substrings      ##
str = "Hello, World!"
index = str.find("World")
print(index)
# Output: 7


##      Counting Occurrences of a Substring      ##
str = "hello hello world"
count = str.count("hello")
print(count)
# Output: 2