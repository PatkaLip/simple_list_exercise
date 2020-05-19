def fill_the_sequence():
    data_in =[1, 2, 4, 5, 6, 8]
    n = 10
    missing_data = []
    for i in range(len(data_in)-1):
        if data_in[i+1] - data_in[i]>1:
            missing_data.append(data_in[i]+1)
        if i+2 == len(data_in):
            while data_in[i+1] != n:
                missing_data.append(data_in[i+1] + 1)
                data_in[i+1] += 1
    print(missing_data)


fill_the_sequence()