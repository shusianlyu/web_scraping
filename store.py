# ----------------------------------------------------------------------
# Name:      store
# Purpose:   implement a fictional online store
# Author(s): Jessie Lyu, An Tran
# ----------------------------------------------------------------------

class Product:

    """
    Represents all products sold by the store
    Argument:
    description (string): description of product
    list_price (int): manufacturer suggested retail price
    Attributes:
    id (string): id of product
    stock (int): number of items in stock
    """

    category = 'GN'
    next_serial_number = 1

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.id = self.generate_product_id()
        self.stock = 0
        self.sales = []
        self.reviews = []

    def restock(self, quantity):
        """
        restocks product
        :param quantity: (int) amount to restock
        :return: None
        """
        self.stock += quantity

    def review(self, stars, text):
        """
        adds review and rating to review list
        :param stars: (int) rating
        :param text: (int) review text
        :return: None
        """
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        """
        sell quantity of product at sale price
        :param quantity: (int) amount of product to be sold
        :param sale_price: (int) price product is sold at
        :return: None
        """
        if self.stock != 0:
            if quantity >= self.stock:
                self.sales += [sale_price for i in range(self.stock)]
                self.stock = 0
                # for i in range(self.stock):
                #     self.sales.append(sale_price)
                # self.stock = 0
            else:
                self.sales += [sale_price for i in range(quantity)]
                self.stock -= quantity
                # for i in range(quantity):
                #     self.sales.append(sale_price)
                # self.stock -= quantity

    @classmethod
    def generate_product_id(cls):
        """
        create product id string
        :return: string
        """
        new_id = f'{cls.category}{cls.next_serial_number:06}'
        cls.next_serial_number += 1
        return new_id

    def __str__(self):
        return f'{self.description}\nProduct ID: {self.id}\nList price: $' \
               f'{self.list_price:,.2f}\nAvailable in stock: {self.stock}'

    @property
    def lowest_price(self):
        """
        lowest sale price
        :return: int
        """
        if len(self.sales) != 0:
            return min(self.sales)

    @property
    def average_rating(self):
        """
        avg rating for product
        :return: float
        """
        if len(self.reviews) != 0:
            avg = sum(y for x, y in self.reviews) / len(self.reviews)
            return avg

    def __add__(self, other):
        new_bundle = Bundle(self, other)
        return new_bundle


class VideoGame(Product):

    """
    Video game product
    Argument:
    description (string): description of product
    list_price (int): manufacturer suggested retail price
    Attributes:
    id (string): id of product
    stock (int): number of items in stock
    """

    category = 'VG'
    next_serial_number = 1

    def __init__(self, description, list_price):
        super().__init__(description, list_price)


class Book(Product):

    """
        Video game product
        Argument:
        description (string): description of product
        author (string): author of book
        pages (int): pages of book
        list_price (int): manufacturer suggested retail price
        Attributes:
        id (string): id of product
        stock (int): number of items in stock
    """

    category = 'BK'
    next_serial_number = 1

    def __init__(self, description, author, pages, list_price):
        self.author = author
        self.pages = pages
        super().__init__(description, list_price)

    def __lt__(self, other):
        return self.pages < other.pages


class Bundle(Product):

    """
            Bundle product
            Argument:
            description (string): description of products in bundle
            list_price (int): total cost of bundle with 20% discount
            Attributes:
            id (string): id of product
            stock (int): number of items in stock
            bundle_discount (int): discount of bundle
    """

    category = 'BL'
    next_serial_number = 1
    bundle_discount = 20

    def __init__(self, *product):
        description = ' & '.join([name.description for name in product])
        list_price = sum([name.list_price for name in product]) * (100-20)/100
        super().__init__(description, list_price)


def main():
    book = Product("Large enormous book", 14)
    sunglasses = Product("Nyan cat sunglasses", 199)
    print(Product.category)
    print(Product.next_serial_number)
    print(book.id)
    print(book.description)
    print(book.list_price)
    print(book.stock)
    print(book.reviews)
    print(book.sales)
    book.restock(20)
    sunglasses.restock(5)
    print(book)
    print(sunglasses)
    book.sell(3, 14)
    book.sell(1, 10)
    print(book.sales)
    sunglasses.sell(8, 170)
    print(sunglasses.sales)
    print(book)
    print(sunglasses)
    book.restock(10)
    print(book)
    sunglasses.restock(20)
    print(sunglasses)
    book.review(5, 'Great sunglasses! Love them.')
    book.review(3, 'Glasses look good but they scratch easily')
    sunglasses.review(4, 'Good but expensive')
    print(book.reviews)
    print(sunglasses.reviews)
    print(Product.category)
    print(Product.next_serial_number)
    print(book.lowest_price)
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
    bundle1 = Bundle(book, backpack, mario)
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
    best_bundle = sunglasses + sunglasses + book1 + mario
    print(best_bundle)


if __name__ == '__main__':
    main()
