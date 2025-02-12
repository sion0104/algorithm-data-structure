import Foundation

func solution(_ sides:[Int]) -> Int {
    let sortedSlides = sides.sorted()
    
    if sortedSlides[0] + sortedSlides[1] > sortedSlides[2] {
        return 1
    }
    
    return 2
}