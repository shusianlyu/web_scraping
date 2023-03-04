# ----------------------------------------------------------------------
# Name:      store
# Purpose:   implement a fictional online store
# Author(s): Jessie Lyu, An Tran
# Date: 03/04/2023
# ----------------------------------------------------------------------
"""
Implementation of a fictional online store

This program consists of four classes to represent and
manipulate items sold by a fictional online store.
The class is created by description, listing price,
and some additional information based on each class' requirement.
"""


class Product:

    """
    Represent a product that sold by the store.

    Argument:
    description (string): product's description.
    list_price (int): product's listing price.

    Attributes:
    description (string): product's description.
    list_price (int): product's listing price.
    id (string): product's id.
    stock (int): product's number of items in stock.
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
        :param quantity: (int) the amount to be restocked
        :return: None
        """
        self.stock += quantity

    def review(self, stars, text):
        """
        Add stars and review as a tuple to the product.
        :param stars: (int) number of stars given by the reviewer
        :param text: (string) the text of the review
        :return: None
        """
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        """
        Deduct the number of items in stock.
        :param quantity: (int) the amount to be deducted
        :param sale_price: (int) the actual sale price of product
        :return: None
        """
        # check if stock is sufficient
        if self.stock > quantity:
            self.stock -= quantity
            self.sales.extend([sale_price] * quantity)
        else:
            self.sales.extend([sale_price] * self.stock)
            self.stock = 0

    @classmethod
    def generate_product_id(cls):
        """
        Generate product id string.
        :return: (string) product id
        """
        product_id = f"{cls.category}{cls.next_serial_number:06}"
        cls.next_serial_number += 1
        return product_id

    def __str__(self):
        return (f"{self.description}\n"
                f"Product ID: {self.id}\n"
                f"List price: ${self.list_price:,.2f}\n"
                f"Available in stock: {self.stock}")

    @property
    def lowest_price(self):
        """
        Find the lowest price of the product.
        :return: (int) lowest price, None otherwise
        """
        # check if the product has been sold
        if self.sales:
            return min(self.sales)
        return None

    @property
    def average_rating(self):
        """
        Average star rating for the product.
        :return: (float) average star rating, None otherwise
        """
        # check if the product has reviews
        if self.reviews:
            return sum(y for x, y in self.reviews) / len(self.reviews)
        return None

    def __add__(self, other):
        # create bundle
        new_bundle = Bundle(self, other)
        return new_bundle


class VideoGame(Product):

    """
    Represent a video game product with specific category and
    independent counter for the serial number.

    Argument:
    description (string): product's description.
    list_price (int): product's listing price.

    Attributes:
    description (string): product's description.
    list_price (int): product's listing price.
    id (string): product's id.
    stock (int): product's number of items in stock.
    sales (list): product's actual sale prices.
    reviews (list): product's user reviews.
    """

    # class variables
    category = "VG"  # denotes the category
    next_serial_number = 1  # denotes the next serial number

    def __init__(self, description, list_price):
        super().__init__(description, list_price)


class Book(Product):

    """
    Represent a book product with specific category,
    independent counter for the serial number, author and pages.

    Argument:
    description (string): product's description.
    author (string): author of the book.
    pages (int): pages of the book.
    list_price (int): product's listing price.

    Attributes:
    description (string): product's description.
    list_price (int): product's listing price.
    id (string): product's id.
    stock (int): product's number of items in stock.
    sales (list): product's actual sale prices.
    reviews (list): product's user reviews.
    author (string): author of the book.
    pages (int): pages of the book.
    """

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

    """
    Represent a bundle of two or more products with specific category,
    independent counter for the serial number and discount.

    Argument:
    item1 (Product): first product
    item2 (Product): second product
    args: 0 or more additional arguments

    Attributes:
    description (string): bundle product's description.
    list_price (int): bundle product's listing price after discount.
    id (string): bundle product's id.
    stock (int): bundle product's number of items in stock.
    sales (list): bundle product's actual sale prices.
    reviews (list): bundle product's user reviews.
    """

    # class variables
    category = "BL"  # denotes the category
    next_serial_number = 1  # denotes the next serial number
    bundle_discount = 20  # denotes the discount of the bundle

    def __init__(self, item1, item2, *args):
        description = f"{item1.description} & {item2.description}"
        price = item1.list_price + item2.list_price
        # check if the items are more than two
        if args:
            # add product descriptions to the string
            description += ' & ' + (' & '.join(arg.description
                                               for arg in args))
            # sum up the price of remaining items
            price += sum(arg.list_price for arg in args)
        # update list_price with discount
        list_price = price * (100 - self.bundle_discount) / 100

        super().__init__(description, list_price)


def main():
    sunglasses = Product('Vans Hip Cat Sunglasses', 14)
    print(Product.category)
    print(Product.next_serial_number)
    print(sunglasses.id)
    print(sunglasses.description)
    print(sunglasses.list_price)
    print(sunglasses.stock)
    print(sunglasses.reviews)
    print(sunglasses.sales)
    headphones = Product('Apple Airpods Pro', 199)
    sunglasses.restock(20)
    headphones.restock(5)
    print(sunglasses)
    print(headphones)
    sunglasses.sell(3, 14)
    sunglasses.sell(1, 10)
    print(sunglasses.sales)
    headphones.sell(8, 170)  # There are only 5 available
    print(headphones.sales)
    print(sunglasses)
    print(headphones)
    sunglasses.restock(10)
    print(sunglasses)
    headphones.restock(20)
    print(headphones)
    sunglasses.review(5, 'Great sunglasses! Love them.')
    sunglasses.review(3, 'Glasses look good but they scratch easily')
    headphones.review(4, 'Good but expensive')
    print(sunglasses.reviews)
    print(headphones.reviews)
    print(Product.category)
    print(Product.next_serial_number)
    print(sunglasses.lowest_price)
    print(sunglasses.average_rating)
    backpack = Product('Nike Explore', 60)
    print(backpack.average_rating)
    print(backpack.lowest_price)
    mario = VideoGame('Mario Tennis Aces', 50)
    mario.restock(10)
    mario.sell(3, 40)
    mario.sell(4, 35)
    print(mario)
    print(mario.lowest_price)
    mario.review(5, 'Fun Game!')
    mario.review(3, 'Too easy')
    mario.review(1, 'Boring')

    print(mario.average_rating)
    lego = VideoGame('LEGO The Incredibles', 30)
    print(lego)
    lego.restock(5)
    lego.sell(10, 20)
    print(lego)
    print(lego.lowest_price)
    print(VideoGame.category)
    print(VideoGame.next_serial_number)
    book1 = Book('The Quick Python Book', 'Naomi Ceder', 472, 39.99)

    print(book1.author)
    print(book1.pages)
    book1.restock(10)
    book1.sell(3, 30)
    book1.sell(1, 32)
    book1.review(5, 'Excellent how to guide')
    print(book1)
    print(book1.average_rating)
    print(book1.lowest_price)
    book2 = Book('Learning Python', 'Mark Lutz', 1648, 74.99)
    book1.restock(20)
    book1.sell(2, 50)
    print(book2)
    print(book1 > book2)
    print(book1 < book2)
    print(Book.category)
    print(Book.next_serial_number)

    bundle1 = Bundle(sunglasses, backpack, mario)
    print(bundle1)
    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)
    bundle1.sell(2, 95)
    print(bundle1)
    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)
    bundle1.sell(3, 95)
    print(bundle1)
    print(bundle1.lowest_price)
    bundle2 = Bundle(book1, book2)
    bundle2.restock(2)
    print(bundle2)
    print(Bundle.category)
    print(Bundle.next_serial_number)
    print(Bundle.bundle_discount)
    back_to_school_bundle = backpack + book1
    print(back_to_school_bundle)
    best_bundle = sunglasses + headphones + book1 + mario
    print(best_bundle)


if __name__ == '__main__':
    main()
