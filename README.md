# company-financial-data-downloader
A python script to download financial information for any company from Yahoo Finance, and output it in a spreadsheet.

## Usage guide
In order to run this application, make sure you have the latest Python 3 installed. You also need to download this repository either by clicking "Clone or download" or by running this command on a git client:

    git clone https://github.com/proyectoramirez/company-financial-data-downloader.git

Then, in order to install all the required libraries, run this command:

    pip install -r requirements.txt

Once this is done, you will also need to provide a list of companies to get data for. By default, the program will look for a file called `companies.csv` in the folder it is excecuted from, which should contain each of the company tickers wanted in a new line. Example:

    AAPL
    MSFT
    INTC
    PZZA

Finally, you can run the script and download the data needed with this command:

    python main.py

If you want to use a different csv as an input, you can provide its file path as an argument on the command line through the `--companies` flag (or just `-c`):

    python main.py --companies "YOUR_FILE_PATH"
