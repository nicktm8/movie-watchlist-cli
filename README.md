# 🎬 Movie Watchlist CLI

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=flat)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen?style=flat)

A Python CLI app structured around a strict separation of concerns: Model → Service → Storage → UI. Simple problem, intentional architecture.

---

## ⚙️ Features

- Add movies to your watchlist with title, release year, genre, and IMDb URL
- View all saved movies in a numbered list
- Remove movies from the watchlist
- Persistent storage — your data is saved between sessions
- Input validation and error handling

---

## 🏗️ Project Structure

```
movie-watchlist-cli/
│
├── models/
│   └── movie.py          # Movie data class
│
├── services/
│   └── movie_manager.py  # Business logic (add, view, remove)
│
├── storage/
│   └── file_handler.py   # File serialization / deserialization
│
├── data/
│   └── library.pkl       # Persistent data storage (auto-created)
│
├── main.py               # CLI entry point
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nicktm8/movie-watchlist-cli.git
cd movie-watchlist-cli
```

2. Run the application:
```bash
python main.py
```

No external dependencies required — uses Python standard library only.

---

## 📷 Usage

When you run the program, you will see a menu:

```
--------------------------------------------------

           Welcome to Movie Watchlist app

--------------------------------------------------
Choose an option:
1. Add movie
2. Remove movie
3. Show all movies
4. Exit

Enter number 1, 2, 3 or 4:
```

### Adding a movie

Select option `1` and enter the required details:

```
Movie title: Inception
Movie release year: 2010
Movie genre: Sci-Fi, Thriller
Movie IMDb URL: https://www.imdb.com/title/tt1375666/
```

### Viewing movies

Select option `3` to display all saved movies:

```
All movies in the watchlist:

1. Title: Inception
   Year:  2010
   Genre: Sci-Fi, Thriller
   IMDb:  https://www.imdb.com/title/tt1375666/
--------
```

---

## 🧱 Architecture

The application follows a layered architecture with clear separation of concerns:

| Layer | File | Responsibility |
|---|---|---|
| Model | `models/movie.py` | Represents a single movie (data only) |
| Service | `services/movie_manager.py` | Business logic — add, view, remove |
| Storage | `storage/file_handler.py` | Save and load data using `pickle` |
| Entry point | `main.py` | CLI menu and user interaction |

**Data flow:**
```
User → main.py → MovieManager → FileHandler → data/library.pkl
```

---

## 🛠️ Planned Improvements

- [ ] Migrate from `pickle` to JSON for human-readable storage
- [ ] Search and filter movies by genre or year
- [ ] Input validation (URL format, year range)
- [ ] Unit tests
- [ ] Rich terminal output using the `rich` library

---

## 🧠 Technical Highlights

- **OOP design** — `Movie` class models data cleanly; `MovieManager` owns business logic; `FileHandler` isolates I/O
- **Layered architecture** — strict separation between data, logic, storage, and UI layers
- **Persistent storage** — serialization and deserialization with Python's `pickle` module
- **Defensive file handling** — auto-creates `data/` directory if missing; gracefully handles empty watchlist
- **Zero dependencies** — built entirely with Python standard library

---

## Changelog
 
### v0.1.0 — Initial Release
- Add `Movie` model with title, year, genre, and IMDb URL
- Add `FileHandler` with pickle-based save and load
- Add `MovieManager` with add, view, and remove logic
- Add CLI interface with main menu loop
- Auto-create `data/` directory on first save
 
---

## Contributing
 
Contributions, suggestions, and feedback are welcome — especially since there's plenty of room to improve.
 
1. Fork the repository
2. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```
3. Commit your changes:
```bash
git commit -m "Add your feature"
```
4. Push to your branch:
```bash
git push origin feature/your-feature-name
```
5. Open a Pull Request
 
If you spot a bug or have an idea, feel free to open an [issue](https://github.com/nicktm8/movie-watchlist-cli/issues).
 
---

## 👤 Author

Nick Tem  
GitHub: https://github.com/nicktm8
