# 2019 KAKAO BLIND RECRUITMENT 매칭 점수
# https://programmers.co.kr/learn/courses/30/lessons/42893

def solution(word, pages):
    answer = 0
    lenWord = len(word)
    linkWord = "<a href="
    lenLink = len(linkWord)
    domainWord = '<meta property="og:url" content='
    lenDomain = len(domainWord)

    #기본점수, domain, links
    pageInfos = [[0, '', []] for i in range(len(pages))]

    hs = -1
    for page in pages:
        hs += 1
        domain = ''
        score1 = 0
        score2 = 0
        links = []
        score3 = 0
        score4 = 0

        lenPage = len(page)
        page = page.lower()
        word = word.lower()

        for i in range(lenPage-lenWord+1):
            wordWindow = page[i:i+lenWord]
            if(wordWindow == word):
                if(i>0 and i+lenWord<lenPage-1):
                    if(ord(page[i-1]) < ord('a') or ord(page[i-1]) > ord('z')):
                        if(ord(page[i+lenWord]) < ord('a') or ord(page[i+lenWord]) > ord('z')):
                            score1 += 1
            if(i+lenLink <= lenPage):
                linkWindow = page[i: i+lenLink]
                if(linkWord == linkWindow):
                    score2 += 1
                    flag = False
                    idx = i+lenLink
                    linkStr = ''
                    while flag==False:
                        idx += 1
                        if(page[idx] == '"'):
                            flag = True
                        else:
                            linkStr += page[idx]
                    links.append(linkStr)
            if(i+lenDomain <= lenPage):
                domainWindow = page[i: i+lenDomain]
                if(domainWord == domainWindow):
                    flag = False
                    idx = i+lenDomain
                    domainStr = ''
                    while flag==False:
                        idx += 1
                        if(page[idx] == '"'):
                            flag = True
                        else:
                            domainStr += page[idx]
                    domain = domainStr
        pageInfos[hs][0] = score1
        pageInfos[hs][1] = domain
        pageInfos[hs][2] = links
    scores = []
    for i in range(len(pageInfos)):
        pi = pageInfos[i]
        pagescore = 0
        pagescore += pi[0]
        lenLinks = len(pi[2])
        domain = pi[1]
        for j in range(len(pageInfos)):
            if(i!=j):
                pi2 = pageInfos[j]
                links2 = pi2[2]
                lenLinks2 = len(links2)
                if(domain in links2):
                    pagescore += (pi2[0]/lenLinks2)
        scores.append((pagescore, i))
    maxIdx = 0
    maxScore = 0
    for i in range(len(scores)):
        score = scores[i]
        if(score[0] > maxScore):
            maxScore = score[0]
            maxIdx = score[1]

    answer = maxIdx

    return answer


print(solution(	"blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution(	"Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))