#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getDiscountedPrice' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER barcode as parameter.
# API URL: https://jsonmock.hackerrank.com/api/inventory?barcode=<barcode>
#

def getDiscountedPrice(barcode):
    # Write your code here
    import requests

    url = f"https://jsonmock.hackerrank.com/api/inventory?barcode={barcode}"
    response = requests.request("GET", url)

    response_text = response.json()
    data = response_text['data']
    
    if not data:
        return -1

    dict_data = data[0]
    price = dict_data['price']
    discount = dict_data['discount']
    result = round(price - price*(discount/100))
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    barcode = int(input().strip())

    result = getDiscountedPrice(barcode)

    fptr.write(str(result) + '\n')

    fptr.close()
