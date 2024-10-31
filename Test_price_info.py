import price_info

price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def test_total_cost_shopping():
 test_total_cost = 0
 for key in price_list.keys():
        if key in quantity_list:
           test_total_cost += quantity_list[key]*price_list[key]

 result_total_cost = 0
 result_total_cost = price_info.total_cost_shopping()

 assert (result_total_cost == test_total_cost)

def test_cost_of_fruits():
     test_cost = 12.0
     result_total_cost = price_info.cost_of_fruits('apple', 10)

     assert(result_total_cost == test_cost)





