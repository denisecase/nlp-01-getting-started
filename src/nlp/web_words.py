"""web_words.py - Project script (example).

Purpose

  Retrieve a web page, extract its text, count word frequencies,
  and visualize the results.

Analytical Questions

- What terms dominate this page?
- What topic does the vocabulary suggest?
- What noise appears from navigation or markup?
- What preprocessing steps might improve results?

Notes:
- This example performs simple frequency analysis.
- More advanced text processing techniques will be introduced later.

Run from root project folder with:

  uv run python -m nlp.web_words
"""

# ============================================================
# Section 1. Setup and Imports (includes logging deps)
# ============================================================
import logging
from pathlib import Path

from bs4 import BeautifulSoup
from datafun_toolkit.logger import get_logger, log_header, log_path
import matplotlib.pyplot as plt
import polars as pl
import requests
from wordcloud import WordCloud

print("Imports complete.")

# ============================================================
# Configure Logging (script execution only)
# ============================================================

LOG: logging.Logger = get_logger("CI", level="DEBUG")

ROOT_PATH: Path = Path.cwd()
NOTEBOOKS_PATH: Path = ROOT_PATH / "notebooks"
SCRIPTS_PATH: Path = ROOT_PATH / "scripts"

log_header(LOG, "NLP")
LOG.info("START script.....")

log_path(LOG, "ROOT_PATH", ROOT_PATH)
log_path(LOG, "NOTEBOOKS_PATH", NOTEBOOKS_PATH)
log_path(LOG, "SCRIPTS_PATH", SCRIPTS_PATH)


# ============================================================
# Section 2. Retrieve a Web Page (as HTML text)
# ============================================================

# Choose a page to analyze.
# The Shakespeare page is simple and stable.
# The Wikipedia page is interesting, but requires a User-Agent header.
# url: str = "https://shakespeare.mit.edu/romeo_juliet/full.html"
url: str = "https://en.wikipedia.org/wiki/Natural_language_processing"

# Some sites reject requests that look like anonymous scripts.
# This header helps the request look more like a normal browser visit.
headers: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (compatible; NLP-Course-Example/1.0)"
}

# Request the page and stop with an error if the request fails.
response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

# Store the raw HTML text.
html: str = response.text

print(f"Downloaded {len(html):,} characters from:")
print(url)


# ============================================================
# Section 3. Parse the HTML (into a BeautifulSoup tree)
# ============================================================

# BeautifulSoup() takes raw HTML text
# and builds a parse tree (a structured representation of the document)
# we assign to a variable named soup (short for "soup of tags").

# Example Input:
# "<html><body><p>Hello</p></body></html>"

# Example BeautifulSoup parse tree:
# html
#  └── body
#       └── p
#            └── "Hello"

# This makes it easier to extract text and inspect page structure.

# Call BeautifulSoup with the raw HTML and a parser (lxml is fast and lenient).
soup: BeautifulSoup = BeautifulSoup(html, "lxml")

print("HTML parsed successfully.")
print(type(soup))


# ============================================================
# Section 4. Extract Visible Text from the HTML
# ============================================================

# Extract visible text from the page with get_text() method.
# separator=" " inserts spaces between chunks of text.
# strip=True removes leading and trailing whitespace.
text: str = soup.get_text(separator=" ", strip=True)

# Use [0:1000] to show only the first 1000 characters of the text.
# Or [:1000] gives the same result, since the start index defaults to 0.
print("First 1000 characters of extracted text:")
print(text[:1000])


# ============================================================
# Section 5. Clean the Text (split, lowercase, remove punctuation)
# ============================================================

# Split the text into rough word-like pieces using whitespace.
words: list[str] = text.split()
count_of_words: int = len(words)

print("First 20 raw words:")
print(words[:20])
print(f"Total raw words: {count_of_words:,}")

# Convert all words to lowercase so "Language" and "language"
# are counted as the same word.
# Use a list comprehension (concise list to list transformation)
# that creates a new lowercase list from a list of words.
words = [word.lower() for word in words]

# Strip out (remove) common punctuation from the beginning and end of words.
# Keep only tokens longer than 3 characters to reduce noise.
# Again, a list comprehension is great for simple list-to-list transformations.
clean_words: list[str] = [
    word.strip(".,:;!?()[]\"'") for word in words if len(word) > 3
]
count_of_clean_words: int = len(clean_words)

print("First 20 cleaned words:")
print(clean_words[0:20])
print(f"Total cleaned words: {count_of_clean_words:,}")


# ============================================================
# Section 6. Build a Frequency Table with Polars
# ============================================================


# For working with tabular data,
# Polars is faster and smaller than pandas,
# has a more modern API, and the concepts are similar.

# Create a Polars DataFrame (df) with one row per word with a column named "word".
df: pl.DataFrame = pl.DataFrame({"word": clean_words})

# Group by word, count occurrences, and sort from most common to least common.
# This is a powerful pattern for counting and summarizing data in Polars.
# Function chain: group_by() -> len() -> sort()
freq_df: pl.DataFrame = df.group_by("word").len().sort("len", descending=True)

print("Top 20 most frequent words:")
print(freq_df.head(20))


# ============================================================
# Section 7. Build "Most Frequent Words" Bar Chart
# ============================================================

# Focus on the 10 most common words for a simple bar chart.
# Use head(10) to get the top 10 rows of the frequency DataFrame.
top_df: pl.DataFrame = freq_df.head(10)

# Make the figure size larger for better readability.
# 10 inches wide by 5 inches tall is a common size for bar charts.
plt.figure(figsize=(10, 5))

# Set the x-axis to the "word" column (the unique words).
# Set the y-axis to the "len" column (the counts).
plt.bar(top_df["word"], top_df["len"])

# Define ax as the current axes (gca = get current axes)
# so we'll be able to modify tick parameters.
ax = plt.gca()

# Set the tick labels on the x-axis
# to rotate 45 degrees for better readability,
ax.tick_params(axis="x", labelrotation=45)

plt.title("Most Frequent Words")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# ============================================================
# Section 8. Build a Word Cloud
# ============================================================

# For this, we want a Python dictionary
# mapping words to their frequencies.
# We can use the zip() function to combine the "word" and "len" columns into a dictionary.
# First, convert the frequency dfs to lists with to_list(),
# then zip() them together into a dictionary.
# strict=True ensures both lists are the same length.
freq_dict: dict[str, int] = dict(
    zip(freq_df["word"].to_list(), freq_df["len"].to_list(), strict=True)
)
print("Sample of word frequencies:")
for word, freq in list(freq_dict.items())[:10]:
    print(f"{word}: {freq}")

# Build a word cloud where larger words occur more frequently in the text.
# Set width and height in pixels and set the background color.
wc: WordCloud = WordCloud(width=1000, height=500, background_color="white")

# Generate the word cloud from the frequency dictionary.
wc.generate_from_frequencies(freq_dict)

# Set the figure size in inches
plt.figure(figsize=(12, 6))

# Display the word cloud image with imshow() and turn off axes for a cleaner look.
plt.imshow(wc)
plt.axis("off")
plt.title("Word Cloud")
plt.show()

# ============================================================
# LOG THE END (only in the script)
# ============================================================

LOG.info("========================")
LOG.info("Pipeline executed successfully!")
LOG.info("========================")
LOG.info("END main()")
