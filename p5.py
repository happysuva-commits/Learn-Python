#Saal leap year hai ya nahi. (4 se divisible aur 100 se nahi, ya 400 se divisible) 

year=2027

leap=(year%4==0 and year %100!=0) or (year % 400==0)
print(leap)