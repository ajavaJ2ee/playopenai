import re


price= 'Price: $1,896,062.50252415'

#expression='[0-9\$]*[0-9\,]*\.[0-9]*'
expression='\$[0-9\,]*\.[0-9]*'
exp2='[A-z\:]+'

matches=re.search(expression,price)

matches2=re.search(exp2,price)

print(matches)

print(matches2)