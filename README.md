# rentalfinder
# Vancouver Rental Finder

A rental aggregation and filtering platform focused on Vancouver housing posts from Chinese social media platforms such as Xiaohongshu.

The project extracts visible post content from housing listings, parses key rental information using keyword matching and regular expressions, and organizes listings into a searchable and filterable website.

## Project Goal

Finding rentals in Vancouver through Xiaohongshu can be messy because posts often have:

- duplicated listings
- inconsistent formatting
- missing prices
- unclear locations
- no centralized filtering system

This project aims to convert unstructured housing posts into structured rental data.

## MVP Workflow

```text
Xiaohongshu Housing Post
        ↓
Chrome Extension / Webhook Plugin
        ↓
Extract visible webpage text + URL
        ↓
FastAPI Backend
        ↓
Keyword + Regex Extraction
        ↓
SQLite Database
        ↓
React Frontend
        ↓
Search / Filter / Save Listings
```

## MVP Features

### Rental Information Extraction

The system will extract:

- price
- location
- room type
- move-in date
- utilities and furniture information
- contact information
- original post URL

### Rental Detection

The system will detect whether a post is likely a rental listing using keywords such as:

```text
租房
转租
sublet
lease
rent
studio
1b1b
2b2b
主卧
次卧
```

### Search and Filtering

Users will be able to filter listings by:

- price range
- neighborhood
- room type
- move-in date
- keywords

## Tech Stack

### Frontend

- React
- Tailwind CSS
- Axios

### Backend

- Python
- FastAPI

### Database

- SQLite for the initial MVP
- PostgreSQL as a future upgrade

### Extraction Engine

- Python regular expressions
- keyword matching
- optional LLM integration in future versions

## Project Structure

```text
vancouver-rental-finder/
├── frontend/
│   ├── src/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── extractor.py
│   ├── database.py
│   └── rentals.db
│
├── docs/
│
└── README.md
```

## Planned Future Features

### AI-Powered Extraction

Use LLMs to improve extraction accuracy for messy formatting, slang, and incomplete rental posts.

### Duplicate Listing Detection

Detect reposted or duplicated rental listings.

### Scam Detection

Flag suspicious posts based on unrealistic pricing, incomplete information, or repeated scam patterns.

### Map Integration

Display rental listings on an interactive Vancouver map.

## Why This Project?

This project combines:

- web development
- backend API design
- data extraction
- natural language processing concepts
- database design
- product engineering

It is both practically useful and a strong portfolio project for software engineering internships.

## Development Status

Current phase:

- [ ] Set up backend
- [ ] Build extraction engine
- [ ] Design database schema
- [ ] Build frontend UI
- [ ] Connect webhook pipeline

## Notes

This project does not directly scrape or bypass protected platform systems.

The MVP focuses on extracting user-visible webpage content through browser tooling and organizing the data into a personal rental aggregation platform.

## Author

Joy Tao
Computer Engineering @ UBC
