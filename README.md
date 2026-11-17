# Book Search & Reading List Application.

## 1. Project Overview
The **Book Search & Reading List Application** is a Python-based project that allows users to search for books using the Open Library API and save their favourite books into a local JSON file.

Users can search for books by title, author, or both. The application retrieves live book information from the API, displays book details and cover image URLs, and allows users to select and save books to their personal reading list.

## 2. Features
- **Search by Title:** Find books using their titles.
- **Search by Author:** Find books written by a specific author.
- **Search by Both:** Search using both book title and author name.
- **Live API Integration:** Fetch real-time book information from the Open Library API.
- **Book Details:** Display book title, author, first publication year, and edition count.
- **Book Cover URLs:** Retrieve and display book cover image URLs when available.
- **JSON File Storage:** Save selected books and their information in a local JSON file.

## 3. Technologies & Libraries Used
- **Python:** Main programming language.
- **Requests:** Send HTTP GET requests and retrieve data from the API.
- **JSON:** Convert API responses into Python objects and python list into json format.
- **Open Library API:** Retrieve live book information and cover details.

## 4. API Integration
This project uses the Open Library Search API to retrieve book information.
**API Endpoint:**
(https://openlibrary.org/search.json)
**Book Cover API:**
(https://covers.openlibrary.org/b/id/{cover_id}-L.jpg)
L-represent large size, M-represent medium size, S-represent small size.

The application sends search parameters to the API depending on the user's selection:
- `?title='power'`: Search using a book title.
- `?author='robert greene'`: Search using an author's name.
- `?title='power'&author='robert greene'`: Search using both parameters.

The API returns book information in JSON format, which is processed and displayed by the application.
**No API key is required.**

## 5. Project Requirements
### Software Requirements
- Google Colab or 
- Visual Studio Code or any Python-compatible IDE.
- Git (for cloning the repository).

### Python Libraries
| Library | Purpose |
|---|---|
| requests | Sending HTTP requests to the API |
| json | Reading, writing, converting JSON data |

## 6. Installation and Setup
Open your terminal and run:
# Clone the repository
git clone https://github.com/ayoush2026/python-reading-list.git
# Navigate to the project directory
cd python-reading-list
# Install dependencies
pip install requests
# Run the application
python main.py

## 7. Project Demonstration
### Step 1: Configure Reading List Storage.
Before running the application, specify the location where you want to save Reading_List.json in the file-handling section of main.py
### Step 2: Choose a Search Option
The application provides three search options:
```text
Search Book By: Pick Number
1. Title
2. Author
3. Both
```
### Step 3: Enter Search Information
Depending on your selection, enter the book title, author's name, or both.
### Step 4: View Search Results
The application displays available book information, including:
- Book number
- Title
- Author name
- First publication year
- Number of editions
- Cover image URL (when available)
### Step 5: Save Books
After viewing the search results, you can select the book number of any book you want to save.
The application maintains a saved Map and prevents duplicate selections.
### Step 6: Save Your Reading List
Enter `0` when you finish selecting books.
The selected books are saved in a JSON file.


## 8. Sample Output
The following is an illustrative example of the application output. Actual results depend on the API response.
```text
Search Book By: Pick Number
1.Title
2.Author
3.Both
1
Enter the Title of Book:power
Results Found: 118225


----------------Book Search Results----------------
Number: 0
Image Url: https://covers.openlibrary.org/b/id/6424160-L.jpg
Title: The 48 Laws of Power
Author Name: ['Robert Greene']
First Published: 1998
Editions: 51

Number: 1
Image Url: https://covers.openlibrary.org/b/id/551262-L.jpg
Title: The Power of Now
Author Name: ['Eckhart Tolle']
First Published: 1997
Editions: 45

Number: 2
Image Url: https://covers.openlibrary.org/b/id/6553019-L.jpg
Title: The Power of Your Subconscious Mind
Author Name: ['Joseph Murphy']
First Published: 1963
Editions: 132

----


Number: 98
Image Url: https://covers.openlibrary.org/b/id/4818037-L.jpg
Title: Mind power
Author Name: ['John Kehoe']
First Published: 1990
Editions: 2

Number: 99
Image Url: https://covers.openlibrary.org/b/id/411267-L.jpg
Title: Power and interdependence
Author Name: ['Robert O. Keohane']
First Published: 1977
Editions: 5

Do you Want To Save Any Book:
1. Yes
0. Save File!
Enter: 1
Enter The Number Of Book You Want To Save no>=0 and no<100
Enter: 1
---------------Saved list---------------
{'id': '/works/OL5727686W', 'title': 'The Power of Now', 'author': ['Eckhart Tolle'], 'edition_count': 45, 'cover_id': 551262, 'publish_year': 1997, 'language': ['ind', 'spa', 'eng'], 'image_url': 'https://covers.openlibrary.org/b/id/551262-L.jpg'}

Do you Want To Save Any Book:
1. Yes
0. Save File!
Enter: 1
Enter The Number Of Book You Want To Save no>=0 and no<100
Enter: 0
---------------Saved list---------------
{'id': '/works/OL5727686W', 'title': 'The Power of Now', 'author': ['Eckhart Tolle'], 'edition_count': 45, 'cover_id': 551262, 'publish_year': 1997, 'language': ['ind', 'spa', 'eng'], 'image_url': 'https://covers.openlibrary.org/b/id/551262-L.jpg'}

{'id': '/works/OL1968368W', 'title': 'The 48 Laws of Power', 'author': ['Robert Greene'], 'edition_count': 51, 'cover_id': 6424160, 'publish_year': 1998, 'language': ['fre', 'ind', 'spa', 'por', 'eng', 'ger', 'tur', 'rus', 'ara'], 'image_url': 'https://covers.openlibrary.org/b/id/6424160-L.jpg'}

Do you Want To Save Any Book:
1. Yes
0. Save File!
Enter: 1
Enter The Number Of Book You Want To Save no>=0 and no<100
Enter: 7
---------------Saved list---------------
{'id': '/works/OL5727686W', 'title': 'The Power of Now', 'author': ['Eckhart Tolle'], 'edition_count': 45, 'cover_id': 551262, 'publish_year': 1997, 'language': ['ind', 'spa', 'eng'], 'image_url': 'https://covers.openlibrary.org/b/id/551262-L.jpg'}

{'id': '/works/OL1968368W', 'title': 'The 48 Laws of Power', 'author': ['Robert Greene'], 'edition_count': 51, 'cover_id': 6424160, 'publish_year': 1998, 'language': ['fre', 'ind', 'spa', 'por', 'eng', 'ger', 'tur', 'rus', 'ara'], 'image_url': 'https://covers.openlibrary.org/b/id/6424160-L.jpg'}

{'id': '/works/OL41258W', 'title': 'Absolute Power', 'author': ['David Baldacci'], 'edition_count': 52, 'cover_id': 7121965, 'publish_year': 1995, 'language': ['fre', 'vie', 'und', 'por', 'ger', 'dut', 'eng'], 'image_url': 'https://covers.openlibrary.org/b/id/7121965-L.jpg'}

Do you Want To Save Any Book:
1. Yes
0. Save File!
Enter: 1
Enter The Number Of Book You Want To Save no>=0 and no<100
Enter: 99
---------------Saved list---------------
{'id': '/works/OL5727686W', 'title': 'The Power of Now', 'author': ['Eckhart Tolle'], 'edition_count': 45, 'cover_id': 551262, 'publish_year': 1997, 'language': ['ind', 'spa', 'eng'], 'image_url': 'https://covers.openlibrary.org/b/id/551262-L.jpg'}

{'id': '/works/OL1968368W', 'title': 'The 48 Laws of Power', 'author': ['Robert Greene'], 'edition_count': 51, 'cover_id': 6424160, 'publish_year': 1998, 'language': ['fre', 'ind', 'spa', 'por', 'eng', 'ger', 'tur', 'rus', 'ara'], 'image_url': 'https://covers.openlibrary.org/b/id/6424160-L.jpg'}

{'id': '/works/OL41258W', 'title': 'Absolute Power', 'author': ['David Baldacci'], 'edition_count': 52, 'cover_id': 7121965, 'publish_year': 1995, 'language': ['fre', 'vie', 'und', 'por', 'ger', 'dut', 'eng'], 'image_url': 'https://covers.openlibrary.org/b/id/7121965-L.jpg'}

{'id': '/works/OL4629903W', 'title': 'Power and interdependence', 'author': ['Robert O. Keohane'], 'edition_count': 5, 'cover_id': 411267, 'publish_year': 1977, 'language': ['eng'], 'image_url': 'https://covers.openlibrary.org/b/id/411267-L.jpg'}

Do you Want To Save Any Book:
1. Yes
0. Save File!
Enter: 1
Enter The Number Of Book You Want To Save no>=0 and no<100
Enter: 1
this book already exit.
Enter The Number Of Book You Want To Save no>=0 and no<100
Enter: 6
---------------Saved list---------------
{'id': '/works/OL5727686W', 'title': 'The Power of Now', 'author': ['Eckhart Tolle'], 'edition_count': 45, 'cover_id': 551262, 'publish_year': 1997, 'language': ['ind', 'spa', 'eng'], 'image_url': 'https://covers.openlibrary.org/b/id/551262-L.jpg'}

{'id': '/works/OL1968368W', 'title': 'The 48 Laws of Power', 'author': ['Robert Greene'], 'edition_count': 51, 'cover_id': 6424160, 'publish_year': 1998, 'language': ['fre', 'ind', 'spa', 'por', 'eng', 'ger', 'tur', 'rus', 'ara'], 'image_url': 'https://covers.openlibrary.org/b/id/6424160-L.jpg'}

{'id': '/works/OL41258W', 'title': 'Absolute Power', 'author': ['David Baldacci'], 'edition_count': 52, 'cover_id': 7121965, 'publish_year': 1995, 'language': ['fre', 'vie', 'und', 'por', 'ger', 'dut', 'eng'], 'image_url': 'https://covers.openlibrary.org/b/id/7121965-L.jpg'}

{'id': '/works/OL4629903W', 'title': 'Power and interdependence', 'author': ['Robert O. Keohane'], 'edition_count': 5, 'cover_id': 411267, 'publish_year': 1977, 'language': ['eng'], 'image_url': 'https://covers.openlibrary.org/b/id/411267-L.jpg'}

{'id': '/works/OL8315351W', 'title': 'Powerful Stranger', 'author': ['Patricia Wilson'], 'edition_count': 2, 'cover_id': 8225146, 'publish_year': 1993, 'language': ['eng'], 'image_url': 'https://covers.openlibrary.org/b/id/8225146-L.jpg'}

Do you Want To Save Any Book:
1. Yes
0. Save File!
Enter: 0
File Saved!
Reading List Saved Successfully
```

## 9. Reading List Storage
The application stores selected books in a JSON file named:`Reading_List.json`

Each saved book contains the following information:

- `id`: Open Library book identifier.
- `title`: Book title.
- `author`: Author name.
- `edition_count`: Number of editions.
- `cover_id`: Book cover identifier.
- `publish_year`: First publication year.
- `language`: Available language information.
- `image_url`: Book cover image URL.

### Example JSON Structure

```json
[
    {
        "id": "/works/OL...",
        "title": "Python Crash Course",
        "author": ["Eric Matthes"],
        "edition_count": 15,
        "cover_id": 123456,
        "publish_year": 2015,
        "language": ["eng"],
        "image_url": "https://covers.openlibrary.org/b/id/123456-L.jpg"
    }
]
```

## 10. Project Structure

```text
python-reading-list/
│
├── main.py
├── README.md
├── .gitignore
```
