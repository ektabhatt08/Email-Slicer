# Get user email address

email = input("What is your email address?: ").strip()


# Slice out user name

user_name= email[ :email.index('@')]

# Slice out host name

domain= email[email.index('@')+1 : ]

# Format Message

output = 'Your user name is {} and domain name is {}'.format(user_name, domain)

# Display Output

print(output)
