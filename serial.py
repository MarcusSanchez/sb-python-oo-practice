import random

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

    def __init__(self, start=0):
        """Init the serial generator. Use underscores to private the attributes."""
        self._start = start
        self._next = start - 1

    def __repr__(self):
        return f"<SerialGenerator start={self._start} next={self._next}>"

    def generate(self):
        """Generate the next serial number."""
        self._next += 1
        return self._next

    def reset(self):
        """Reset the serial number to the initial start."""
        self._next = self._start - 1


# serial_generator = SerialGenerator(100)
# print(serial_generator.generate())
# print(serial_generator.generate())
# print(serial_generator.generate())
# serial_generator.reset()
# print(serial_generator.generate())
# print(serial_generator.generate())
# print(serial_generator)
