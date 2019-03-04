#String formatting options

# formatting integers
print("Binary representation of {0} is {0:b}".format(12))

# formatting floats
print("Exponent representation: {0:e}".format(1566.345))

# round off
print("One third is: {0:.3f}".format(1/3))

# string alignment
print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))
