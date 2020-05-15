import os
import random
import sys

method = ['Braised','Roasted','Grilled','Sauteed','Boiled','Sous-vide','Baked','Broiled']   
protein = ['Chicken Legs','Chicken Breast','Pork Chop','Ground Pork','Ground Beef', 'Chicken wings','Beef Steak','Sausages',]
carbSide = ['Rice','Potatoes','Pasta','Noodles','Squash Noodles','Legumes','Beans','Couscous']
vegSide = ['Broccoli','Carrots','Onions','Peppers','Mushrooms','Summer Squash','Cabbage','Tomatoes','Artichokes','Cucumbers','Celery']
sauceSide = ['Salsa Verde','Broth','Cream','Tomato','Jus','Chimichurri','Chipotle','Buffalo','BBQ']


def dinner():
    answer = (input('Would you like to start dinner?\n')).lower()
    
    
    if answer == 'yes':
            print('\nO.K., here is tonight\'s option.\n')
            print(random.choice(method))
            print(random.choice(protein) + ' with')
            print(random.choice(carbSide)+ ',')
            print(random.choice(vegSide)+ ',')
            print(random.choice(vegSide)+ ',')
            print('and a ' + random.choice(sauceSide)+ ' sauce')
            print('Enjoy the meal!\n')
                
    if answer =='no':
        print('Great, Andrew hates cooking anyway\n\n\n')
        dinner()
        os.execv(__file__, sys.argv)
        
while True:
    dinner()
    if input("Want to see more options?\n").strip().upper() != 'Y':
        continue

dinner()
