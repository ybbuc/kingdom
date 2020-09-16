def create_greeting(time_of_day):
    greeting = 'Good ' + time_of_day + ', King Jakob!'
    return greeting


current_time = 'morning'
print(create_greeting(current_time))
