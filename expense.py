
print(f""" A friendly Hobbit, named Tomburan Longriver, has opened a shop at the local Middle Earth Festival. He sells Rabbit Stew, Cram Bread, Salted Pork, Mushrooms, Honey Cake, Lembas, and Well Water. Tomburan needs help keeping track of his dishes sold, money earned per dish, and total profits after the festival grounds takes a cut. """)

print(f""" "We will need to create a sort of app for Tomburan Longriver to help him with his horrible math skills and money management. We can start by taking inventory of everything that was sold." """)

M = int(input("How many Mushrooms were sold: "))
L = int(input("How many Lembas were sold: "))
C = int(input("How many Cram Bread were sold: ")) S = int(input("How many Salted Pork were sold: ")) R = int(input("How many Rabbit Stew were sold: ")) H = int(input("How many Honey Cake were sold: ")) W = int(input("How many Well Water were sold: "))

price_mushrooms = 0.80 price_lembas = 3.00 price_cram_bread = 2.00 price_salted_pork = 2.25 price_rabbit_stew = 3.25 price_honey_cake = 2.00 price_well_water = 1.25

total_M = M * price_mushrooms total_L = L * price_lembas total_C = C * price_cram_bread total_S = S * price_salted_pork total_R = R * price_rabbit_stew total_H = H * price_honey_cake total_W = W * price_well_water

total_received = total_M + total_L + total_C + total_S + total_R + total_H + total_W Pre_Cut = total_received / 2

cut_taken = total_received * 0.0675 total_minus_cut = total_received - cut_taken

print("------------------------------------------") 
print("----Tomburan Longriver's Savory Dishes----") 
print("------------------------------------------")
print(" QTY DISH NAME UNIT PRICE TOTAL RECEIVED") 
print("---- ------------- ---------- --------------") 
print(f"{M:<4} Mushrooms $ {price_mushrooms:<8} $ {total_M:<12.2f}") print(f"{L:<4} Lembas $ {price_lembas:<8} $ {total_L:<12.2f}") 
print(f"{C:<4} Cram Bread $ {price_cram_bread:<8} $ {total_C:<12.2f}") print(f"{S:<4} Salted Pork $ {price_salted_pork:<8} $ {total_S:<12.2f}") print(f"{R:<4} Rabbit Stew $ {price_rabbit_stew:<8} $ {total_R:<12.2f}") 
print(f"{H:<4} Honey Cake $ {price_honey_cake:<8} $ {total_H:<12.2f}") print(f"{W:<4} Well Water $ {price_well_water:<8} $ {total_W:<12.2f}") print(" --------------") 
print(f" TOTAL RECEIVED $ {total_received:<12.2f}") print(f" CUT TAKEN $ {cut_taken:<12.2f}") print(f" TOTAL MINUS CUT $ {total_minus_cut:<12.2f}")

print(f"Total Profit pre-cut: {Pre_Cut:.2f}")
