R_Bdor = 5
M_Bdor = 6
R_poty = 3
M_poty = 2
print(f"Ronaldo best player awards = {R_Bdor+R_poty}")
print(f"Messi best player awards = {M_Bdor+M_poty}")
if R_Bdor>M_Bdor and R_poty>M_poty:
    print("Ronaldo is the GOAT.")
elif M_Bdor>R_Bdor and M_poty>R_poty:
    print("Messi is the GOAT.")
else:
    print("Both of them are the GOATS!")