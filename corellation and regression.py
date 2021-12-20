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

def Sxx(dataPair):
    x,y,xy,xx,yy,n = dataPair
    sxx = xx - (x*x)/n
    print(f'S_XX = {xx} - {x}^2/{n} = {sxx:.4f}')
    return sxx

def Syy(dataPair):
    x,y,xy,xx,yy,n = dataPair
    syy = yy - (y*y)/n
    print(f'S_XY = {yy} - {y}^2/{n} = {syy:.4f}')
    return syy

def Sxy(dataPair):
    x,y,xy,xx,yy,n = dataPair
    sxy = xy - (x*y)/n
    print(f'S_XY = {xy} - {x}*{y}/{n} = {sxy:.4f}')
    return sxy

def r(sxx,syy,sxy):
    R = sxy/(sxx**(1/2)*syy**(1/2))
    print(f'r = {sxy:.4f}/(sqrt{sxx:.4f}*sqrt{syy:.4f}) = {R:.4f}')
    if R == -1:
        print('Perfect Negative Correlation: r = -1')
    elif R == 0:
        print('No Correlation: r = 0')
    elif R == 1:
        print('Perfect Positive Correlation: r = 1')
    elif R < -0.75:
        print('Stong Negatie Correlation: -1 < r < -0.75')
    elif R < -0.65:
        print('Moderate Negative Correlation: -0.75 < r < -0.65')
    elif R < 0:
        print('Weak Negative Correlation: -0.65 < r < 0')
    elif R < 0.65:
        print('Weak Positive Correlation: 0 < r < 0.65')
    elif R < 0.75:
        print('Moderate Positive Correlation: 0.65 < r < 0.75')
    else:
        print('Strong Positive Correlation: 0.75 < r < 1')
    return R

def rsquare(sxx,syy,sxy):
    r2 = sxy*sxy/(sxx*syy)
    print(f'r^2 = {sxy:.4f}^2/({sxx:.4f}*{syy:.4f}) = {r2:.4f}')
    return r2

def b(sxy,sxx):
    B = sxy/sxx
    print(f'b = {sxy:.4f}/{sxx:.2f} = {B:.4f}')
    return B

def a(B,tX,tY,n):
    A = tY/n - B*(tX/n)
    print(f'a = {tY}/{n} - {B:.4f}*({tX}/{n}) = {A:.4f}')
    print(f'\nY = A + BX\nY = {A:.4f} + {B:.4f}X')
    return A

#input
numDataPair = int(input('How many data pair: '))
dataPair = []
for i in range(1,numDataPair+1):
    x = int(input(f'{i} X value: '))
    y = int(input(f'{i} Y value: '))
    xy = x*y
    xx = x*x
    yy = y*y
    dataPair.append([x,y,xy,xx,yy]) 

tX = tY= tXY = tXX = tYY = 0
print(f'{"x":^6}|{"y":^6}|{"xy":^6}|{"x^2":^6}|{"y^2":^6}')
for x,y,xy,xx,yy in dataPair:
    tX += x
    tY += y
    tXY += xy
    tXX += xx
    tYY += yy
    print(f'{x:^6}|{y:^6}|{xy:^6}|{xx:^6}|{yy:^6}')
print('-'*36)
print(f'{tX:^6}|{tY:^6}|{tXY:^6}|{tXX:^6}|{tYY:^6}')
dataPair.append([tX,tY,tXY,tXX,tYY,numDataPair])

print('')
sxx = Sxx(dataPair[-1])
syy = Syy(dataPair[-1])
sxy = Sxy(dataPair[-1])
print('')
print('Correlation Coefficient')
R = r(sxx,syy,sxy)
print('')
print('Coefficient of Determination')
rSquare = rsquare(sxx,syy,sxy)
print('')
print('Simple Linear Regression')
B = b(sxy,sxx)
A = a(B,tX,tY,numDataPair)