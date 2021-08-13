def solution(m, musicinfos):
    answer = '(None)'
    actualMusics = []
    
    for a in range(len(musicinfos)):
        music = musicinfos[a]
        start, end = music.split(',')[0], music.split(',')[1]
        title, tempCode = music.split(',')[2], music.split(',')[3]
        #print('title',title)
        code = []
        for t in tempCode:
            if t.isalpha() : code.append(t)
            elif t == '#' : code[-1] = code[-1]+'#'
        playTime = (int(end[:2])-int(start[:2]))*60 + int(end[3:]) - int(start[3:])
        actualMusic = (playTime // len(code)) * code + code[:(playTime%len(code))+1]
        #print('m',m)
        #print('actualMusic',actualMusic)
        listM = []
        for x in m:
            if x.isalpha() : listM.append(x)
            elif x == '#' : listM[-1] = listM[-1]+"#"
        #print('listM',listM)
        i = 0
        while True:
            if i+len(listM) > len(actualMusic) : break
            if listM == actualMusic[i:i+len(listM)] : 
                actualMusics.append((title,playTime,a)); break
            i += 1
    
    
    print('actualMusics',actualMusics)
    if actualMusics :
        candidate = []
        maxPlayTime = max(actualMusics, key = lambda x : x[1])[1]
        #print('maxPlayTime',maxPlayTime)
        for candy in actualMusics:
            if candy[1] == maxPlayTime : candidate.append(candy)
        answer = min(candidate, key = lambda x : x[2])[0]
    
    #print('final',answer)
    
    return answer
