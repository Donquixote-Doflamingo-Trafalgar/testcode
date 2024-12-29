Gk1 = "Abh"
Gk2 = bool("Sri") == False
Def1 = bool("Zee") == False
Def2 = "Eth"
Def3 = bool("Sid") == False
Def4 = "Aar"
Def5 = "Sidbl" 
Def6 = "Nob" 
Mid1 = "Sidh"
Mid2 = "Dhr"
For1 = "San"
if Gk1 and Gk2:
    print("Both goalkeepers are available.")
elif Gk1 or Gk2:
    print("One goalkeeper is available.")
if Def1 and Def2 and Def3 and Def4 and Def5 and Def6:
    print("All defenders are available.")
elif Def1 and Def3 and (Def5 or Def4):
    print("Best defenders are available.")
else:
    print("Best defenders are not available.")
if Gk2 and Def1 and Def3 and Def4 and Def5 and Mid1 and Mid2 and For1:
    print("The best squad is available.")
else: 
    print("The best squad is not possible.")
if not (Gk2 and Def1 and Def3):
    print(f"{Mid2}")
else:
    print("They aren't available.")
