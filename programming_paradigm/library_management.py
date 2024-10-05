class Book():
    def __init__(self, title, author,_is_checked_out ):
        self.title=title
        self.author=author
        self._is_checked_out=_is_checked_out
        
          
     
class library(Book):        
    
    def setup(self):
        self._books=[]
    
    
    def add_book(self):
        
        self._books.append(Book())
        
    def check_out_book(self,title): 
         self._books.remove(title)
         return self._books
         
        
    def return_book(self,title):
        self._books.append(title)
        return self._books
        
     
     
    def list_available_books(self): 
        print(self._books)   
        
                 