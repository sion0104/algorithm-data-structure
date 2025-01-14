import sys

digital_humanities_keywords = ["social", "history", "language", "literacy"]
public_bigdata_keywords = ["bigdata", "public", "society"]

title = sys.stdin.readline().strip().lower()

if any(keyword in title for keyword in digital_humanities_keywords):
    print("digital humanities")
elif any(keyword in title for keyword in public_bigdata_keywords):
    print("public bigdata")
