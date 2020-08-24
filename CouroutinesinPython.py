#Coroutines in Python
def searcher():
    import time
    #some 4 seconds time consuming task
    book = 'This is  a book on haary and code with harry and good'
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print('Your text is in the book')
        else:
            print("Text is not in the book")

search = searcher()
next(search)
input('Press any key')
search.send('Harry')
input('Press any key')
search.send('harry and')
input('Press any key')
search.send('Hey Keshav How are you')
input('Press any key ')
search.send('Hey Ravi How are you')
#search.send('Hey Nishant')



