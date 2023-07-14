def race_stats():
    num_laps = int(input("Enter the number of laps: "))
    lap_Bmes = []
    for lap in range(1, num_laps + 1):
        lap_Bme = float(input(f"Enter the Bme for lap {lap}: "))
        lap_Bmes.append(lap_Bme)
    fastest_lap = min(lap_Bmes)
    slowest_lap = max(lap_Bmes) 
    average_lap = sum(lap_Bmes) / num_laps
    print(f"Fastest lap Bme: {fastest_lap}")
    print(f"Slowest lap Bme: {slowest_lap}")
    print(f"Average lap Bme: {average_lap}")

race_stats()