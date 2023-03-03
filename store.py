# ----------------------------------------------------------------------
# Name:      store
# Purpose:   implement a fictional online store
# Author(s): Jessie Lyu, An Tran
# ----------------------------------------------------------------------
"""
Implementation of a fictional online store

docstring here
"""


class Product:
    """
    Represent a product that sold by the store.

    Argument:
    description (string): product's description.
    list_price (string): product's listing price.

    Attributes:
    description (string): product's description.
    list_price (string): product's listing price.
    id (string): product's id.
    stock (number): product's number of items in stock.
    sales (list): product's actual sale prices.
    reviews (list): product's user reviews.
    """

    # class variables
    category = "GN"  # denotes the category
    next_serial_number = 1  # denotes the next serial number

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.id = self.generate_product_id()
        self.stock = 0
        self.sales = []
        self.reviews = []

    def restock(self, quantity):
        """
        Restock the given quantity to the product.
        :param quantity: (number) the amount to be restocked.
        """
        self.stock += quantity

    def review(self, stars, text):
        """
        Add stars and review as a tuple to the product.
        :param stars: (number) number of stars given by the reviewer.
        :param text: (string) the text of the review.
        """
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        """
        Deduct the number of items in stock.
        :param quantity: (number) the amount to be deducted.
        :param sale_price: (number) the actual sale price of product.
        """
        if self.stock >= quantity:
            self.stock -= quantity
            self.sales.extend([sale_price] * quantity)
        else:
            for i in range(self.stock):
                self.sales.append(sale_price)
                self.stock -= self.stock

    @classmethod
    def generate_product_id(cls):
        """

        :return:
        """
        cls.next_serial_number += 1
        product_id = f"{cls.category}{cls.next_serial_number - 1:06}"
        return product_id

    def __str__(self):
        return (f"{self.description}\nProduct ID: "
                f"{self.id}\n"
                f"List price: ${self.list_price:,.2f}\n"
                f"Available in stock: {self.stock}")

    @property
    def lowest_price(self):
        if self.sales:
            return min(self.sales)
        return None

    @property
    def average_rating(self):
        if self.reviews:
            return sum([item[1] for item in self.reviews]) / len(self.reviews)
        return None

    def __add__(self, other):
        new_bundle = Bundle(self, other)
        return new_bundle


class VideoGame(Product):
    # class variables
    category = "VG"  # denotes the category
    next_serial_number = 1  # denotes the next serial number


class Book(Product):
    # class variables
    category = "BK"  # denotes the category
    next_serial_number = 1  # denotes the next serial number

    def __init__(self, description, author, pages, list_price):
        super().__init__(description, list_price)
        self.author = author
        self.pages = pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __lt__(self, other):
        return self.pages < other.pages


class Bundle(Product):
    # class variables
    category = "BL"  # denotes the category
    next_serial_number = 1  # denotes the next serial number
    bundle_discount = 20

    def __init__(self, item1, item2, *args):
        description = f"{item1.description} & {item2.description}"
        list_price = item1.list_price + item2.list_price
        for each_arg in args:
            description += f" & {each_arg.description}"
            list_price += each_arg.list_price
        super().__init__(description,
                         list_price * ((100 - self.bundle_discount) / 100))

