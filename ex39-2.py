# 2016 vistacourt software
# tom kelly

names = {
    'Tom Kelly': 'TK',
    'Tessie Zimmerman': 'TZ',
    'Zack Zimmerman': 'ZZ',
}

birthday = {
    'TK': '02/23/1969',
    'TZ': '09/7/1965',
    'ZZ': '11/06/1995'
}



print '-' * 10
print "TK's birthday is: ", birthday['TK']
print "TZ's birthday is: ", birthday['TZ']
print "ZZ's birthday is: ", birthday['ZZ']

print '-' * 10
print "Tom Kelly's initials are: ", names['Tom Kelly']
print "Tessie Zimmerman's initials are: ", names['Tessie Zimmerman']
print "Zack Zimmerman's initials are: ", names['Zack Zimmerman']

print '-' * 10
print "Tom Kelly's burthday is: ", birthday[names['Tom Kelly']]
print "Tessie Zimmerman's birthday is: ", birthday[names['Tessie Zimmerman']]
print "Zack Zimmerman's birthday is: ", birthday[names['Zack Zimmerman']]


print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for x, y in states.items():
        print  "%s %s" % (x, y)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
        
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])



print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
