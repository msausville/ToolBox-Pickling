""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    # Note: Looked at classmates' code to help make this.
    if exists(file_name) and not reset:
        # The file has already been made and the reset button hasn't been pressed.
        file = open(file_name, 'rb+')
        # Open the file in reading mode
        counter = load(file)
        counter += 1
        # Tell the counter to add one because the file was opened again.
        file.close
        return counter
        # Close the file and tell us the number on the counter.
    else:
        file = open(file_name, 'wb')
        # The file hasn't been declared or has been reset, rewrite it or make a new one.
        counter = 1
        # The file has been opened once so the count is one.
        dump(counter, file)
        # dumping it is what saves the pickle.
        file.close
        return counter

    # pickle.load
    # check if file exists
    # if doesn't, create file
    # initialize counter variable


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
