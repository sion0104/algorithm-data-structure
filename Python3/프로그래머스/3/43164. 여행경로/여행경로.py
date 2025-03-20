from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    
    for departure, arrival in tickets:
        routes[departure].append(arrival)
        
    for departure in routes:
        routes[departure].sort()
    
    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            return path
        
        for i in range(len(routes[airport])):
            next_airport = routes[airport].pop(i)
            new_path = dfs(next_airport, path + [next_airport])
            
            if new_path:
                return new_path
            
            routes[airport].insert(i, next_airport)
    
    return dfs("ICN", ["ICN"])
        
    

        
            
             