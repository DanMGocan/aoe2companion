from data import units
unit_names = [unit["name"].replace("_", " ") for unit in units]

valid_phrases = set()

# Counter one unit 
for unit in unit_names:
    phrase = f"counter {unit}"
    valid_phrases.add(phrase)

# Counter a combination of two units 
for unit in unit_names:
    for unit2 in unit_names:
        if unit == unit2:
            continue
        else:
            phrase = f"counter {unit} plus {unit2}"
            valid_phrases.add(phrase)

# Counter a combination of three units 
for unit in unit_names:
    for unit2 in unit_names:
        for unit3 in unit_names:
                # Use a set to check for uniqueness
                if len({unit, unit2, unit3}) == 3:
                    phrase = f"counter {unit} plus {unit2} plus {unit3}"
                    valid_phrases.add(phrase)


# Counter a combination of four units 
for unit in unit_names:
    for unit2 in unit_names:
        for unit3 in unit_names:
            for unit4 in unit_names:
                # Use a set to check for uniqueness
                if len({unit, unit2, unit3, unit4}) == 4:
                    phrase = f"counter {unit} plus {unit2} plus {unit3} plus {unit4}"
                    valid_phrases.add(phrase)



# Open a file in write mode
with open("set_contents.txt", "w") as file:
    for element in valid_phrases:
        # Write each element to the file followed by a newline
        file.write(element + "\n")

print(len(units))