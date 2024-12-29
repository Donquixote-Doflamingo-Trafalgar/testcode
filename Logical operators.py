Player1 = "Salah"
Goals1 = 19
Assists1 = 15
Player2 = "Raphinha"
Goals2 = 17
Assists2 = 10
print(f"{Player1}'s club GA 2024/25 = {Goals1+Assists1}")
print(f"{Player2}'s club GA 2024/25 = {Goals2+Assists2}")
if Goals1>Goals2 and Assists1>Assists2:
    print(f"{Player1} is the better club player.")
elif Goals2>Goals1 and Assists2>Assists1:
    print(f"{Player2} is the better club player.")