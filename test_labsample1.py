import labsample1 


def test_get_longest_workout():
   result = []
   testcase = [
       {'date': '15.01.2022', 'activity': 'Running', 'duration': 40},
       {'date': '16.01.2022', 'activity': 'Swimming', 'duration': 100},
       {'date': '17.01.2022', 'activity': 'Yoga', 'duration': 10}
   ]
   test = {'date': '16.01.2022', 'activity': 'Swimming', 'duration': 100}
   result = labsample1.get_longest_workout(testcase)
   assert(result == test)
    
def test_calc_total_duration():
    result = []
    testcase = [
           {'date': '15.01.2022', 'activity': 'Running', 'duration': 40.0},
           {'date': '16.01.2022', 'activity': 'Swimming', 'duration': 100.0},
           {'date': '17.01.2022', 'activity': 'Yoga', 'duration': 10.0}
       ]
    test = 150.0
    result = labsample1.calc_total_duration(testcase)
    assert(result == test)
    workouts = labsample1.load_csv()

def test_calc_average_duration():  
    result = []
    testcase = [
           {'date': '15.01.2022', 'activity': 'Running', 'duration': 40.0},
           {'date': '16.01.2022', 'activity': 'Swimming', 'duration': 100.0},
           {'date': '17.01.2022', 'activity': 'Yoga', 'duration': 10.0}
       ]
    test = 50.0
    result = labsample1.calc_average_duration(testcase)
    assert(result==test)
    workouts = labsample1.load_csv()
