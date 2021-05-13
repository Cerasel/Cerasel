

test_data = [[1, 2, 3], [3, 3, 5], [8, 9, 4], [2, 8, 4]]
def pinball_game(test_data, nr_holes = 10):
    result = set()
    for game_result in test_data:
        result = result.union(set(game_result))
    holes_set = set(range(1, nr_holes + 1))
    print(holes_set)
    result = holes_set.difference(result)
    print(result)
pinball_game(test_data)
