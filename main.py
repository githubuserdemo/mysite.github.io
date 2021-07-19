import datetime
from random import randint


with open("index.md", 'w') as file:
    current_time = datetime.datetime.now()
    random_number = randint(0, 1000)
    file.write(
        f' ## Heading 2 \n The current time is {current_time} and a random number is {random_number}')
