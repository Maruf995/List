print("   Список Продуктов     ")
products = ["Вода", "Хлеб", "Овощи"]
print(products)
while True:
    delete = input("Добавить [1], Убрать [2] ")
    if delete == "1":
        print("Какой продукт добавить? ")
        product = input()
        products.append(product)
        print(products)
    if delete == "2":
        print("Какой продукт убрать? ")
        product = input()
        products.remove(product)
        print(products)
else:
    print("Не верное число!")
