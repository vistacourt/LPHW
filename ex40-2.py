# 2016 vistacourt software
# tom kelly
class Song(object):

    def __init__(self, celcius):
        self.celcius = celcius
##
##    def sing_me_a_song(self):
##        for line in self.lyrics:
##            print line

##happy_bday = Song(["Happy birthday to you",
##                   "I don't want to get sued",
##                   "So I'll stop right there"])
##
##bulls_on_parade = Song(["They rally around tha family",
##                        "With pockets full of shells"])
##
##happy_bday.sing_me_a_song()
##
##bulls_on_parade.sing_me_a_song()


    def convert_temp(self):
        self.celsius = int(raw_input("Enter a temperature in Celsius: "))
        Fahrenheit = 9.0/5.0 * self.celsius + 32
        print "Temperature:", self.celsius, "Celsius = ", Fahrenheit, " F"

temp = Song()
temp.convert_temp()
