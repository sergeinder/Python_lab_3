from Product import Product
from Foreign_product import ForeignProduct
from Broken_product import BrokenProduct

product = Product(price=5)
another_product = Product(name="Potato", price=20, size=0.05)


def input_name(massage: str = "") -> str:
    while True:
        try:
            my_name = input(massage)
            if my_name == "":
                raise ValueError
            return my_name
        except ValueError:
            print("You entered empty name: ")


def input_float(massage: str = "") -> float:
    while True:
        try:
            float_value = float(input(massage))
            if float_value < 0.01:
                raise ValueError
            return float_value
        except ValueError:
            print("You entered incorrect data")


foreign_product = ForeignProduct(name=input_name("Enter name: "),
                                 size=input_float("Enter size: "),
                                 price=input_float("Enter price: "),
                                 country_name=input_name("Enter country name: "),
                                 transit_tax=input_float("Enter transit tax: "))
broken_product = BrokenProduct(name=input_name("Enter name: "),
                               size=input_float("Enter size: "),
                               price=input_float("Enter price: "),
                               fault_description=input_name("Enter fault description: "))

print("Function box: ", foreign_product.box(1, 1, 1))

print("Sale from Product: ", product.sale(20))
print("Sale from BrokenProduct", broken_product.sale(10))
print("Sale from ForeignProduct: ", foreign_product.sale(10))

print(product)

print(product + another_product)

print(foreign_product)
print(broken_product)
