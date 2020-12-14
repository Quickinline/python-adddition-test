import random
def average_correct(list):
    return sum(list)/len(list)

def test_average():
    for x in range(5):
        list = [random.randint(5,200) for x in range(15)]
        assert average_correct(list) == average(list)
