# Opdracht 1: Variables - Fictieve winkel
# Gemaakt door: Ibrahim

# 1. Variabelen voor drie verschillende producten en hun prijzen
product_1_naam = "Laptop"
product_1_prijs = 750.00

product_2_naam = "Muis"
product_2_prijs = 25.50

product_3_naam = "Toetsenbord"
product_3_prijs = 45.00

# 2. Variabelen voor het aantal verkochte producten
aantal_product_1 = 4
aantal_product_2 = 12
aantal_product_3 = 7

# 3. Bereken hoeveel geld de winkel in totaal heeft verdiend (totale omzet)
omzet_1 = product_1_prijs * aantal_product_1
omzet_2 = product_2_prijs * aantal_product_2
omzet_3 = product_3_prijs * aantal_product_3

totale_omzet = omzet_1 + omzet_2 + omzet_3

# 4. Print de namen, prijzen en aantallen van de producten
print("--- PRODUCT OVERZICHT ---")
print(f"Product: {product_1_naam} | Prijs: €{product_1_prijs} | Aantal verkocht: {aantal_product_1}")
print(f"Product: {product_2_naam} | Prijs: €{product_2_prijs} | Aantal verkocht: {aantal_product_2}")
print(f"Product: {product_3_naam} | Prijs: €{product_3_prijs} | Aantal verkocht: {aantal_product_3}")

# 5. Print daarna de totale omzet
print("-------------------------")
print(f"Totale omzet van de winkel: €{totale_omzet}")