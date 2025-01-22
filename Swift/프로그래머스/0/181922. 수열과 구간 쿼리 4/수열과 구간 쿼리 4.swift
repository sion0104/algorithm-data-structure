import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var arr = arr
    
    for query in queries {
        let s = query[0]
        let e = query[1]
        let k = query[2]
        
        for i in stride(from: s, through: e, by: 1) {
            if i % k == 0 {
                arr[i] += 1
            }
        }
    }
    
    return arr
}