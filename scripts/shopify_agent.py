import random

def calculate_investment(price, cost, stock_percent=0.20):
    profit = price - cost
    to_stock = profit * stock_percent
    to_brand = profit - to_stock
    return profit, to_stock, to_brand

def generate_shopify_description(product_name, material):
    hooks = ["Error 404: Normalcy not found.", "Bland is the new bold.", "Join the glitch."]
    return f"<h2>{product_name.upper()}</h2><p>{random.choice(hooks)}</p><p>Premium {material}.</p>"

# --- USER INPUT ---
print("🐑 BLAND SHEEP BUSINESS AGENT 🐑")
name = input("Product Name: ")
cost = float(input("Total Cost to make (Tee + Print + Shipping): $"))
retail = float(input("Retail Price: $"))

profit, to_stock, to_brand = calculate_investment(retail, cost)

print("\n" + "="*30)
print(f"FINANCIAL BREAKDOWN for {name}")
print("="*30)
print(f"Profit per Shirt: ${profit:.2f}")
print(f"Reinvest in Brand: ${to_brand:.2f}")
print(f"✨ SEND TO STOCK FUND: ${to_stock:.2f}")
print("-" * 30)

# Calculate Goal
spy_price = 500  # Rough estimate of SPY share price
shirts_needed = int(spy_price / to_stock) + 1
print(f"GOAL: Sell {shirts_needed} shirts to buy 1 full share of SPY.")
print("="*30)

print("\n--- GENERATED SHOPIFY DESCRIPTION ---")
print(generate_shopify_description(name, "Cotton"))
