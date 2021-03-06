# 2016 vistacourt software
# tom kelly

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Texas': 'TX'
}
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'NY': 'New York',
    'OR': 'Portland',
    'TX': 'Texas'
}



print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Cali has: ", cities[states['California']]

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
