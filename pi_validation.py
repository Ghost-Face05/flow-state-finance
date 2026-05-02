# pi_validation.py

"""
This script performs domain validation functionality for a self-hosted Pi Network application.
"""

import re


def validate_domain(domain):
    # Validate if the domain format is correct using regex
    regex = r'^(?:http(s)?://)?(?:www\.)?([a-zA-Z0-9_-]+\.[a-zA-Z]{2,})$'
    return re.match(regex, domain) is not None


def main():
    domain = input("Enter the domain to validate: ")
    if validate_domain(domain):
        print(f'The domain {domain} is valid.')
    else:
        print(f'The domain {domain} is invalid.')


if __name__ == '__main__':
    main()
