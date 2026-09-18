import numpy as np

data = [100.1, 100.2, 100.3, 100.4, 99.5, 99.6, 99.7, 99.8, 99.9, 100.0]
usl = 102.0 #MAX in Ruler
lsl = 98.0  #MIN in Ruler

def cpk(test_data, usl, lsl):
    mean = np.mean(test_data)
    std = np.std(test_data, ddof=1) # sample standard deviation
    cpk = min((usl - mean) / (3 * std), (mean - lsl) / (3 * std))

    return mean, std, cpk

mean, std, cpk = cpk(data, usl, lsl)
print(f"均值：{mean:.2f}, 标准差：{std:.2f}, CPK：{cpk:.2f}")