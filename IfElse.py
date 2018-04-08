# Leksjon 3: Vi prøver ut if-else og casting fra string til int. Brukeren gir inn en tid på døgnet og programmet returnerer en hilsen.

inntekst = input("Hvor mye er klokka?")

klokkeslett = int(inntekst)

if klokkeslett > 18:
    print("God kveld!")
elif klokkeslett > 12: 
    print("God ettermiddag!")
elif klokkeslett > 6:
    print("God morgen!")
else:
    print("God natt!")


# For de viderekommende: Kan du håndtere at bruker gir inn et tall som ikke er gyldig?