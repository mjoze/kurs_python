# word = "antidisestablishmentarianism"
# answer = word[word.index('establishment'):word.index('aria')]

email = input('What is your email address?: ').strip()
user = email[:email.index('@')]
domain = email[email.index('@') + 1:]
output = "Your usename is {} and your domain is {}".format(user, domain)
print(output)


