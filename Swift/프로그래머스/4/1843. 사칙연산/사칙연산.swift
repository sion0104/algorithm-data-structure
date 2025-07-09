func solution(_ input_array:[String]) -> Int {

    var numbers: [Int] = []
    var op: [OP] = []

    input_array.forEach {
        if $0 == "+" { op.append(.add); return }
        if $0 == "-" { op.append(.sub); return }
        numbers.append(Int($0)!)
    }
    
    if numbers.count == 0 { return 0 }

    var record: [[(Int, Int)]] = []

    for i in 0..<numbers.count {
        record.append( [(numbers[i], numbers[i])] );
        guard i > 0 else { continue }
        record[i-1].append((op[i-1].run(record[i-1][0].0, numbers[i]), op[i-1].run(record[i-1][0].0, numbers[i])))
        guard i > 1 else { continue }

        for n in stride(from: i - 2, through: 0, by: -1) {
            var max = 0
            var min = 0
            
            stride(from: record[n].count-1, through: 0, by: -1).forEach {
                let new = [op[n+$0].run(record[n][$0].0, record[n+$0+1][record[n].count-1-$0].0),
                           op[n+$0].run(record[n][$0].0, record[n+$0+1][record[n].count-1-$0].1),
                           op[n+$0].run(record[n][$0].1, record[n+$0+1][record[n].count-1-$0].0),
                           op[n+$0].run(record[n][$0].1, record[n+$0+1][record[n].count-1-$0].1)]

                guard let newMin = new.min(), let newMax = new.max() else { return }
                if $0 == record[n].count-1 { min = newMin; max = newMax }
                else {
                    min = (min > newMin) ? newMin : min
                    max = (newMax > max) ? newMax : max
                }
            }
            record[n].append((max, min))
        }
    }

    return record[0].last?.0 ?? 0
}

enum OP {
    case add, sub
    
    func run(_ lhs: Int, _ rhs: Int) -> Int {
        return (self == .add) ? lhs + rhs : lhs - rhs
    }
}