import pandas as pd
from googlesearch import search
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re
import datetime
import time

def main():
    ua = UserAgent()
    headers = {"User-Agent": ua.random}

    query = input("Enter a search query: ")
    print("Searching...")
    results = []

    for url in search(query, num_results=50):
        try:
            time.wait(5)
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.find("title").get_text()
            result = "Success"
        except:
            title = ""
            result = "Error"
        results.append({"Website Name": url, "Date and Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Request Response Result": result, "Title": title})

    df = pd.DataFrame(results)
    # create a new dataframe for categorizing the results
    categorized_df = pd.DataFrame(columns=["Website Name", "Date and Time", "Request Response Result", "Title", "Category"])
    for idx, row in df.iterrows():
        # categorize the websites based on the title
        if re.search(r"\bnews\b", row["Title"], re.IGNORECASE):
            row["Category"] = "News"
        elif re.search(r"\bsocial media\b|\bfacebook\b|\btwitter\b", row["Title"], re.IGNORECASE):
            row["Category"] = "Social Media"
        elif re.search(r"\bblog\b", row["Title"], re.IGNORECASE):
            row["Category"] = "Blog"
        else:
            row["Category"] = "Other"
        categorized_df = categorized_df.append(row, ignore_index=True)

    # save the categorized results to a new excel file
    categorized_df.to_excel(f"{query}_osint_results_categorized.xlsx", index=False)
    print(f"Categorized results saved to {query}_osint_results_categorized.xlsx")


if __name__ == "__main__":
    main()
