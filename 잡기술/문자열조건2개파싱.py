# 순위검색 ' and ' 도 파싱해야하고 ' '도 파싱해야 하는 상황
# replace(" and "," ").split(" ")을 사용한다.
queryList = query[q].replace('and ', '').split(' ')
