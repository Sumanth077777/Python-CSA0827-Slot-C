def num_good_pairs(nums):
    freq_map = {}
    good_pairs = 0
    good_pairs_indices = []
    for i, num in enumerate(nums):
        freq_map[num] = freq_map.get(num, 0) + 1
        good_pairs += freq_map[num] - 1
        if freq_map[num] >= 2:
            good_pairs_indices.append((nums.index(num, 0, i), i))
    print("Good pairs indices (0-indexed):", good_pairs_indices)
    return good_pairs
nums = [1, 2, 3, 1, 1, 3]
print("Number of good pairs:", num_good_pairs(nums))
