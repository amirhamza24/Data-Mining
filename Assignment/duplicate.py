import pandas as robin

afsar = robin.read_csv("employees.csv")


afsar.sort_values("First Name", inplace=True)

print(afsar)

afsar.drop_duplicates(subset="First Name",keep = False, inplace = True)

print(afsar)