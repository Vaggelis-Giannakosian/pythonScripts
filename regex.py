import re

emailPatter = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
passwordPatter = re.compile(r"(^[a-zA-Z0-9$%#@]{7,}\d$)")


string = 'e.giannakosian@gmail.com'
password = 'asdfasdfsdf$%'

print('search' in string)


result = emailPatter.search(string)
passwordRes = passwordPatter.fullmatch(password)
print(passwordRes)
result2 = emailPatter.findall(string)
result3 = emailPatter.fullmatch(string)
result4 = emailPatter.match(string)


# print(result.group(0))
# print(result2)
# print(result3)
# print(result4)
#
#
#

