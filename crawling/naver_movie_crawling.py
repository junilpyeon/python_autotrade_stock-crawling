import urllib.request
from bs4 import BeautifulSoup


def main():
    url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=156464"
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

    ul = soup.find("ul", class_="rvw_list_area")
    for i in ul.find_all("li"):
        print(i.strong.get_text())


if __name__ == "__main__":
    main()
