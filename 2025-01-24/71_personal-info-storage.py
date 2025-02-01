'''
def day_calculator(date_str):
    """Converts a date (YYYYMMDD format) into a numerical value for comparison."""
    print(f'{int(date_str[:4])} * 12 * 28 + {int(date_str[4:6])} * 28 + {int(date_str[6:8])}')
    year, month, day = int(date_str[:4]), int(date_str[4:6]), int(date_str[6:8])
    return year * 12 * 28 + month * 28 + day  # Convert year and month to days
    '''

def day_calculator(string):
    # print(f'{string[:4]}*365 + {string[4:6]}*28 + {string[6:8]}')
    return int(string[:4])*12*28 + int(string[4:6])*28 + int(string[6:8])


def solution(today, terms, privacies):

    # removing the dots from the list 'privacies' and the string 'today'
    today = "".join(today.split("."))
    today_days = day_calculator(today)

    # changing the list 'terms' into a dictionary
    terms_dict = {}
    for i in range(len(terms)):
        terms_dict[terms[i][0]] = int(terms[i][2:])*28

    expired_list = []
    for i in range(len(privacies)):
        privacy_data = privacies[i].split()
        privacy_date = "".join(privacy_data[0].split("."))
        expiry_days = day_calculator(privacy_date) + terms_dict[privacy_data[1]] - 1
        if expiry_days < today_days:
            expired_list.append(i+1)


    return expired_list
            

# Test cases
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# print(solution(today, terms, privacies))

print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])) 
