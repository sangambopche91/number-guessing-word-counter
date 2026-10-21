# Number Guessing Game & Word Counter

## Project Overview
A beginner-friendly Python command-line application that combines a number guessing game with a text-file word counter.

## Features
- Random number generation from 1 to 100
- Seven valid guessing attempts
- High/low hints and score tracking
- Best score retained during the current session
- Text file reading with UTF-8 encoding
- Case-insensitive word frequency analysis
- Top 10 most common words
- Total and unique word counts
- Input validation and missing-file handling

## Scoring Rule
The player starts with a potential score of 100 points. Each incorrect valid guess reduces the score by 10 points. A correct guess on the first attempt earns 100 points. The score cannot fall below zero, and failure to guess within seven attempts earns zero.

## Requirements
Python 3.10 or newer. No external packages are required.

## How to Run
1. Download `main.py` and `sample.txt`.
2. Open a terminal in the project directory.
3. Run `python main.py`.
4. Select an option from the main menu.

## Word Counter
The word counter converts text to lowercase, removes punctuation, and uses Python's `collections.Counter` to report the ten most frequent words, total words, and unique words.

Common words such as "the" and "and" may dominate frequency results.

## Files
- `main.py` — application source code
- `sample.txt` — sample input text
