import bs4 as bs
import urllib.request
stop_words=["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although",
            "always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around"
            , "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside",
            "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de",
            "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc",
            "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for",
            "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence",
            "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in",
            "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may",
            "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither",
            "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once",
            "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put",
            "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six",
            "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that",
            "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick",
            "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards","twelve",
            "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence","i","w",
            "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever",
            "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the","b","c","d",
            "e","f","g","h","j","k","l","m","n","o","ö","p","r","s","u","q","z","x","y","t","|","-3","←","$","count","10","0","1","2","3","4","5","6","7","8","9","line"]
print("WELCOME TO THE BOOK ANALYSIS PROGRAM")
print()
book_num=int(input("how many books do you want to see : "))
if book_num==1 :
   book_name=input("please enter a book name : ") 
elif book_num==2 :
   book_name=input("please enter a book name : ")
   book_name_2=input("please enter a book name : ")          
if book_num==1 or book_num==2 : #If the number of books is 1 or 2, the user will be able to get information about the frequency words of a book or compare 2 books.  
   num_try=0
   check=True
   while (check):
      main_url="https://en.wikibooks.org/wiki/" #When we look at the html code content of wikibooks, this part is common for every book so I said the main url to this part.
      book_name=book_name.replace(" ","_")
      if num_try==0:    
         final_url_2=main_url+book_name+"/Print_version"  #i wrote alternatives to which url end the book can end with and my loop will continue until reach the correct link
      elif num_try==1:
            final_url_2=main_url+book_name+"/print_version"
      elif num_try==2:
            final_url_2=main_url+book_name+"/Print_Version"      
      elif num_try==3:
            final_url_2=main_url+book_name+"/printable_version"                 
      try:
         source = urllib.request.urlopen(final_url_2).read()
         check=False         
      except urllib.error.HTTPError:
         num_try+=1
         check=True
         continue        
   soup = bs.BeautifulSoup(source, 'lxml')   
   if book_num==2: #If the user wants to see 2 books, I applied the things I applied for the 1st book here for the 2nd book.
      num_try=0
      check=True
      while (check):
         main_url="https://en.wikibooks.org/wiki/" #When we look at the html code content of wikibooks, this part is common for every book so I said the main url to this part.
         book_name_2=book_name_2.replace(" ","_")
         if num_try==0:
            final_url_2=main_url+book_name_2+"/Print_version" 
         elif num_try==1:
            final_url_2=main_url+book_name_2+"/print_version"
         elif num_try==2:
            final_url_2=main_url+book_name+"/Print_Version"  
         elif num_try==3:
            final_url_2=main_url+book_name_2+"/printable_version"                      
         try:
            source = urllib.request.urlopen(final_url_2).read()
            check=False           
         except urllib.error.HTTPError:
            num_try+=1
            check=True
            continue            
      soup_2 = bs.BeautifulSoup(source, 'lxml')            
   if book_num==1: #If the user selects 1 book, a text file is opened for only 1 book and the text of the relevant book in the mw-parser-output class of the wikibooks site is transferred to the text.
      f = open("book.txt", "w") #i print the printable book to the text of book.txt
      for i in soup.find_all(class_="mw-parser-output"):
         f.write(i.text.encode('utf8').decode('ascii', 'ignore'))
      f.close()
   if book_num==2: #i print the second book to the text of book.txt
      f = open("book.txt", "w")
      for i in soup.find_all(class_="mw-parser-output"):
         f.write(i.text.encode('utf8').decode('ascii', 'ignore'))
      f.close()
      f_2 = open("book_2.txt", "w")
      for i in soup_2.find_all(class_="mw-parser-output"):
         f_2.write(i.text.encode('utf8').decode('ascii', 'ignore'))
         f_2.close()
   replace_chars="!,.;:(#?[]&)=>'<&@^%'_-0123456789*/`*\"{}|~\n\t" #I take the words in the text from the 0th index of the word until I encounter one of these chars. Thanks to this, I made a more accurate count
   b=[] #I collected the situation that I did not list stop words and other unnecessary things in list b for book 1.
   f=open("book.txt")
   a=f.readlines()  
   for lines in a:
       line=lines.split(" ") #In these loops I separate my book by lines and spaces.
       if len(line)==1 :
          continue
       else :
          for words in line:         
             words=words.lower() #With to.lower(), I converted all the words of my text to lowercase. 
             for chars in replace_chars:
                     if chars in words: #In this loop, I check my word until it comes to one of the characters I keep in 'replace char' from the first index, and 
                                        #when it comes across one of these characters, I accept my word only up to the index it coincides with.                       
                           index_of_chars = words.index(chars)
                           words = words.replace(chars," ")
                           words = words[0:index_of_chars]     
             checking_stop=False #in my loop here, if the word is stop words or "" space, I don't add that word to my list.
             for stop_words_element in stop_words:
               if (words==stop_words_element) or words=='':
                  checking_stop=True
                  break
             if checking_stop==False:  
                b.append(words)             
   if book_num==2 :
      d=[] #I collected the situation that I did not list stop words and other unnecessary things in list d for book 2.
      f_2=open("book_2.txt")
      x=f_2.readlines()
      for lines in x:
          line=lines.split(" ") 
          if len(line)==1 :
             continue
          else :
             for words in line:
                words=words.lower()                                        
                for chars in replace_chars:
                     if chars in words:
                           index_of_chars = words.index(chars)
                           words = words.replace(chars," ")
                           words = words[0:index_of_chars]                        
                checking_stop=False
                for stop_words_element in stop_words:
                  if (words==stop_words_element) or words=='':
                     checking_stop=True
                     break
                if checking_stop==False:  
                      d.append(words)                  
      distinct_words_1=[] #If the word in the 1st book is not in the 2nd, I add this word to my distinct1 list.
      for word3 in b :
         if word3 not in d :
            distinct_words_1.append(word3)  
      distinct_words_2=[] #If the word in the 2nd book is not in the 1st, I add this word to my distinct2 list.
      for word6 in d :
         if word6 not in b:
            distinct_words_2.append(word6)     
   def CountWords(text_words): # This function counts the words and keeps them 
       high_num = 0
       Counted_words={}
       Word_Count = {}    
       for wordss in text_words: # Counts every word
           if wordss not in Word_Count:
               Word_Count[wordss] = 1
           else:
               Word_Count[wordss] =  Word_Count[wordss] + 1            
       for a in range (len(text_words)): # Keep first (len(text_words)) word with high frequences
           for key in Word_Count.keys():
               if Word_Count[key] > high_num and key not in Counted_words: #finds highest frequence words
                   high_num = Word_Count[key]
                   high_string = key
           Counted_words[high_string] = high_num
           high_num = 0  #After each word and number, I equate the word to the blank and the number back to 0.
           high_string = " "
       return Counted_words
   freq_num=input("Do you want to see frequencies words in book? İf you want please enter Y/yes :")
   #Here I ask the user if she wants to see a word or not, if she wants, I ask the user how many words the user wants to see first,
   #and if the user doesn't, I get the number 20 as a constant.
   if freq_num=="Y" or freq_num=="yes" :
      frequencies_num=int(input("How many word frequencies you wish to see in this document : "))
   elif freq_num!= "Y" and freq_num!= "yes":
      frequencies_num=20
   print()
   if book_num==1: #If the user selects 1 book, I will print the most common words in the book here.
      c = CountWords(b)
      print("BOOK 1:", book_name)
      print('{:<4s}{:<12s}{:>12s}'.format("NO","WORD","FREQ_1")) #I used the format method to line up properly. "d"for int and "s" for string value
      continue_count=False
      start=0
      for key in c :
         print('{:<4d}{:<12s}{:>12d}'.format(start+1,key,c[key]))
         start+=1    
         if start==frequencies_num: #I return the loop for the frequency_num I received from the user or the fixed number of 20 that I chose.
            continue_count=True
         if continue_count==True:
            break
   print()
   if book_num==2: #If the user selects 2 book, I will print the common and distinct words in the books here.
      freq_1=CountWords(b)
      freq_2=CountWords(d)
      print()
      print("BOOK 1:", book_name)
      print("BOOK 2:", book_name_2)
      print("COMMON WORDS")
      print('{:<4s}{:<12s}{:>12s}{:>12s}{:>12s}'.format("NO","WORD","FREQ_1"," FREQ_2","FREQ_SUM"))
      continue_count=False
      i=0   
      for key in freq_1: #If the words in the 1st book are also in the 2nd, I call my funtion and print them on the screen with their numbers.
         if key in freq_2:
            print('{:<4d}{:<12s}{:>12d}{:>12d}{:>12d}'.format(i+1,key, freq_1[key],freq_2[key],freq_1[key]+freq_2[key]))
            i+=1
            if i==frequencies_num:
               continue_count=True
         if continue_count==True:
            break
      print()
      m=CountWords(distinct_words_1) #i called my function for distinct1 list
      print()
      print("BOOK 1:", book_name)
      print("DISTINCT WORDS")
      print('{:<4s}{:<12s}{:>10s}'.format("NO","WORD","FREQ_1"))
      continue_count=False
      s=0
      for key in m :  
         print('{:<4d}{:<12s}{:>10d}'.format(s+1,key,m[key]))
         s+=1
         if s==frequencies_num:
            continue_count=True
         if continue_count==True:
            break
      print()
      n=CountWords(distinct_words_2) #i called my function for distinct1 list
      print()
      print("BOOK 2:", book_name_2)
      print("DISTINCT WORDS")
      print('{:<4s}{:<12s}{:>10s}'.format("NO","WORD","FREQ_2"))
      continue_count=False
      start=0
      for key in n :
         print('{:<4d}{:<12s}{:>10d}'.format(start+1,key,n[key]))
         start+=1 
         if start==frequencies_num:
            continue_count=True
         if continue_count==True:
            break
else : #If the user enters a number other than 1 or 2, none of the above operations occur and I give the user a warning message.
   print("please enter 1 or 2 for the see the book")
input()



   
