# Real Estate Web Scraping

This project is a web scraping script that collects real estate data from a website and saves it to a CSV file. It also downloads and saves images associated with the listings.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/real-estate-web-scraping.git
   ```

2. Navigate to the project directory:

   ```shell
   cd real-estate-web-scraping
   ```

3. Install the required Python packages using pip:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```shell
   python main.py
   ```

2. Wait for the scraping process to complete. The script will scrape multiple pages, so it may take some time.

3. After the scraping is finished, the data will be saved to a CSV file named `batdongsan.csv`. The images associated with the listings will be downloaded and saved in the `images` folder.

4. Once the process is complete, you can analyze the data in the CSV file or use it for further processing.

## Configuration

You can modify the script by changing the following variables:

- `num_threads`: Number of threads to use for concurrent scraping. Adjust this value based on your system's capabilities.
- `baseUrl`: The base URL of the website to scrape. Change this if you want to scrape a different website.
- `listCarLinks`: An empty list that can be used to store additional data if required.
