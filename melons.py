"""Classes for melon orders."""

from random import randint

class AbstractMelonOrder():
    """ An abstract base class that other melon orders inherit from """

    def __init__(self, species, qty):
        """ Initialize melon order attributes """

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None

    def get_base_price(self):
        """ Choose random base price """

        return randint(5, 9)


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty)

        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """ A government melon order """

    def __init__(self, species, qty):
        super().__init__(species, qty)

        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        
        if passed == True:
            self.passed_inspection = True

