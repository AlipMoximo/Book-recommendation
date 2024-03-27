import tkinter as tk
from tkinter import messagebox
import requests

# Google Books API base URL
BASE_URL = "https://www.googleapis.com/books/v1/volumes"

def search_books(query, max_results=5):
    """Search books based on a query."""
    params = {
        'q': query,
        'maxResults': max_results
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data.get('items', [])

def get_book_details(book_id):
    """Get details of a specific book by its ID."""
    url = f"{BASE_URL}/{book_id}"
    response = requests.get(url)
    data = response.json()
    return data

def recommend_books(preferences):
    """Recommend books based on user preferences."""
    query = " ".join(preferences)
    books = search_books(query)
    return books

def get_recommendations():
    """Get recommendations based on user input."""
    preferences = [
        reading_history_entry.get(),
        genres_entry.get(),
        authors_entry.get(),
        ratings_entry.get()
    ]
    recommended_books = recommend_books(preferences)
    if recommended_books:
        recommended_list.delete(0, tk.END)
        for book in recommended_books:
            volume_info = book.get('volumeInfo', {})
            title = volume_info.get('title', 'Unknown Title')
            authors = volume_info.get('authors', ['Unknown Author'])
            recommended_list.insert(tk.END, f"{title} by {', '.join(authors)}")
    else:
        messagebox.showinfo("No Results", "No books found based on your preferences.")

def main():
    global reading_history_entry, genres_entry, authors_entry, ratings_entry, recommended_list

    root = tk.Tk()
    root.title("Monica's book recommendations")

    reading_history_label = tk.Label(root, text="What is your reading history?")
    reading_history_label.pack()
    reading_history_entry = tk.Entry(root, width=50)
    reading_history_entry.pack()

    genres_label = tk.Label(root, text="What Genres do you prefer?")
    genres_label.pack()
    genres_entry = tk.Entry(root, width=50)
    genres_entry.pack()

    authors_label = tk.Label(root, text="Who is the author?")
    authors_label.pack()
    authors_entry = tk.Entry(root, width=50)
    authors_entry.pack()

    ratings_label = tk.Label(root, text="Book, Author ratings")
    ratings_label.pack()
    ratings_entry = tk.Entry(root, width=50)
    ratings_entry.pack()

    recommend_button = tk.Button(root, text="Get Recommendations", command=get_recommendations)
    recommend_button.pack()

    recommended_list = tk.Listbox(root, width=80)
    recommended_list.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
