myweek = ["mon","tue", "wed", "thur", "fri", "sat", "sun"]

myweek.append("holiday")
add_list = ["christmass","Easter","good_friday"]
myweek.extend(add_list)
myweek.insert(2,"jamuhuri")
myweek.remove("mon")
myweek.reverse()
# display fri
print(myweek[4])
# remove jamuhuri and display days of the week
myweek.pop(9)
myweek.insert(6,"mon")
print(myweek[3:7])



 






print(myweek)
print(type(myweek))

