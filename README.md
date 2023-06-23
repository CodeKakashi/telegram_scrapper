# Telegram Channel Message Scraper

This script allows you to scrape messages from a Telegram channel and save them as JSON files. It uses the Telethon library to connect to the Telegram API and retrieve channel messages.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3 installed on your system.
- Telethon library installed. You can install it using pip: `pip install telethon`.
- Telegram API credentials (API ID and API hash). You can obtain them by creating a new application on the Telegram website: [https://my.telegram.org/apps](https://my.telegram.org/apps).
- Telegram phone number and username for the account you want to use to access the channel.

## Setup

1. Clone this repository or download the script file (`telegram_scraper.py`) to your local machine.
2. Install the required dependencies by running the following command:

```pip install telethon```

3. Open the `telegram_scraper.py` file in a text editor.
4. Replace the placeholder values in the `api_id`, `api_hash`, `phone`, and `username` variables with your actual Telegram API credentials and account information.

## Usage

To run the script and scrape messages from a Telegram channel, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where the `telegram_scraper.py` file is located.
2. Run the following command:
   
```python telegram_scraper.py```

3. If you haven't authorized the script to access your Telegram account, it will prompt you to enter the verification code or password.
4. Enter the entity of the Telegram channel you want to scrape. It can be the channel URL or entity ID.
5. The script will start scraping the channel messages and display the progress.
6. Once the scraping is complete, the messages will be saved as JSON files named with the offset ID of the last message retrieved.
- For example, if the last message's offset ID is 12345, the output file will be named `12345.json`.
- Each message is stored as a separate JSON object in the file, containing various message details such as sender, date, text, etc.

## Schedule

The script includes an example of using the `schedule` library to schedule the scraping job at regular intervals. By default, the script is configured to run the job every 2 minutes.

To customize the scheduling behavior, you can modify the `job` function and the `schedule.every()` statement according to your requirements.

## License

This project is licensed under the [MIT License](LICENSE).

