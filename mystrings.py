# strings - alphanumeric and symbols.

# lower() - function
# name.lower() - method

first_name = "JohN  "
last_name = "DoE"
first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()
full_name = first_name + " " + last_name
print(full_name)

# Email
email = "john@gmail.com"
print(email.count("@"))

# Length of characters
print(len(first_name) != 0)

#split a string
sent = "This is a laptop"
print(type(sent.split(" ")))

