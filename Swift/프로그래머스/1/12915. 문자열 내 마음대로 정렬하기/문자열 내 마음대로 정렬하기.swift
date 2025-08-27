func solution(_ strings:[String], _ n:Int) -> [String] {
    return strings.sorted { s1, s2 in
        let char1 = s1[s1.index(s1.startIndex, offsetBy: n)]
        let char2 = s2[s2.index(s2.startIndex, offsetBy: n)]
                           
        if char1 == char2 {
            return s1 < s2
        } else {
            return char1 < char2
        }
    }
}