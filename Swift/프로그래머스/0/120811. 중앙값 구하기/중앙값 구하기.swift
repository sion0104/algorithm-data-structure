import Foundation

func solution(_ array:[Int]) -> Int {
    var array = array
    array.sort()
    return array[array.count/2]
}