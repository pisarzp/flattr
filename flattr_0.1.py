#!/usr/bin/python2.6 -tt
# flattr v.01
# Piotr Pisarz 2012
# pisarzp@gmail.com
# All Rights Reserved

import urllib
import re
import csv
import time
import smtplib, os


list_of_links = []
girls_dict = {}



def UrlToText(url):
  url_file = urllib.urlopen(url)
  contents = url_file.read()
  return contents
  

  

def ReturnFlatsData(website):
  temp_dict={}
  something_list= re.findall(r'cell\_location(.+?)<div',website)
  
  ##print website
  ##print phone_number_list
  ##print url_location
  #print website
  print 'START------>'
  print something_list

  return something_list

  
def ProcessOfertyNet():
  ##This procedure parses oferty.net and gets flat data into the database
  # Insert manually link with the first page with listings of all flats in the city to the variable start_link
  start_link_oferty_net = "http://www.oferty.net/mieszkania/szukaj?page=1&ps%5Badvanced_search%5D=&ps%5Blocation%5D%5Btype%5D=1&ps%5Blocation%5D%5Bmap%5D=&ps%5Blocation%5D%5Btext%5D=Warszawa&ps%5Btype%5D=1&ps%5Btransaction%5D=1&ps%5Bliving_area_from%5D=od&ps%5Bliving_area_to%5D=do&ps%5Bprice_from%5D=od&ps%5Bprice_to%5D=do&type=1"
  max_pages_to_crawl = 1
  continue_loop = 1
  counter =1
  
  # loop is executed until continue_loop is set to 0
  # trigger to set continue_loop to 0 is [TO BE DETERMINED. CURRENTLY REACHING 100]
  while continue_loop:
  	link = 'http://www.oferty.net/mieszkania/szukaj?page=' + str(counter) + '&ps%5Badvanced_search%5D=&ps%5Blocation%5D%5Btype%5D=1&ps%5Blocation%5D%5Bmap%5D=&ps%5Blocation%5D%5Btext%5D=Warszawa&ps%5Btype%5D=1&ps%5Btransaction%5D=1&ps%5Bliving_area_from%5D=od&ps%5Bliving_area_to%5D=do&ps%5Bprice_from%5D=od&ps%5Bprice_to%5D=do&type=1'
  	parsed_webpage = UrlToText(link)
  	#print parsed_webpage
  	flats_data = ReturnFlatsData(parsed_webpage)
  	print flats_data
  	#link <td class="cell_location"><a href="
              
  	
  	if counter == max_pages_to_crawl:
  		continue_loop = 0	
  	counter+=1
  
  
  return


  
def main():
  #Global variables setup
  debug = 1
  #CSV output data
  today_date = time.strftime("%Y%m%d", time.localtime())
  today_time = time.strftime("%H:%M", time.localtime())
  output_file = str(today_date) + '-' + str(today_time) +  '-flats_data.csv'
  
  # Create CSV Output file 
  '''
  
  data_file = open(output_file, 'w')
  field_names = ['id','link','year','floor',]
  data_writer = csv.DictWriter(data_file, field_names)
  header_row = {'id':'ID',
                'link':'Link',
                'year':'Year',
                'floor':'Floor',
            	}
  data_writer.writerow(header_row)
  '''
 
  #Begin main part of the program
  #
  
  ProcessOfertyNet()
  
    

    
if __name__ == '__main__':
  main()
  