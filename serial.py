#!/usr/bin/env python3
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
        self.start = self.begin = start
        

    def generate(self):
        self.start += 1
        return self.start - 1

    def reset(self):
        self.start = self.begin
        return
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()