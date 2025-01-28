import Foundation

func solution(_ n:Int, _ slicer:[Int], _ num_list:[Int]) -> [Int] {
    switch n {
        case 1:
            let result = Array(num_list[0...slicer[1]])
            return result
        case 2:
            let result = Array(num_list[slicer[0]...])
            return result
        case 3:
            let result = Array(num_list[slicer[0]...slicer[1]])
            return result
        case 4:
            var result: [Int] = []
            var index = slicer[0]
            while index <= slicer[1] {
                result.append(num_list[index])
                index += slicer[2]
            }
            return result
        default:
            return []
    }
}