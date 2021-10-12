#! python3

# THIS FILE TAKES TEXT COPIED ON YOUR CLIPBOARD
# AND THEN SCRAPS THE PHONE NUMBERS AND EMAIL ADDRESSES FROM THE TEXT
# AND THEN COPIES IT BACK AGAIN TO THE CLIPBOARD SO THAT YOU CAN PASTE THE SCRAPED PHONE NUMBERS AND EMAIL ADDRESSES

#Creating a phone and email scraper in python
import re, pyperclip
# Create a regex object for phone numbers
phoneRegex = re.compile(r'''
\d\d\d-\d\d\d-\d\d\d\d
''', re.VERBOSE)
#Create a regex object for email addresses
emailRegex = re.compile(r'''
    # some.+_thing@something.com
    [a-zA-Z0-9_.+]+ #name, Created our own character class which detects all alphanumerals as well as _. and + symbols
    @ #@ symbol
     [a-zA-Z0-9_.+]+ #domain name part (inside square bracket no need of \ character)
''', re.VERBOSE)
#Get the text off the clipboard
text = pyperclip.paste()
#Extract the email/phone numbers from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


#Copy the extracted email/phone number to the clipboard
results = '\n'.join(extractedPhone) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

