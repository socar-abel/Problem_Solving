//
//  main.swift
//  ProblemSolving
//
//  Created by 김상우 on 2022/12/27.
//

import Foundation

var n = Int(readLine()!)!
var nums = readLine()!.components(separatedBy: " ").map{ Int($0)! }
nums.sort()

if nums.count == 1 {
    print(nums[0] * nums[0])
}
else {
    print(nums[0] * nums[nums.count - 1])
}
