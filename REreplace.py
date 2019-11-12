import re
email_address = "Please contact us at: support@datacamp.com"
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)', r'xyz@set.ac.in', email_address)
print(new_email_address)