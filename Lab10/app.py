import xml.etree.ElementTree as ET
from datetime import datetime

def process_library(xml_file):
    try:
        # Парсинг XML файла
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Вывод всех книг
        print("Список всех книг в библиотеке:")
        print("=" * 50)
        total_price = 0
        book_count = 0
        
        for book in root.findall('book'):
            book_id = book.get('id')
            title = book.find('title').text
            author = book.find('author').text
            year = int(book.find('year').text)
            genre = book.find('genre').text
            price = float(book.find('price').text)
            
            print(f"ID: {book_id}")
            print(f"Название: {title}")
            print(f"Автор: {author}")
            print(f"Год: {year}")
            print(f"Жанр: {genre}")
            print(f"Цена: ${price:.2f}")
            print("-" * 50)
            
            total_price += price
            book_count += 1
        
        # Вычисление средней цены
        if book_count > 0:
            avg_price = total_price / book_count
            print(f"\nСредняя цена книг: ${avg_price:.2f}")
        
        # Фильтрация книг по критериям
        filter_genre = input("\nВведите жанр для фильтрации (оставьте пустым для пропуска): ")
        filter_year = input("Введите год для фильтрации (оставьте пустым для пропуска): ")
        
        print("\nРезультаты фильтрации:")
        print("=" * 50)
        filtered_books = 0
        
        for book in root.findall('book'):
            title = book.find('title').text
            author = book.find('author').text
            year = int(book.find('year').text)
            genre = book.find('genre').text
            price = float(book.find('price').text)
            
            # Проверка критериев фильтрации
            genre_match = not filter_genre or genre.lower() == filter_genre.lower()
            year_match = not filter_year or year == int(filter_year)
            
            if genre_match and year_match:
                print(f"Название: {title}, Автор: {author}, Год: {year}, Жанр: {genre}, Цена: ${price:.2f}")
                filtered_books += 1
        
        if filtered_books == 0:
            print("Книги по заданным критериям не найдены.")
            
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
    except ET.ParseError:
        print("Ошибка: файл имеет неверный формат XML.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск обработки
process_library("library.xml")
