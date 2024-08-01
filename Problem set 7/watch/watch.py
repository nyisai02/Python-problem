import re
def main():
    print(parse(input("HTML: ")))


def parse(s):

    if re.search(r"<iframe(.)*><\/iframe>",s):
        link_url=re.search(r"(http(s?)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)",s)
        if link_url:
            url_part=link_url.groups()
            return "https://youtu.be/"+ url_part[3]
    else:
        return "None"
if __name__ == "__main__":
    main()
