#start with end in mind, print out fortune for user

print('You will have a great day! Your lucky number is: 3')

#want lucky number and perdiction changing

import random

lucky_number = random.randint(1,100)

print(f'You will have a great day! Your lucky number is: {lucky_number}')

#now change perdiction

fortune_number = random.randint(1,3)

fortune_text = ''

if fortune_number == 1:
  fortune_text = 'You will have a great day!'
if fortune_number == 2:
  fortune_text = 'Today will be tough... but worth it.'
if fortune_number == 3:
  fortune_text = 'You will get married this year!'

print(f'{fortune_text} Your lucky number is: {lucky_number}')