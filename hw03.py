"""
Name: Shameen Shetty
ID	: 1001429743
"""

import numpy as np


def calcAsciiVal(bitArray):
    count = 7
    asciiValue = 0
    for bit in bitArray:
        if bit == 0:
            result = 0
        if bit == 1:
            result = np.power(2, count)
        asciiValue += result
        count -= 1
    return asciiValue

pulse0 = np.ones(10)
pulse1 = np.append(np.ones(5), -1 * np.ones(5))


"""
We get all the data from the file data-communications.csv and store it in 
csvData, where we do not assign a type to item.
""" 
fileName = "data-communications.csv"
csvData = np.genfromtxt(fileName, dtype=None, delimiter=",")

data = np.reshape(csvData, (-1, 10))
"""
for the above line of code we are reshaping the shape of the data from (x,)
(i.e a 1D array) to an array with unknown number of rows (-1) and 10 cols (10)
hence the (-1, 10)
"""

length = data.shape[0]
for i in range(length):
    word = data[i,:]

    """
    For the below code we will be taking cosine theta of the two vectors,
    theta_alpha is the angle between the digits and pulse0, while theta_alpha is
    the angle between the digits and pulse1. If alpha < beta, then we assign the
    data value as pulse0, otherwise is beta < alpha, it is pulse1 instead.
    """
    
    data_norm = np.linalg.norm(word)
    pulse0_norm = np.linalg.norm(pulse0)
    pulse1_norm = np.linalg.norm(pulse1)
    
    theta_alpha = np.cos(np.dot(word, pulse0) / (data_norm * pulse0_norm))
    theta_beta = np.cos(np.dot(word, pulse1) / (data_norm * pulse1_norm))
    
    minimum = np.min([theta_alpha, theta_beta])
    
    if minimum == theta_alpha:
        data[i] = pulse0
    if minimum == theta_beta:
        data[i] = pulse1


newLength = int(length/8)
bitArray = []
message = []
"""
For the below nested for loop we break it into lines of 8 (so we can get 8 bits
of data), and append the value into bitArray (if pulse0, then 0 or 1 otherwise)
Then we enter the bitArray into calcAsciiVal which gets the decimal val of the 
8-bit num, and use chr() to convert it to a character, then we use .clear() to
remove all the numbers from the bitArray, so we can add the next 8 bits into it
"""
counter = 0
for i in range(newLength):
    for j in range(8):
        if np.array_equal(data[counter], pulse0) is True:
            bitArray.append(0)
        if np.array_equal(data[counter], pulse1) is True:
            bitArray.append(1)
            
        counter += 1
    character = chr(calcAsciiVal(bitArray))
    message.append(character)
    bitArray.clear()

print("".join(message))