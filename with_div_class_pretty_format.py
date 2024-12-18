import requests
from bs4 import BeautifulSoup

url = 'https://nwc.education/aston-university-official-agent-in-bangladesh/'  # Replace with the URL you want to get the content from
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the class 'wpb_wrapper'
    wpb_wrapper_elements = soup.find_all('div', class_='wpb_wrapper')

    # Check if there are at least 2 elements
    if len(wpb_wrapper_elements) >= 2:
        # Get the second element
        second_wpb_wrapper = wpb_wrapper_elements[1]

        # Prettify the second wpb_wrapper content
        prettified_content = second_wpb_wrapper.prettify()

        # Save the prettified content to a new text file
        with open('second_wpb_wrapper_content_pretty.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(prettified_content)

        print("Second wpb_wrapper content saved to second_wpb_wrapper_content_pretty.txt")
    else:
        print("There are less than 2 wpb_wrapper elements")
