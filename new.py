from collections import deque

def water_jug_problem(capacity1, capacity2, target):
    queue = deque([(0, 0)]) 
    visited = set([(0, 0)])  
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        if jug1 == target or jug2 == target:
            return True
        
        possible_actions = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),          
            (jug1, 0),          
            (max(0, jug1 - (capacity2 - jug2)), min(capacity2, jug2 + jug1)),  
            (min(capacity1, jug1 + jug2), max(0, jug2 - (capacity1 - jug1))) 
        ]
        
        for new_jug1, new_jug2 in possible_actions:
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                queue.append((new_jug1, new_jug2))
    
    return False 
capacity1 = 7 
capacity2 = 3  
target = 2  

if water_jug_problem(capacity1, capacity2, target):
    print("It is possible to measure the target amount of water.")
else:
    print("It is not possible to measure the target amount of water.")
