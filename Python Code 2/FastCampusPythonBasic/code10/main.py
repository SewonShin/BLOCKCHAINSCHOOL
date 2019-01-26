from konlpy.tag import Okt

ok = Okt()
test = "안녕하세요. 저는 신세원입니다."
for i in ok.pos(test, norm=True):
    # print(i)
for i in ok.pos(test):
    # if i[1] == 'hashtag':
        #print(i)
test = "패스트캠퍼스 패캠 신세원 코딩 프로그램"
for i in ok.nouns(test):
    print(i)