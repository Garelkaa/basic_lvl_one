from pifagor_pyramid import is_pifagor


def test_is_pifagorova_pyramid():
    assert is_pifagor([5, 3, 4]) == True
    assert is_pifagor([6, 8, 10]) == True
    assert is_pifagor([100, 3, 65]) == False
    assert is_pifagor([3, 4, 5]) == True


test_is_pifagorova_pyramid()
