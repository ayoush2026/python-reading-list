import requests
import json

try:

  choice = input('Search Book By: Pick Number \n1.Title\n2.Author\n3.Both\n')

  params = {} # use params for API request

  if choice=='1':
   params['title'] = input('Enter the Title of Book:')
  elif choice=='2':
   params['author'] = input('Enter the Author of Book:')
  elif choice=='3':
   params['title'] = input('Enter you Title of Book:')
   params['author'] = input('Enter the Author of Book:')
  else:
   print('Invalid Input!')
   raise Exception('Program Terminate')

  url = "https://openlibrary.org/search.json"
  headers = {"User-Agent": "ReadingList/1.0(ayoushkumar391@gmail.com)"}
  response = requests.get(url,params=params,headers=headers,timeout=5)
  response.raise_for_status()
  result = response.json()

  print('Results Found:',result['num_found'])

  length = len(result['docs'])
  result = result['docs']
  Saved_List = []

  # add Api to print cover
  No=0
  print('\n\n----------------Book Search Results----------------')
  for book in result:

    if book.get('cover_i'):
     cover_url = f"https://covers.openlibrary.org/b/id/{book.get('cover_i')}-L.jpg"
     print('Image Url:',cover_url)

    print('Number:',No)
    print('Title:',book['title'])
    print('Author Name:',book['author_name'])
    print('First Published:',book['first_publish_year'])
    print('Editions:',book['edition_count'],end='\n\n')
    No+=1

  choice=''

  while choice!='0':
   print('Do you Want To Save Any Book:')
   print('1. Yes')
   print('0. Terminate Program')
   choice = input('Enter: ')
   if choice=='1':

     while True:

      try:
       print(f'Enter The Number Of Book You Want To Save no>=0 and no<{length}')
       book_no = int(input('Enter: '))
      except:
        print('Please Pick Number')
        continue

      if book_no>=0 and book_no<length:
       Saved_List.append({
           'id':result[book_no]['key'] if result[book_no].get('key') else '',
           'title':result[book_no]['title'] if result[book_no].get('title') else '',
           'author':result[book_no]['author_name'] if result[book_no].get('author_name') else '',
           'edition_count':result[book_no]['edition_count'] if result[book_no].get('edition_count') else '',
           'cover_id':result[book_no]['cover_i'] if result[book_no].get('cover_i') else '',
           'publish_year':result[book_no]['first_publish_year'] if result[book_no].get('first_publish_year') else '',
           'language':result[book_no]['language'] if result[book_no].get('language') else '',
       })
       print('---------------Saved list---------------')
       for book in Saved_List:
         print(book,end='\n')
       break;

      else:
       print('Invalid Number Pick')

   elif choice!='0':
    print('Invalid Input!')
   else:
    print('Program Terminated!')

  with open('C:\\Users\\PMLS\\Downloads\\Reading_List.json','w') as file:
    json.dump(Saved_List,file,indent=4)
    print('Reading List Saved Successfully')

except Exception as e:
  print('Something Went Wrong!',e)