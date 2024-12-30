def solution(n, words):
    #n명이서 words를 가지고 끝말있중
    order = 1
    dict_word = {}
    prev = "asdfsdf" + str(words[0][0])
    for i,word in enumerate(words):
        if word not in dict_word:
            dict_word[word] = 1
        else:
            if (i+1) %n == 0:
                return [n,order]
            return [(i+1) % n,order]
        if prev[-1] == word[0]:
            if (i+1) % n == 0:
                order += 1
            prev = word
            continue
        else:
            if (i+1) %n == 0:
                return [n,order]
            return [(i+1) % n,order] 

    return [0,0]
        
            
        
        
        