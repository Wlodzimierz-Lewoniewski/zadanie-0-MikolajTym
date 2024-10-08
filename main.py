import re
from collections import Counter

import pandas as pd

def get_data():
    doc_num = input("Type the doc number:\n")
    doc_num = int(doc_num.strip())
    docs = []
    for i in range(doc_num):
        doc = input(f"Type the {i+1} document:\n").strip()
        docs.append(doc)
    keyword_num = input("Type the keyword number that should be find in documents:\n")
    keyword_num = int(keyword_num.strip())
    keywords = []
    for i in range(keyword_num):
        keyword = input(f"Type the {i+1} keyword:\n").strip()
        keywords.append(keyword)
    return docs, keywords

docs, keywords = get_data()

for keyword in keywords:
    keyword = keyword.lower()
    df = pd.DataFrame(data={"document": docs})
    df["clean_doc"] = df["document"].apply(lambda doc: re.sub(r'[^\w\s]', '', doc).lower().split(" "))
    df["count"] = df["clean_doc"].apply(lambda doc: Counter(doc).get(keyword, 0))
    # If counted words numbers are equal, sort by document alphabetically
    # df = df.sort_values(by=["count", "document"], ascending=[False, True])
    df = df.sort_values(by=["count"], ascending=[False])
    df = df[df["count"]>0]
    results = list(df.index)
    print(results)