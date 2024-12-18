import requests
from bs4 import BeautifulSoup

url = 'https://nwc.education/aston-university-official-agent-in-bangladesh/'  # Replace with the URL you want to get the content from
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    wpb_wrapper_elements = soup.find_all('div', class_='wpb_wrapper')
    if len(wpb_wrapper_elements) >= 2:
        second_wpb_wrapper = wpb_wrapper_elements[1]
        for tag in second_wpb_wrapper.find_all(True):
            del tag['class']
        for div in second_wpb_wrapper.find_all('div'):
            div.unwrap()
        with open('second_wpb_wrapper_cleaned_content.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(str(second_wpb_wrapper))

        print("Cleaned second wpb_wrapper content saved to second_wpb_wrapper_cleaned_content.txt")
    else:
        print("There are less than 2 wpb_wrapper elements")
