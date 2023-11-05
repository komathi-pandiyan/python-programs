def fractional_knapsack(N, W, values, weight):
    value_per_weight = [(values[i] / weight[i], i) for i in range(N)]
    value_per_weight.sort(reverse=True)

    total_value = 0.0
    current_weight = 0

    for ratio, i in value_per_weight:
        if current_weight + weight[i] <= W:
            total_value += values[i]
            current_weight += weight[i]
        else:
            fraction = (W - current_weight) / weight[i]
            total_value += fraction * values[i]
            break
    return total_value
N = 3
W = 50
values = [60, 100, 120]
weight = [10, 20, 30]

result = fractional_knapsack(N, W, values, weight)
print("{:.2f}".format(result))

