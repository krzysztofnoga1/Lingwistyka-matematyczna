states_trans = [
    ['q0', 'q0', 'q0', 'q0m', 'q0d'],
    ['q1m', 'q2m', 'q5m', 'q0m', 'q0m'],
    ['q1d', 'q2d', 'q5d', 'q0d', 'q0d'],
    ['q2m', 'q3m', 'qe', 'q1m', 'q1m'],
    ['q2d', 'q3d', 'q6d', 'q1d', 'q1d'],
    ['q3m', 'q4m', 'qe', 'q2m', 'q2m'],
    ['q3d', 'q4d', 'q7d', 'q2d', 'q2d'],
    ['q4m', 'q5m', 'qe', 'q3m', 'q3m'],
    ['q4d', 'q5d', 'q8d', 'q3d', 'q3d'],
    ['q5m', 'qe', 'qe', 'q4m', 'q4m'],
    ['q5d', 'q6d', 'qe', 'q4d', 'q4d'],
    ['q5m', 'q5m', 'q5m', 'q5m', 'q5m'],
    ['q6d', 'q7d', 'qe', 'q5d', 'q5d'],
    ['q7d', 'q8d', 'qe', 'q6d', 'q6d'],
    ['q8d', 'qe', 'qe', 'q7d', 'q7d'],
    ['q8d', 'q8d', 'q8d', 'q8d', 'q8d'],
    ['-', '-', '-', '-', '-']
]

states = ['q0', 'q0m', 'q0d', 'q1m', 'q1d', 'q2m', 'q2d', 'q3m', 'q3d',
'q4m', 'q4d', 'q5m', 'q5d', 'q6d', 'q7d', 'q8d', 'qe']

inputs = ['1', '2', '5', 'm', 'd']

states_path = ['q0']

state_index = 0
input_index = 0
chosen_path = 'x'
running = True

def print_automat():
    print('   ', end=' ')
    for j in range(0, 5):
        if j < 4:
            print('', inputs[j], end='  ')
        else:
            print('', inputs[j])
    print("-----------------------")

    for i in range(0, 16):
        if len(states[i]) == 2:
            print(states[i], '', end='|')
        else:
             print(states[i], end='|')
        for k in range(0, 5):
            if k < 4:
                if len(states_trans[i][k]) == 2:
                    print(states_trans[i][k], '', end='|')
                else:
                    print(states_trans[i][k], end='|')
            else:
                if len(states_trans[i][k]) == 2:
                    print(states_trans[i][k])
                else:
                    print(states_trans[i][k])
    print("-----------------------")
    

def print_states_path():
    iterations = len(states_path)
    for i in range(0, iterations):
        if(i < iterations - 1):
            print(states_path[i], end=" --> ")
        else:
            print(states_path[i])
    print("--------------------------------------------------------------------------------------------------------------")

def check_if_input_correct(coin):
    if coin not in inputs:
        raise ValueError("Podany symbol nie znajduje się w alfabecie automatu.")

def choose_coffee(input):
    global state_index, input_index, chosen_path
    if input == 'm':
        input_index = 3
        states_path.append(states_trans[state_index][input_index])
        state_index = 1
        chosen_path = 'm'
    elif input == 'd':
        input_index = 4
        states_path.append(states_trans[state_index][input_index])
        state_index = 2
        chosen_path = 'd'
    else:
        pass

def go_to_state(input):
    global state_index, input_index
    if input == 'm' or input == 'd':
        pass
    elif input == '1':
        input_index = 0
        states_path.append(states_trans[state_index][input_index])
        if state_index >= 10 and chosen_path == 'd':
            state_index +=1
        else:
            state_index += 2
    elif input == '2':
        input_index = 1
        states_path.append(states_trans[state_index][input_index])
        if state_index >= 10 and chosen_path == 'd':
            state_index +=2
        else:
            state_index += 4
    elif input == '5':
        input_index = 2
        states_path.append(states_trans[state_index][input_index])
        if state_index >= 8 and chosen_path == 'd':
            state_index += 7
        else:
            state_index += 10
    else:
        pass


def change_state(input):
    if(len(states_path) > 1):
        go_to_state(input)
    else:
        choose_coffee(input)
    check_if_more_than_enough()
    check_if_finished()

def check_if_finished():
    global running
    if chosen_path == 'm':
        if state_index == 11:
            print_states_path()
            running = False
            print('Wydanie kawy małej')
    else:
        if state_index == 15:
            print_states_path()
            running = False
            print('Wydanie kawy dużej')

def check_if_more_than_enough():
    global running
    if chosen_path == 'm':
        if state_index > 11:
            print_states_path()
            running = False
            print('Zwrot pieniędzy')
    else:
        if state_index > 15:
            print_states_path()
            running = False
            print('Zwrot pieniędzy')



print_automat()

while(running):
    print_states_path()
    print("Co chcesz zrobić? 1 - wrzuć 1 zł, 2 - wrzuć 2 zł, 5 - wrzuć 5 zł, m - wybierz małą kawę, d - wybierz dużą kawę")
    coin = input()

    try:
        check_if_input_correct(coin)
        change_state(coin)
    except ValueError:
        print("Podany symbol nie znajduje się w alfabecie automatu.")
        exit(0)
