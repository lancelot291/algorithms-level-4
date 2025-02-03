def solution(id_list, report, k):

    # change the form of the report list
    report = list(set(report))
    for i in range(len(report)):
        report[i] = report[i].split()
    # print(report)

    # create a dictionary that has the list of people who are reported by each person
    report_dict = {}
    for name in id_list:
        report_dict[name] = []
    for i in range(len(report)):
        report_dict[report[i][0]].append(report[i][1])
    # print(report_dict)

    # create a dictionary that has the number of message that each person has gotten
    message_count = {}
    for name in id_list:
        message_count[name] = 0

    # create a dictionary that has the number being reported for each person
    report_count = {}
    for name in id_list:
        report_count[name] = 0   
    for i in range(len(report)):
        report_count[report[i][1]] += 1
    # print(report_count)


    # check if the number of reports for each person is greater than or equal to k 
    # and send message to the reporters
    for criminal in id_list:
        if report_count[criminal] >= k:
            for reporter in id_list:
                if criminal in report_dict[reporter]:
                    message_count[reporter] += 1

    return list(message_count.values())
     

    
    

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))