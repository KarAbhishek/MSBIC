import re  # Regular expressions
import urllib  # Website connections

from bs4 import BeautifulSoup  # For HTML parsing
from nltk.corpus import stopwords  # Filter out stopwords, such as 'the', 'or', 'and'


# matplotlib inline

def text_cleaner(website):
    """
    This function just cleans up the raw html so that I can look at it.
    Inputs: a URL to investigate
    Outputs: Cleaned text only
    """
    try:
        site = urllib.urlopen(website).read()  # Connect to the job posting
    except:
        return  # Need this in case the website isn't there anymore or some other weird connection problem

    soup_obj = BeautifulSoup(site)  # Get the html from the site

    for script in soup_obj(["script", "style"]):
        script.extract()  # Remove these two elements from the BS4 object

    text = soup_obj.get_text()  # Get the text from this

    lines = (line.strip() for line in text.splitlines())  # break into lines

    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))  # break multi-headlines into a line each

    def chunk_space(chunk):
        chunk_out = chunk + ' '  # Need to fix spacing issue
        return chunk_out

    text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode(
        'utf-8')  # Get rid of all blank lines and ends of line

    # Now clean out all of the unicode junk (this line works great!!!)

    try:
        text = text.decode('unicode_escape').encode('ascii', 'ignore')  # Need this as some websites aren't formatted
    except:  # in a way that this works, can occasionally throw
        return  # an exception

    text = re.sub("[^a-zA-Z.+3]", " ", text)  # Now get rid of any terms that aren't words (include 3 for d3.js)
    # Also include + for C++

    text = text.lower().split()  # Go to lower case and split them apart

    stop_words = set(stopwords.words("english"))  # Filter out any stop words
    text = []
    for w in text:
        if w not in stop_words:
            text.append(w)

    text = list(
        set(text))  # Last, just get the set of these. Ignore counts (we are just looking at whether a term existed
    # or not on the website)

    return text

sample = text_cleaner('https://www.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0D9Z_NigMRFBqnj4_9rPbMnaYMSgnKsRu0gcL5XJCnD3cZSRlOsFUPMyS7IRniKNjrg4yMsG4gE4-1xPr1SsywoWjx4nHTFLic-XlT7lz0UciOe5fyuvo9qMd1FXU8giQ8marPECYUmpnkH6E5y3f2ETkitqFjZpTHKgkelwjCVSYm4K21M5tqc3nVDN-UwipWBQmGfwQj7rnLpvp8opgJ0TJKY5ybd6P-zTJVbM5G1LF8eoQqlpKfy4m-BP4fSihYl-rMmOFMrEQCnfZYcJOLRzpe5fGl8X1ZXu83QXfSTQJQVKSQ8E715arEX76RTlleVXg6bsu2h53AYx7f2bdD2EALfSreMll6rhPKshhXLl6MaT01Nk-2bsycnL5P0lhLaLTI6ZKwi28wwvfU0Ms6Ci0c6ZGsvMngcsZeFR62mm9rh4FV8UynEffdEs8AMp-God_BMBDvw7DUL5CVnIqa9dMnr2n1Dip7vRd1-_KWLG9nNdvPYMndx0fWv6MZiDzAeJ4S6mXtem8FuNJ2kA8otm6d_EEYW9frONU2u4IpUsMKwbd6dafHKvhcAW5WtpANuKfzOjOnxLaEUKacYRdaEr-id4LEPSxd8kjn2wwgoATSPrtK9MfiAsSvHppaEIJP4Ye93UCqA0fWMslsQvaX2dt5nFwz364gl1-VBYqK2uS4_oFAAGnNz1nBRmK6eiGesoYGuWfTxWh9xt75l7Tb6l4ekJYWutILrV_Z0gNToO-O-wATEwQgE1oeBr_pBsdhUMdx6D7-_wJj2ycGvmokaktSG_gBAS5UJINFQ4akm_qsbTazGgUZfKkPjkYW0eMmhF2CZEeOFZT0m5_jUr37LDrylRzw-KWqwxj7RnZxTwHHvUcWtEyhVfSKb3CE5M6UQ6N1liVX0cejuqWSH4fmpAr8HMj77ztMRsNl0AC0UO5iOp0t-ETQl&p=1&sk=&fvj=0&tk=1b6838ko3518tddc&jsa=5347&sal=0')
sample[:20] # Just show the first 20 words
