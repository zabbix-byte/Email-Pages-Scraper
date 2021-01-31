# --*-- conding : utf8 --*-- 
import requests
import urllib.request
import csv
from bs4 import BeautifulSoup


def findEmails(pages):


    html_page = urllib.request.urlopen(str(pages))
        
    soup = BeautifulSoup(html_page, "html.parser")
        
    find  = soup.find_all('a', href = True)
        
    len_find = len(find)
        
    for i in range(len_find):  
        if find[i]:
            text = str(find[i])
            len_text = len(text)
            position_1 = text.find('mailto:')
            position_2 = text.find('">')

            if position_1 > 0 :
                initial = int(position_1) + 7
                final = int(position_2)

                if position_1 == position_1 :
                    text_email = text[initial:final]
                    
                    print(f'    {pages} :\n \n       {text_email}\n \n')

                    file_text = open('./output/emails_list.txt', 'a')
                    file_text.write(f'{text_email},\n')
                    file_text.close

        else:
            print(f'{pages} : Not found')
                
            

                    



if __name__ == "__main__":
    print( '''
    Z A B B I X    E M A I L    P A G E   F I N D E R
    ''')

    with open('./input/pages_list.txt') as f:
        lines = f.readlines()

    for i in lines:

        findEmails(i)

    
    print('''
    ..Finish
    ''')
 

        





