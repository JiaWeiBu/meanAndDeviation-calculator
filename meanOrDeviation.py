'''
MIT License

Copyright (c) 2021 JiaWeiBu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from math import sqrt
import collections

#sum of x
def sigmaX(a): # a is a list
    #start counter per list
    c = 0
    for x in range(len(a)):
        c += a[x]
    
    return c

#sum of fx
def sigmaFX(a,b): # a and b is a list
    c = 0
    for x in range(len(a)):
        c += (a[x] * b[x])
    
    return c

#data x input
def dataXinput(allX):
    #how many value
    try: 
        n = int(input('Number of input(N): '))
    
        #get all the value
        for a in range(n):
            c = float(input(f'What is the {a + 1} value: '))
            allX.append(c)
    
        #all x in list and the n
        return [allX,n]
    except ValueError:
        restart = input('Error: Number of input must be integer, The data value must be a float , Press enter to restart the programme')
        main()
        
        
    

#get data input
def meanDataInput(allM,allF):
    try:
        #input
        #what is the frequency
        r = int(input('Number of row of data: '))

        #get all the value
        for a in range(r):
            c = float(input(f'What is the {a + 1} value of x: '))
            allM.append(c)
    
        for a in range(r):
            c = int(input(f'WHat is the {a+1} frequency of f: '))
            allF.append(c)
    
        return [allM,allF]
    except ValueError:
        restart = input('Error: Row and frequency must be integer, The data value must be a float , Press enter to restart the programme')
        main()

#meanUngroup
def meanUngroup(x,n):
    #mean calculation
    sumX = sigmaX(x)
    z = sumX/n
    
    print(f"The mean is {z:.4f}")
    
    #return the list of x and n and z is the mean
    return [x,n,z]

#meanGroup
def meanGroup(a,b):
    #mean calculation
    sumFX = sigmaFX(a,b)
    sumF = sigmaX(b)
    z = sumFX/sumF
    
    print(f"The mean is {z:.4f}")
    
    #return the list of a is midpoint list, b is frequency list z is the mean
    return [a,b,z]

#mean display
def dataMean():
    #input for ungroup or group
    dataType = 0

    #validate input data
    while dataType != 'g' and dataType != 'u':
        dataType = input('Is your data group (g) or ungroup (u): ')

    if dataType == 'g':
        allM = []
        allF = []
        k = meanDataInput(allM,allF)
        x = meanGroup(k[0],k[1])
    else:
        #input
        allX = []
        y = dataXinput(allX)
        x = meanUngroup(y[0],y[1])
    
    x.append(dataType)
    #for group data x[0] is midpoint list, x[1] is frequency list, x[2] is mean, x[4] is data type string
    return x
        
#deviation
#sum of fx^2
def sigmaFX2(a,b): # a and b is a list
    c = 0
    for x in range(len(a)):
        c += (a[x] * a[x] * b[x])
    
    return c

#sum of fx square
def sigmaF2X2(a,b):
    c = 0
    for x in range(len(a)):
        c += (a[x]*b[x]) * (a[x]*b[x])
    
    return c

#sum of F(m-mean)
def sigmaXminusMean(a,b): # a is list of x , b is the mean #the output is square
    c=0
    for x in range(len(a)):
        c += ((a[x]-b) * (a[x]-b))

    return c

#sum of F(m-mean)
def sigmaFMminusMean(a,b,d): # a is list of x , b is the mean #the output is square
    c=0
    for x in range(len(a)):
        c += (d[x] * (a[x]-b) * (a[x]-b))

    return c

#deviation
def deviation():
    #input for ungroup or group
    dataTypes = 0

    #validate input data
    while dataTypes != 'p' and dataTypes != 's':
        dataTypes = input('Is your data population (p) or sample(s): ')
    
    if dataTypes == 's':
        mean = dataMean()
        if mean[3] == 'u':
            #calculation
            fMinusX = sigmaXminusMean(mean[0],mean[2])
            median = (mean[1]+1)/2
            variance = fMinusX/(mean[1]-1)
            sDeviation = sqrt(variance)
            print(f'The data input is {mean[0]}\nWith N = {mean[1]}\nThe median is {median:.4f}\nThe mode is {[item for item,count in collections.Counter(mean[0]).items() if count > 1]}\nThe variance is {variance:.4f}\nThe standard deviation is {sDeviation:.4f}')
        else:
            #calculation
            fMinusX = sigmaFMminusMean(mean[0],mean[2],mean[1])
            sumFrequency = sigmaX(mean[1])
            sumF2x2 = sigmaF2X2(mean[0],mean[1])
            sumFx2 = sigmaFX2(mean[0],mean[1])
            mode = max(mean[1])
            median = (sumFrequency)/2
            variance = fMinusX/(sumFrequency-1)
            sDeviation = sqrt(variance)
            print(f'The data input is {mean[0]}\nWith Frequency list: {mean[1]}\nThe median is {median:.4f}\nThe modal class has frequency of {mode}\nSum of F is {sumFrequency}\nSum of FX is {fMinusX:.4f}\nSum of f(m-mean) is {fMinusX:.4f}\
\n(Sum of fm)square is {sumF2x2:.4f}\nSum of F*(x)square is {sumFx2:.4f}\nThe variance is {variance:.4f}\nThe standard deviation is {sDeviation:.4f}')
    else:
        mean = dataMean()
        if mean[3] == 'u':
            #calculation
            fMinusX = sigmaXminusMean(mean[0],mean[2])
            median = (mean[1]+1)/2
            variance = fMinusX/(mean[1])
            sDeviation = sqrt(variance)
            print(f'The data input is {mean[0]}\nWith N = {mean[1]}\nThe median is {median:.4f}\nThe mode is {[item for item,count in collections.Counter(mean[0]).items() if count > 1]}\nThe variance is {variance:.4f}\nThe standard deviation is {sDeviation:.4f}')
        else:
            #calculation
            fMinusX = sigmaFMminusMean(mean[0],mean[2],mean[1])
            sumFrequency = sigmaX(mean[1])
            sumF2x2 = sigmaF2X2(mean[0],mean[1])
            sumFx2 = sigmaFX2(mean[0],mean[1])
            mode = max(mean[1])
            median = (sumFrequency)/2
            variance = fMinusX/(sumFrequency)
            sDeviation = sqrt(variance)
            print(f'The data input is {mean[0]}\nWith Frequency list: {mean[1]}\nThe median is {median:.4f}\nThe modal class has frequency of {mode}\nSum of F is {sumFrequency}\nSum of FX is {fMinusX:.4f}\nSum of f(m-mean) is {fMinusX:.4f}\
\n(Sum of fm)square is {sumF2x2:.4f}\nSum of F (x)square is {sumFx2:.4f}\nThe variance is {variance:.4f}\nThe standard deviation is {sDeviation:.4f}')
     

def main():     
    #validate input data
    dataTapes = 0
    while dataTapes != 'm' and dataTapes != 'd':
        dataTapes = input('Is your data mean (m) or deviation(d): ')

    if dataTapes == 'd':
        deviation()
    else:
        dataMean()

    #display value
    temp = input('Press enter to quit the calculation')
    quit()
    
if __name__ == '__main__':
    main()
