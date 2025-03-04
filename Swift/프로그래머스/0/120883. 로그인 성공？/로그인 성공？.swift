import Foundation

func solution(_ id_pw:[String], _ db:[[String]]) -> String {
    enum LoginResult {
        static let success = "login"
        static let wrongPassword = "wrong pw"
        static let fail = "fail"
    }
    
    let (id, password) = (id_pw[0], id_pw[1])
    
    guard let userInfo = db.first(where: {$0[0] == id} ) else {
        return LoginResult.fail
    }
    
    return userInfo[1] == password ? LoginResult.success : LoginResult.wrongPassword
}