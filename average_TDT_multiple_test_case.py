def average(L):
    if not L:
        return None
    return sum(L)/len(L)

def test_average():
    test_cases = [
        {
            "name"         : "case 1",
            "input"         : [1,2,3],
            "expected" : 2.0
        },

        {   "name"         : "case 2",
            "input"         : [1,2,3,4],
            "expected" : 2.0
        },
        
        {   "name"         : "case 3 or one item only",
            "input"         : [200],
            "expected" : 200.0
        },
        
        {   "name"         : "case 4 or empty list",
            "input"         : [],
            "expected" : None
        }

                ]

    for test_case in test_cases:
            assert average(test_case["input"]) == test_case['expected'], test_case['name']

def add(a,b):
    return a+b

def test_add():
    assert add(5,6) == 11
    
