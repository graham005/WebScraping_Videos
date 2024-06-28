import os
import requests
from bs4 import BeautifulSoup

# Function to scrape video page links from the given Pixabay search URL
def scrape_pixabay_video_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    video_links = []

    for video_div in soup.find_all('div', class_='media'):
        video_page_link = video_div.find('a')['href']
        video_links.append(f"https://pixabay.com{video_page_link}")

    return video_links

# Function to download videos from the individual Pixabay video page URL
def download_video(video_page_url, download_path, resolution="1920x1080"):
    response = requests.get(video_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    download_options = soup.find('div', class_='dropdown-menu').find_all('a')

    # Find the link for the desired resolution
    video_url = None
    for option in download_options:
        if resolution in option.text:
            video_url = option['href']
            break

    if video_url:
        video_title = soup.find('h1', class_='media-title').text.strip().replace(" ", "_") + ".mp4"
        video_response = requests.get(video_url, stream=True)

        with open(os.path.join(download_path, video_title), 'wb') as f:
            for chunk in video_response.iter_content(chunk_size=1024):
                f.write(chunk)
            print(f"Downloaded: {video_title}")
    else:
        print(f"Resolution {resolution} not found for {video_page_url}")

# Main script
if __name__ == "__main__":
    url = "https://pixabay.com/videos/search/airplane/"
    download_path = r"C:\Users\The Elder\Downloads\Airplanes"  # Change the download path here
    resolution = "1920x1080"  # Desired resolution

    # Create download folder if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Scrape Pixabay for video page links
    video_links = scrape_pixabay_video_links(url)
    print(f"Found {len(video_links)} videos.")

    # Download videos from each video page link
    for link in video_links:
        try:
            download_video(link, download_path, resolution)
        except Exception as e:
            print(f"Failed to download from {link}: {e}")
