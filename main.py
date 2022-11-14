
from classes import Helper
import os


def main():
    with Helper() as helper:
        # helper.print_notes()
        # helper.print_contacts()
        helper.running()


if __name__ == '__main__':
    main()
