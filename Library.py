import csv


#fonctions
def add_book() :
    while True :
        try :
            new_book = []
            new_book.append(input("Type the title :  "))
            new_book.append(input("Type the autor :  "))
            new_book.append(input("Type the nature :  "))
            new_book.append(int(input("Type the number of pages :  ")))
            new_book.append(int(input("Type the price($) :  ")))
            return new_book
        except ValueError:
            print("number of pages or price incorrect! try numeric values(ex:23)")


def save_book(new_book) :
    with open("Library.csv",'a') as library :
        writer = csv.writer(library,delimiter=",")
        writer.writerow(new_book)

def clear_library() : # cette fonction permet de supprimer toute la library mais en gardant le header
    clearer = open("Library.csv","w")
    clearer.write("")
    clearer.close()
    header = open("Library.csv","w")
    header.write("title,autor,nature,pages,price\n")
    header.close()

def header_writer() : # J'AI FAIT CETTE fonction pour que le header s'ecrive s'il n'est pas la et vice-versa
    with open("Library.csv","r+") as library :
        reader = csv.reader(library,delimiter=",")
        for line in reader : # je compare la premiere ligne a la chaine de caractere
            header = "title,autor,nature,pages,price"
            if line != header.split(",") :
                clear_library() 
            break

def delete_book() :
    is_name_there = False
    book_name = input("Type the title of the book :  ")
    with open("Library.csv","r+") as library :
        writer = csv.DictWriter(library,fieldnames=["title","autor","nature","pages","price"])#J'use dictwriter pour reecrire le fichier apres chaque delete
        reader = csv.DictReader(library,delimiter=",")
        #reader est un objet de dictionnaire et pour pouvoir supprimer un element je le transform en list
        """for book in reader : #le [:] me permet de faire une copie(slice) de la liste te c'est elle que je parcoure mais je modifie l'original
            if book["title"] == book_name :
                is_name_there = True
                reader.remove(book)
                break
        if  not is_name_there :
            print("name not found in the library")
        clear_library()
        for line in reader :
            writer.writerow(line)"""
        for book in reader :
            if book["title"] == book_name :
                is_name_there = True
                book.clear()
                break
        if  not is_name_there :
            print("name not found in the library")
        clear_library()
        for line in reader :
            writer.writerow(line)

def library_launcher() : 
    header_writer()
    print("Welcome to the portable Library glad to serve you today")
    while True :
        try :
            print("How can we help today?")
            user_choice = input("1. Add a book\n2. Delete a book\n3. Display all books\n4. Clear library\n")
            user_choice = int(user_choice)
            break
        except ValueError :
            print("Try to enter a numeric value (ex:1)")
    match user_choice :
        case 1 :
            new_book = add_book()
            save_book(new_book)
        case 2 :
            delete_book()
        case 4 :
            clear_library()
            print("Library cleared successfully")
        case _ :
            print("incomplet")
        
library_launcher()
    