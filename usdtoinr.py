def conversion(usd):
    inr = usd * 94.92
    return inr
usd = float(input("Enter amount in USD: "))
inr = conversion(usd)
print(f"{usd} USD is equal to {inr} INR")