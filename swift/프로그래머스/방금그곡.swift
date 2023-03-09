import Foundation

func getPlayMinute(_ startTime: String, _ endTime: String) -> Int {
    let arr1 = startTime.split(separator: ":")
    let arr2 = endTime.split(separator: ":")
    let (startHour, startMinute) = (Int(arr1[0])!, Int(arr1[1])!)
    let (endHour, endMinute) = (Int(arr2[0])!, Int(arr2[1])!)
    return (endHour * 60 + endMinute) - (startHour * 60 + startMinute)
}


func parseMelody(_ s: String) -> String {
    var parsedMelody = String(s)
    parsedMelody = parsedMelody.replacingOccurrences(of: "C#", with: "c")
    parsedMelody = parsedMelody.replacingOccurrences(of: "D#", with: "d")
    parsedMelody = parsedMelody.replacingOccurrences(of: "F#", with: "f")
    parsedMelody = parsedMelody.replacingOccurrences(of: "G#", with: "g")
    parsedMelody = parsedMelody.replacingOccurrences(of: "A#", with: "a")
    return parsedMelody
}


func solution(_ m:String, _ musicinfos:[String]) -> String {
    var candidate = [(String, Int)]()
    let M = parseMelody(m)
    
    for musicinfo in musicinfos {
        let arr = musicinfo.split(separator: ",")
        let (startTime, endTime, title, melody) = (arr[0], arr[1], arr[2], arr[3])
        let playMinute = getPlayMinute(String(startTime), String(endTime))
        var parsedMelody = parseMelody(String(melody))
        var totalMelody = String(repeating: parsedMelody, count: Int(playMinute/parsedMelody.count))
        totalMelody += parsedMelody[parsedMelody.startIndex..<parsedMelody.index(parsedMelody.startIndex, offsetBy: Int(playMinute%parsedMelody.count))]
        if totalMelody.contains(M) {
            candidate.append((String(title), playMinute))
        }
    }
    
    candidate.sort { $0.1 > $1.1 }
    
    return candidate.isEmpty ? "(None)" : candidate.first!.0
}
