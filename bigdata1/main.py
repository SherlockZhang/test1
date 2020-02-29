#from sys import argv
from src import api
import argparse
import json
from sys import argv

def main():
    input_fn = argv[1]
    #parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    #parser.add_argument("--page_size")
    #parser.add_argument("--num_page")
    #parser.add_argument("--output")
    #args = parser.parse_args()
    #page_size = args.page_size
    #num_page = int(args.num_page)
    #output_file = args.output
    with open(input_fn,'r') as fh:
        for line in fh:
            line = line.strip('\n')
            page_size, num_page, output_file = line.split(' ')
            page_size = int(page_size)
            num_page = int(num_page)
            
    for i in range(num_page):
            output_data=api.get_data(page_size,i) 
            with open(output_file, 'a') as outfile:
                json.dump(output_data, outfile)

    
if __name__ == '__main__':
    main()
     #output = api.get_data(page_size,1)
