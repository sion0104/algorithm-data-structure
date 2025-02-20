import Foundation

func solution(_ dots:[[Int]]) -> Int {
    let xCoordinates = dots.map{ $0[0] }
    let yCoordinates = dots.map{ $0[1] }
    
    let width = xCoordinates.max()! - xCoordinates.min()!
    let height = yCoordinates.max()! - yCoordinates.min()!
    
    return width * height
}