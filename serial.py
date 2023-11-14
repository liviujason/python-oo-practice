"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0, counter=0):
        self.start = start
        self.counter = 0

    def generate(self):
        """Generate a serial number by incrementing start by plus one"""
        serial = self.start + 1
        self.counter += 1
        self.start += 1
        return serial

    def reset(self):
        """Reset the start number to its original value"""
        self.start = self.start - self.counter
        self.counter = 0
        return self.start
