import requests
import hashlib
import sys

def request_api_data(query_char):
    # CBFDAC6008F9CAB4083784CBD1874F76618D2A97 == password123 SHA1 hashed
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(response, hash_to_check):
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api(password):
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = hashed_password[:5], hashed_password[5:]
    # check password if exists in api response
    api_response = request_api_data(first5_char)
    return get_password_leaks_count(api_response, tail)


def main(args):
    for password in args:
        count = pwned_api(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password')
        else:
            print(f'{password} was not found. Carry on!')
    return 'done'


if __name__ == '__main__':
    array_of_passwords = sys.argv[1:]
    # add custom passwords
    # array.append('another_pass')
    main(array_of_passwords)


exit()
