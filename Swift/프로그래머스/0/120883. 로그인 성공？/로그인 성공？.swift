import Foundation

func solution(_ id_pw:[String], _ db:[[String]]) -> String {
    if db.contains(id_pw) {
        return "login"
    } else {
        let id = id_pw[0]

        for info in db {
            if info[0] == id {
                return "wrong pw"
            }
        }
        return "fail"
    }
}