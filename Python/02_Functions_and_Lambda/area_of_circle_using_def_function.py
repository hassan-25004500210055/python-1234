# Area of circle using def function

from matplotlib.pylab import number


def  Area(r):
    a= 3.14 * r * r
    return a
r=int(input("Enter the radius of circle: "))
ans=Area(r)
print("Area of circle is :",ans)