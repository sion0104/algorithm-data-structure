import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var answer: [Int] = []
    
    for query in queries {
        let i = query[0]
        let j = query[1]
        let k = query[2]
        
        let subArray = arr[i...j]
        
        let filtered = subArray.filter { $0 > k }.sorted()
        
        if filtered.isEmpty {
            answer.append(-1)
        } else {
            answer.append(filtered[0])
        }
    }
    
    return answer
}