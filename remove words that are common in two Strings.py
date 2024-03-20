def remove_common_words(S1, S2):
    words_S1 = S1.split()
    words_S2 = S2.split()
    set_S1 = set(words_S1)
    set_S2 = set(words_S2)
    common_words = set_S1.intersection(set_S2)
    filtered_S1 = ' '.join(word for word in words_S1 if word not in common_words)
    filtered_S2 = ' '.join(word for word in words_S2 if word not in common_words)
    return filtered_S1, filtered_S2
S1 =input("Enter s1:")
S2 =input("Enter s2:")
result_S1, result_S2 = remove_common_words(S1, S2)
print("Output:", result_S1)
print("Output:", result_S2)
