# Regex package
import re

# Pdfminer.six is a package used to extract data from pdf files.
# - Analyse and group text in humand-readable way.
# - Extract pdf objects into python objects.
# - It could extract text, images and tables.
from pdfminer.high_level import extract_pages, extract_text

import pandas as pd

# # Visualize elements in pdf
# for page_layout in extract_pages("DevOps.pdf"):
#     for element in page_layout:
#         print(element)

# Extract text
text = extract_text("DevOps.pdf", maxpages=5)
# print(text)
QstPattern = re.compile(r"[0-9]+\.\s([A-Za-z0-9]+( [A-Za-z0-9]+)+)\?")
QstMatches = QstPattern.findall(text)


df = pd.DataFrame(QstMatches)
print(df)

