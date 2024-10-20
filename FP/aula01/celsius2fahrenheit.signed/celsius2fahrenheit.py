# Write a program that reads a temperature in degrees Celsius,
# converts it to Fahrenheit, and shows the result like this:
#     XX ºC = YY ºF
# where XX and YY are the temperatures in Celsius and Fahrenheit, respectively.
#
# The conversion formula is:  TF = 1.8 TC + 32, where TC and TF are
# the temperatures in Celsius and in Fahrenheit, respectively.

TC = float(input("Temperature (ºC)? ")) 
TF = 1.8*TC + 32
print(TC ,"ºC =", TF ,"ºF")


