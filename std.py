import numpy

# sigma σ
# Standard deviation is a number that describes how spread out the values are.
#A low standard deviation means that most of the numbers are close to the mean (average) value.
#A high standard deviation means that the values are spread out over a wider range.
#Example: This time we have registered the speed of 7 cars:
#speed = [86,87,88,86,87,85,86]
#The standard deviation is:
#0.9
#Meaning that most of the values are within the range of 0.9 from the mean value, which is 86.4

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)