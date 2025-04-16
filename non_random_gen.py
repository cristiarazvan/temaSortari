import random
import os
import subprocess
import glob
import time
import matplotlib.pyplot as plt
import pandas as pd




T = 50
SIZES = [10, 100, 1000, 10000, 50000]
MAX_NUMS = [1000000]

def gen(n_tests, size, max_num, positive=1, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            x = max_num - 1
            arr = [
                str(random.randint(0 if positive == 1 else -x, x))
                for _ in range(size)
            ]
            f.write(" ".join(arr) + "\n")


def reOrder(lst):
    if len(lst) <= 1:
        return lst
    left = reOrder(lst[::2])
    right = reOrder(lst[1::2])
    return left + right

def genCresc(n_tests, size, max_num, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            arr = []
            last = 0 
            for _ in range(size):
                current = random.randint(last, max_num - size - 1)
                arr.append(str(current))
                last = current  
            f.write(" ".join(arr) + "\n")


def genDesc(n_tests, size, max_num, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            arr = []
            last = max_num
            for _ in range(size):
                current = random.randint(0 , last)
                arr.append(str(current))
                last = current  
            f.write(" ".join(arr) + "\n")


def genEqual(n_tests, size, max_num, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            random_value = str(random.randint(0, max_num))
            arr = [random_value] * size  
            f.write(" ".join(arr) + "\n")


def genAlmostCresc(n_tests, size, max_num, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            arr = []
            last = 0 
            for _ in range(size):
                current = random.randint(last, max_num - size - 1)
                arr.append(str(current))
                last = current
            
            num_to_modify = int(size * 0.1)
            for _ in range(num_to_modify):
                index = random.randint(0, size - 1)
                if index > 0:
                    previous_value = int(arr[index - 1])
                    arr[index] = str(random.randint(0, previous_value))
            
            f.write(" ".join(arr) + "\n")


def genAlmostDesc(n_tests, size, max_num, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            arr = []
            last = max_num
            for _ in range(size):
                current = random.randint(0, last)
                arr.append(str(current))
                last = current
            
            num_to_modify = int(size * 0.1)
            for _ in range(num_to_modify):
                index = random.randint(0, size - 1)
                if index > 0:
                    previous_value = int(arr[index - 1])
                    arr[index] = str(random.randint(previous_value, max_num))
            
            f.write(" ".join(arr) + "\n")


def gen_merge_worst(n_tests, size, max_num, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")

            arr = list(range(1, size + 1))
            worst_arr = reOrder(arr)

            f.write(" ".join(map(str, worst_arr)) + "\n")


def gen_timsort_worst_case(n_tests, size, max_num, file="teste.in"):
    MIN_RUN = 32

    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")

        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")

            nums = []
            need = (size + MIN_RUN - 1) // MIN_RUN

            for i in range(need):
                run_size = min(MIN_RUN, size - i * MIN_RUN)
                if run_size <= 0:
                    break

                if i % 2 == 0:
                    # Crescator
                    start = i * max_num // need
                    run = list(range(start, start + run_size))
                else:
                    # Descrescator
                    start = (i + 1) * max_num // need - 1
                    run = list(range(start, start - run_size, -1))

                nums.extend(run)

            nums = nums[:size]

            if len(nums) < size:
                nums.extend([0] * (size - len(nums)))

            f.write(" ".join(map(str, nums)) + "\n")


def gen_quick_sort_worst_case(n_tests, size, max_num, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            arr = list(range(1, size + 1))
            f.write(" ".join(map(str, arr)) + "\n")


GENERATOR_LIST = [
    (genCresc, "Sorted Arrays (Ascending)"),
    (genDesc, "Sorted Arrays (Descending)"),
    (genEqual, "Equal Elements"),
    (genAlmostCresc, "Nearly Sorted (Ascending)"),
    (genAlmostDesc, "Nearly Sorted (Descending)"),
    (gen_merge_worst, "Merge Sort Worst Case"),
    (gen_quick_sort_worst_case, "Quick Sort Worst Case"),
    (gen_timsort_worst_case, "TimSort Worst Case")
]


def compile_all():
    cpps = glob.glob("*.cpp")
    execs = []
    for file in cpps:
        name = os.path.splitext(file)[0]
        cmd = ["g++", "-O2", file, "-o", name]
        print(f"Compiling {file} -> {name}")
        subprocess.run(cmd, check=True)
        execs.append(name)
    return execs

def run(x):
    start_time = time.perf_counter()
    subprocess.run(["./" + x], check=True)
    end_time = time.perf_counter()
    return end_time - start_time

def run_nonrand(gen_func, gen_name, execs, sizes=SIZES, max_nums=MAX_NUMS):
    print(f"\nRunning benchmarks with {gen_name}...")
    nonrand_res = {x: {} for x in execs}
    
    for size in sizes:
        for max_num in max_nums:
            print(f"\nGenerating {gen_name} tests with size = {size}")
            gen_func(T, size, max_num)
                
            for ac in execs:
                t = run(ac)
                nonrand_res[ac][(size, max_num)] = t
                print(f"Time : {t:.4f} seconds with {ac}")
    
    return nonrand_res

def plot_nonrand_res(all_results, generator_names):
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
              '#1a55FF', '#FF5733', '#33FF57', '#FF33A8', '#33A8FF']
            
    half_point = len(generator_names) // 2
    
    for window_index in range(2):
        start_idx = half_point * window_index
        end_idx = half_point * (window_index + 1) if window_index == 0 else len(generator_names)
        
        current_generators = generator_names[start_idx:end_idx]
        current_results = all_results[start_idx:end_idx]
        
        if not current_generators:
            continue
            
        n = len(current_generators)
        cols = 2
        rows = (n + cols - 1) // cols 
        
        fig, axes = plt.subplots(rows, cols, figsize=(20, 5 * rows))
        
        if rows == 1 and cols == 1:
            axes = [axes]
        elif rows == 1 or cols == 1:
            axes = axes.flatten() 
        else:
            axes = axes.flatten() 
        
        for i, (gen_name, results) in enumerate(zip(current_generators, current_results)):
            ax = axes[i]
                
            data_list = []
            for alg, stats in results.items():
                for (size, max_num), time_taken in stats.items():
                    data_list.append({
                        "Algorithm": alg,
                        "Array Size": size,
                        "Max Number": max_num,
                        "Time": time_taken,
                    })
            
            if not data_list:
                ax.text(0.5, 0.5, f"No data for {gen_name}", 
                        horizontalalignment='center', verticalalignment='center')
                continue
                
            spec_df = pd.DataFrame(data_list)
            
            line_data = spec_df.pivot_table(
                index="Array Size", columns="Algorithm", values="Time", aggfunc="mean"
            )
            
            for j, alg in enumerate(line_data.columns):
                color_idx = j % len(colors)
                ax.plot(line_data.index, line_data[alg], 
                        marker='o', linewidth=2, label=alg, 
                        color=colors[color_idx], markersize=7)
            
            ax.set_xscale("log")
            ax.set_yscale("log") 
            ax.set_title(f"Performance on {gen_name}")
            ax.set_xlabel("Array Size")
            ax.set_ylabel("Execution Time (s)")
            ax.grid(True, alpha=0.3)
            ax.legend(loc="upper left", fontsize='small')
        
        for j in range(i + 1, rows * cols):
            if j < len(axes):
                axes[j].axis('off')
                
        plt.tight_layout()
        plt.savefig(f"performance_specialized_cases_window{window_index+1}.png")
        plt.show()

def run_all(sizes=SIZES, max_nums=MAX_NUMS):
    execs = compile_all()
    results = {x: {} for x in execs}
    
    # Dummy tests 
    dummy_size = 1000
    dummy_max = 10000
    
    # Generate a dummy test case
    gen(1, dummy_size, dummy_max, 1)
    
    for algo in execs:
        dummy_time = run(algo) 
    
    all_nonrand_res = []
    generator_names = []
    
    for gen_func, gen_name in GENERATOR_LIST:
        print(f"\nRunning benchmarks with {gen_name}...")
        generator_names.append(gen_name)
        results = run_nonrand(gen_func, gen_name, execs, sizes, max_nums)
        all_nonrand_res.append(results)
    
    plot_nonrand_res(all_nonrand_res, generator_names)

if __name__ == "__main__":
    print("Running non random benchmarks...")
    run_all()