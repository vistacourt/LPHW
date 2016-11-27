# 2016 vistacourt software
# tom kelly



def convert_temp():
    Celsius = int(raw_input("Enter a temperature in Celsius: "))
    Fahrenheit = 9.0/5.0 * Celsius + 32
    print "Temperature:", Celsius, "Celsius = ", Fahrenheit, " F"

convert_temp()
