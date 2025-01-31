import Foundation

func solution(_ arr:[Int]) -> Int {
    var arr = arr
    var count = 0
    
    while true {
        var temp: [Int] = []
        
        for num in arr {
             if num >= 50 && num % 2 == 0 {
                 temp.append(num / 2)
             }
            else if num < 50 && num % 2 != 0 {
                temp.append(num * 2 + 1)
            }  
            else {
                temp.append(num)
            }       
        }
           
        if temp == arr {
            return count
        }
         
        arr = temp
        count += 1
    }
        
}