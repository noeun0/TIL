import math

a=20
b=15
c=15
d=0
r=1
angle_C=math.degrees(math.acos((c**2-a**2-b**2)/((-2)*a*b)))
print('c각도',angle_C)
d=((a*math.degrees(math.sin(angle_C)))**2 + ((b+2*r)-a*math.degrees(math.cos(angle_C)))**2)
print(math.degrees(math.sin(angle_C)))

print(angle_C,d)
#라디안 * ㅠ =180