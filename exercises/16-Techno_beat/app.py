def lyrics_generator(list1):
    lyric = ""    
    for i in range(len(list1)):
        if list1[i]== 1 and list1[i-1]== 1 and list1[i-2]== 1:
            lyric += "Drop the base !!! Break the base !!!"
        elif list1[i]== 0:
            lyric +=  ' Boom '
        else:
            lyric += 'Drop the base '
    return lyric            

            



# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))