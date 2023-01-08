"""Python serial number generator."""

class SerialGenerator:
    '''
    Machine to create unique incrementing serial numbers.

    Attributes
    ____________________________
    number: int
        the starting value of numbers to be generated and increased
    ____________________________
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
    '''

    def __init__(self, start, next = None):
        '''
        Storing 2 copies of the number, one to iterate and one save as the initial value to reset to
        '''
        self.start = start
        if next == None:
            self.next = start
        else:
            self.next = next

    def __repr__(self):
        return f'SerialGenerator(start={self.start}, next={self.next})'

    def generate(self):
        '''
        Stores a copy of the current value of the initiated number, iterates the original number by 1, and returns the copy
        '''
        new_serial_number = self.next
        self.next += 1
        return new_serial_number
        

    def reset(self):
        '''
        Resets the initiated number back to it's original value
        '''
        self.next = self.start