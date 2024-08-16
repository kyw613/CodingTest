def is_group_word(word):
    seen = set()
    previous_char = None
    
    for char in word:
        if char != previous_char:
            if char in seen:
                return False
            seen.add(char)
        previous_char = char
    
    return True

def count_group_words(words):
    count = 0
    for word in words:
        if is_group_word(word):
            count += 1
    return count

# 입력 처리
N = int(input())  
words = [input().strip() for _ in range(N)]

print(count_group_words(words))
