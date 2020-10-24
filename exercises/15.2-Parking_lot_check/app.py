parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(list1):
    slots = { "totalSlots": 0, "availableSlots": 0, "occupiedSlots": 0 }
    for x in list1:
        for i in range(len(x)):
            if x[i] == 1:
               slots["occupiedSlots"] += 1
               slots["totalSlots"] += 1
            elif x[i]== 2:
                slots["availableSlots"] += 1
                slots["totalSlots"] += 1
    return slots 
            
    



print (get_parking_lot(parking_state))        



