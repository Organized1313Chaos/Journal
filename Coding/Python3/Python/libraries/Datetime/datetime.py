from datetime import datetime

datetime_str = '19/09/22 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)  # printed in default format