import re
from pdfminer.high_level import extract_pages, extract_text

PDF_NAME = 'DevOps.pdf'

# Extract pages.
text = extract_text(PDF_NAME)

# Separetae pages text.
PAGE_SEPARATOR = r'\d \|                                                                                                Link to Join Our WhatsApp group '
pages = re.split(PAGE_SEPARATOR, text)

for index, page in enumerate(pages):
    with open('./pages/page' + str(index + 1) + '.txt', 'w') as file:
        file.write(page)

# Remove header of page.

# Remove footer of page.

# Split paragraphes.

# Verify is the first paragraphe is the start of paragraphe.

# Split the paragraphe by Question mark separator.1