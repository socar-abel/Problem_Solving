import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var answer = [Int]()
    let N = genres.count
    // ["classic": 1450, "pop": 3100]
    var genreTotalPlay = [String: Int]()
    // ["classic": (곡번호, 재생수), ...]
    var genreSongList = [String: [(Int, Int)]]()
    
    for i in 0..<N {
        genreTotalPlay[genres[i], default: 0] += plays[i]
        genreSongList[genres[i], default: [(Int, Int)]()].append((i, plays[i]))
    }
    
    let sortedGenreTotalPlay = genreTotalPlay.sorted{ $0.value > $1.value }
    for elem in sortedGenreTotalPlay {
        let (genre, _) = elem
        var songList = genreSongList[genre]!
        songList.sort{$0.0 < $1.0}
        songList.sort{$0.1 > $1.1}
        answer.append(songList.first!.0)
        if songList.count >= 2 {
            answer.append(songList[1].0)
        }
    }
    
    return answer
}
