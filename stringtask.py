# Clean up the following variable to give the
#  clean version in lower case. Using inbuilt
#  methods in the str class 
# name = “  JOHn  .“ to “john”

name = "JOHn"
name = name.lower()
print(name)

# Slice the below string to get you the resulting sentence:
# sentence_one = “The Dog Breed is German Shepherd” only display
# “Breed is German”
# sentence_two = “Defeats for the Clinton forces, this was her
# moment of triumph” only display “Clinton forces”

text = "The Dog Breed is German Shepher"
print(text[8:23])

txt = "Defeats for the Clinton forces"
print(txt[16:30])

# Split the below sentence using a semicolon i.e ;
# And display length of the result. 
# “The lazy dog; ran so fast; it hit the wall.” 

txt = "The lazy dog; ran so fast; it hit the wall"

x = txt.split(";")
print(x)

# first_name="  Joh.n"  last_name="  
# Do,e" Clean up and display Full name i.e John Doe

first_name = "  Joh.n"
last_name = "   Do,e"
first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()
full_name = first_name + " " + last_name 
print(full_name)

# Having the string r = '["E","W","C"]' #Manipulate it to display EWC

r = '["E","W","C"]'
print("".join(r))



