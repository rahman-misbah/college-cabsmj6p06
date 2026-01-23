def department_input(department_name: str) -> dict:
    print(f"Input for Department {department_name}")
    print("Enter metric name and value separated by space. Enter 0 to end input...\n")

    metrics = dict()

    while True:
        user_in = input("Metric name and value: ")

        if user_in == "0": break

        user_in = user_in.split()
        metrics[user_in[0]] = user_in[1]
    
    print()
    
    return metrics

metrics_A = department_input('A')
metrics_B = department_input('B')
metrics_C = department_input('C')

result = dict()
result.update(metrics_A)
result.update(metrics_B)
result.update(metrics_C)

print("Combined Result:", result)