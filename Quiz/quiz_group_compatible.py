product = ["computer", "ram", "cpu"]
price = [100,20,40]
#price.reverse()
print("Product: ",product)
print("Price: ",price)
print("show lists: ",end="")
for g in zip(product,price):
    print(g,end="")