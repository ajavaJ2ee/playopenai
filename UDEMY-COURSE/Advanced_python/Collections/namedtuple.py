from collections import namedtuple


account=('checking','1565.0')

# print(account[0])
# print(account[1])

Account=namedtuple('Account',['name','balance'])

# account=Account('checking','1565.0')
#
# print(account.name)
#
# print(account.balance)

accountnamedtuple=Account(*account)

print(accountnamedtuple._asdict())

print(accountnamedtuple.name)

print(accountnamedtuple.balance)


