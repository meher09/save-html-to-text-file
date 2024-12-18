# HTML Content Extractor for Aston University Page

<h2 align="center">This content is created for educational purposes only.</h2>

This Python script extracts the main content from the following URL:
[https://nwc.education/aston-university-official-agent-in-bangladesh/](https://nwc.education/aston-university-official-agent-in-bangladesh/),
removes unnecessary HTML tags and class attributes, and saves the cleaned content into two separate text files:

- One file contains the HTML content with `<div>` tags and `class` attributes.
- Another file contains the basic HTML elements (headings, images, lists, etc.) with all `<div>` tags and `class` attributes removed.

## Features

- Sends a request to the URL to fetch the HTML content.
- Extracts the second occurrence of the `wpb_wrapper` class.
- Saves two versions of the content:
  1. **With div and class attributes**: Contains all original HTML tags and classes.
  2. **Without div and class attributes**: Removes all `div` tags and class attributes, leaving only basic HTML elements like headings, images, lists, tables, etc.
  3. **With div and class attributes Pretify Fomat**: Contains all original HTML tags and classes and output will be in pretty format.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

To get started, clone or download this repository, and install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

1. **Download the Python script.**

2. **Run the script**:

   ```bash
   python sscript_name.py
   ```

3. The script will send a request to the URL and save the extracted content into two text files:

   - `second_wpb_wrapper_content_with_div.txt` (content with `div` and `class` attributes)
   - `second_wpb_wrapper_cleaned_content.txt` (content without `div` and `class` attributes)
   - ` second_wpb_wrapper_content_pretty.txt` (content witho `div` and `class` attributes and pretty format)

4. The files will be saved in the same directory as the script.

## How It Works

1. The script sends an HTTP request to the provided URL: [https://nwc.education/aston-university-official-agent-in-bangladesh/](https://nwc.education/aston-university-official-agent-in-bangladesh/).
2. It uses BeautifulSoup to parse the HTML content.
3. It finds all elements with the `wpb_wrapper` class and selects the second occurrence.
4. It saves two versions of the extracted content:
   - One version with the original HTML structure.
   - Another version with all `div` tags and `class` attributes removed, leaving only basic HTML elements.

## Example Output

- **With div and class** (`second_wpb_wrapper_content_with_div.txt`):  
  Contains the full HTML content, including all `div` tags and `class` attributes.

- **Without div and class** (`second_wpb_wrapper_cleaned_content.txt`):  
  Contains only the basic HTML elements (headings, lists, etc.), with `div` tags and `class` attributes removed.
