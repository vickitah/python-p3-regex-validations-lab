import re

# Name regex:
# - Starts with uppercase letter
# - Followed by one or more lowercase letters
# - Can have multiple words separated by a single space
# - Each word follows same pattern
name_regex = re.compile(
    r"^[A-Z][a-z]*(?:['-][A-Z][a-z]*)?(?: [A-Z][a-z]*(?:['-][A-Z][a-z]*)?)*$"
)

# Phone regex:
# - Matches formats like "5555555555", "555-555-5555", "(555) 555-5555"
# - Allows optional parentheses around area code
# - Allows optional dashes or spaces as separators
phone_regex = re.compile(r"^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$")

# Email regex:
# - Allows word characters, dots, and hyphens before and after '@'
# - Requires '@' and a domain with a dot and extension
# - Simple but works for most cases in your tests

email_regex = re.compile(r"^[A-Za-z][\w\.-]*@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+$")