# Leksjon 4: Kalkulator. Vi tar et regnestykke som input (tall operator tall) og splitter det opp i et array. Vi gjør en if-sjekk på operatoren 
# og utfører regnestykket. Til slutt caster vi regnestykket og svaret til strings og skriver tilbake til konsoll. 

print("Skriv inn regnestykket ditt: ")
inndata = input().split()
tall1 = inndata[0]
operator = inndata[1]
tall2 = inndata[2]

if operator == "+":
    sum = tall1 + tall2
elif operator == "-":
    sum = tall1 - tall2
elif operator == "/":
    sum = tall1 / tall2
elif (operator == "*"):
    sum = tall1 * tall2

print("Regnestykket: " + str(tall1) + operator + str(tall2))
print("Svar: " + str(sum))