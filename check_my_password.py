import requests 
import hashlib

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/"+query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching :{res.status_code}. check api an try again') 
    return res
def get_password_leaks_count(hashes, has_to_check):
    hashes = (line.split(':') for line in hashes.text)
    print(response.text)

def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5_char,tail = sha1_password[:5],sha1_password[5:]
    response  = request_api_data(first_5_char)
    print(first_5_char)
    print(tail)
    return get_password_leaks_count(response,tail)

pwned_api_check('pass')