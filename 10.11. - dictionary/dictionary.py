diction = {"klic": 5, "zamek": 8}
znamky = {"Stepan": 4, "Vojtech": 2, "Matej": 1, "Honza": 5}
print(znamky)
test = {10: 15, 20: 64}
test2 = {"Stepan": "jj"}
test3 = {}

znamky["Matej"] = 3
print(znamky)

znamky["Martin"] = 2
print(znamky)

znamky.update({"Jiří": 1, "Jana": 4})
print(znamky)

potraviny = ["Rohlik", "Jabko", "Chleba"]
ceny_potravin = [3, 20, 30]

ceny = {key:value for key, value in zip(potraviny, ceny_potravin)}
print(ceny)

print(znamky["Matej"])

if "Matej" in znamky:
    print("Nachazi se")
else:
    print("nenachazi se :(")

print(znamky.get("Matej"))

print(znamky.pop("nic", "Tento klic nema znamku"))

print(list(znamky))

for hodnoty in znamky.values():
    print(hodnoty)

for klic, hodnota in znamky.items():
    print(klic + " ma znamku " + str(hodnota))


cisla_ceny = {
    00000000: "televize",
    11111111: "telefon",
    22222222: "kniha",
    33333333: "auto",
    44444444: "opice",}
uzivatel = input("zadejte 8 cisle")
uzivatel = int(uzivatel)
if uzivatel in cisla_ceny:  
    print("gratuluji vyhral jsi " + cisla_ceny.get(uzivatel))
else:   
    print("nevyhral jsi nic")
 
