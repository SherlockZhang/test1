from requests import get
from sys import argv
from 
if __name__ == '__main__':
    input_fn = argv[1:]
    val = float(input_fn[0])
    to = input_fn[1]
    from_ = input_fn[2]
    print(from_)	
    #r = get(f'https://api.exchangerate-api.com/v4/latest/{input_fn}')
    #r.raise_for_status()
    #print(r.json())
