## Installation

# !pip install faker

from faker import Faker

#define local data
fake = Faker(['en_IN'])

'''
fake.name()
address()
email()
street_address()
street_name()
fake.first_name_male() 
fake.last_name()
fake.zipcode()
fake.latlng()
building_number()
city()
fake.postcode()
np.random.choice(["United Kingdom", "France", "Belgium"]
'''

import random
#faker.random.seed(20)

name = fake.name()
package_codes = ["DEV_BHOOMI","PASSPORT", "SSP", "LOCAL_POLICE_STATION"]
package_code = random.choice(package_codes)
