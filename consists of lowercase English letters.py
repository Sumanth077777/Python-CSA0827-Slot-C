def group_anagrams(strs):
    # Create a hashmap to store anagrams
    anagrams_map = {}
    
    # Iterate through each string in the input array
    for s in strs:
        # Sort the characters of the string to get its key
        key = ''.join(sorted(s))
        
        # Add the string to the corresponding list in the hashmap
        if key in anagrams_map:
            anagrams_map[key].append(s)
        else:
            anagrams_map[key] = [s]
    
    # Return the values of the hashmap as a list of lists
    return list(anagrams_map.values())

# Test the function with the given input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)
