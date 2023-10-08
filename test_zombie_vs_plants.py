from zombie_vs_plants import plants_vs_zombies


def test_plants_vs_zombies():
    assert plants_vs_zombies([1, 3, 5, 7], [2, 4, 6, 8]) == True
    assert plants_vs_zombies([1, 3, 5, 7], [2, 4]) == False
    assert plants_vs_zombies([1, 3, 5, 7], [2, 4, 0, 8]) == True
    assert plants_vs_zombies
