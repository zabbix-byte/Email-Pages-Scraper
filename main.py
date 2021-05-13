# --*-- conding : utf8 --*-- 
import requests
import urllib.request
import csv
from bs4 import BeautifulSoup


def run():
    return  '\nZ A B B I X    C O N T E N T    P A G E   F I N D E R\n'


def findEmails(pages):
    """
    Email finder funcction
    needs: page
    return output file

    """
    try:
        html_page = urllib.request.urlopen(str(pages)) #Request the page html
        soup = BeautifulSoup(html_page, "html.parser") #Instace BeatifulSoup 

        """
        Filtering html page
        """

        filter_soup  = soup.find_all('a', href = True) 
        len_find = len(filter_soup)


        for i in range(len_find):  
            if filter_soup[i]:
                text = str(filter_soup[i])
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
    except:
        print("-----------------------------------------")
        print('Error detected:')
        print('-')
        print(f"<Error> [{pages}] [Request don't work]")
        print("-----------------------------------------")
        
            
if __name__ == "__main__":
    print(run())

    with open('./input/pages_list.txt') as f:
        lines = f.readlines()

    for i in lines:

        findEmails(i)

    print('''
    ..Finish
    ''')
 

        





