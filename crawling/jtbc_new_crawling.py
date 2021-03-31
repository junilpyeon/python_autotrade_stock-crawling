import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def main():
    url = "http://news.jtbc.joins.com/section/index.aspx?scode=70"
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")

    times = []

    for i in range(0, 20):
        times.append(soup.find_all("span", class_="date")[i].get_text().strip())

    edited = []

    for i in range(0, len(times)):
        edited.append(times[i][8:10])

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for i in range(0, len(edited)):
        if edited[i] == "05": # 05일 기사 개수 구하기
            count1 = count1 + 1
        elif edited[i] == "06": # 06일 기사 개수 구하기
            count2 = count2 + 1
        elif edited[i] == "07": # 07일 기사 개수 구하기
            count3 = count3 + 1
        elif edited[i] == "08": # 08일 기사 개수 구하기
            count4 = count4 + 1

    days = [count1, count2, count3, count4]
    activities = ['05', '06', '07', '08']
    colors = ['red', 'blue', 'green', 'yellow']
    plt.pie(days, labels=activities, colors=colors, startangle=90, autopct='%.2f%%')
    plt.show()