import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(
        r'^<iframe( width="\d{1,3}" height="\d{1,3}")? src="https?://(www\.)?youtube\.com/embed/(\w+)".*></iframe>$',
        s,
        re.IGNORECASE,
    ):
        return f"https://youtu.be/{link.group(3)}"
    else:
        return None


if __name__ == "__main__":
    main()
