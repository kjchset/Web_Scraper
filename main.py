import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape titles from a given URL
def scrape_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Adjust the selector based on the website's structure
    titles = [title.get_text() for title in soup.select('h2')]  # Assuming titles are in <h2> tags
    return titles

# Streamlit app
def main():
    st.title("Web Scraping with Streamlit")
    
    url = st.text_input("Enter the URL to scrape:")
    
    if st.button("Scrape"):
        if url:
            with st.spinner("Scraping titles..."):
                try:
                    titles = scrape_titles(url)
                    st.success("Scraping completed!")
                    st.write("### Article Titles:")
                    for title in titles:
                        st.write(f"- {title}")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a URL.")

if __name__ == "__main__":
    main()
