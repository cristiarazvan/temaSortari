import os
import subprocess
import glob
import time
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

T = 2000
T = 25
SIZES = [10, 100, 1000, 50000, 100000]
MAX_NUMS = [10, 100, 10000, 10000000]


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


def gen(n_tests, size, max_num, positive=1, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            arr = [str(random.randint(0 if positive==1 else -max_num, max_num)) for _ in range(size)]
            f.write(" ".join(arr) + "\n")

def genCresc(n_tests, size, max_num, positive=1, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + '\n')
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            arr = []
            last = 0 if positive == 1 else -max_num
            for _ in range(size):
                arr.append(str(random.randint(last, max_num - size - 1)))
                last = arr[-1]
            f.write(" ".join(arr) + '\n')

def genDesc(n_tests, size, max_num, positive=1, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + '\n')
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            arr = []
            last = max_num
            for _ in range(size):
                arr.append(str(random.randint(0 if positive == 1 else -max_num, last)))
                last = arr[-1]
            f.write(" ".join(arr) + '\n')

def genEqual(n_tests, size, max_num, positive=1, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + '\n')
        for _ in range(n_tests):
            f.write(f"{size} {max_num}'\n")
            arr = [str(random.randint(0 if positive==1 else -max_num, max_num)) * size]
            f.write(" ".join(arr) + '\n')

def genAlmostCresc(n_tests, size, max_num, positive=1, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + '\n')
        for _ in range(n_tests):
            f.write(f"{size} {max_num}'\n")
            arr = []
            last = 0 if positive == 1 else -max_num
            for _ in range(size):
                arr.append(str(random.randint(last, max_num - size - 1)))
                last = arr[-1]
            for _ in range(size*0.1):
                index = random.randint(0, size-1)
                arr[index] = str(random.randint(0 if positive==1 else -max_num ,arr[index-1]))
            f.write(" ".join(arr) + '\n')

def genAlmostDesc(n_tests, size, max_num, positive=1, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + '\n')
        for _ in range(n_tests):
            f.write(f"{size} {max_num}'\n")
            arr = []
            last = 0 if positive == 1 else -max_num
            for _ in range(size):
                arr.append(str(random.randint(last, max_num - size - 1)))
                last = arr[-1]
            for _ in range(size*0.1):
                index = random.randint(0, size-1)
                arr[index] = str(random.randint(arr[index-1], max_num))
            f.write(" ".join(arr) + '\n')

def reOrder(lst):
    if len(lst) <= 1:
        return lst
    left = reOrder(lst[::2])
    right = reOrder(lst[1::2])
    return left + right

def gen_merge_worst(n_tests, size, max_num, positive=1, file="teste.in"):
    with open(file, "w") as f:
        f.write(str(n_tests) + "\n")
        for _ in range(n_tests):
            f.write(f"{size} {max_num}\n")
            
            if positive == 1:
                arr = list(range(1, size + 1))
            else:
                if size == 1:
                    arr = [0]
                else:
                    step = (2 * max_num) // (size - 1)
                    arr = [-max_num + i * step for i in range(size)]
            
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


def run(x):
    start_time = time.perf_counter()
    subprocess.run(["./" + x], check=True)
    end_time = time.perf_counter()
    return end_time - start_time


def main():
    execs = compile_all()
    results = {x : {} for x in execs}
    
    for size in SIZES:
        for max_num in MAX_NUMS:
            for sgn in (1, -1):
                print(f"\nGenerating tests with size = {size}, max_num = {max_num}, allow negatives = {True if sgn == -1 else False}")
                gen(T, size, max_num, sgn)

                for ac in execs:
                    t = run(ac)
                    results[ac][(size, max_num, sgn)] = t
                    print(f"Time : {t:.4f} seconds with {ac}")
    
    data_list = []
    for alg, stats in results.items():
        for (size, max_num, sgn), time_taken in stats.items():
            sign_type = "Positive only" if sgn == 1 else "Positive and negative"
            data_list.append({
                "Algorithm": alg,
                "Array Size": size,
                "Max Number": max_num,
                "Number Type": sign_type,
                "Time": time_taken
            })
    
    df = pd.DataFrame(data_list)
    
    plt.figure(figsize=(12, 10))
    heatmap_data = df.pivot_table(
        index="Algorithm", 
        columns="Array Size", 
        values="Time", 
        aggfunc='mean'
    )
    
    alg_order = heatmap_data.mean(axis=1).sort_values().index
    heatmap_data = heatmap_data.reindex(alg_order)
    
    
    sns.heatmap(heatmap_data, annot=True, fmt=".4f", cmap="RdYlGn_r", 
                cbar_kws={'label': 'Time (seconds)'},
                robust=True)
    plt.title("Sorting Algorithm Performance Across Array Sizes")
    plt.tight_layout()
    plt.savefig("performance_heatmap.png")
    plt.show()
    
    plt.figure(figsize=(14, 8))
    
    line_data = df.pivot_table(
        index="Array Size", 
        columns="Algorithm", 
        values="Time", 
        aggfunc='mean'
    )
    
    for alg in line_data.columns:
        plt.plot(line_data.index, line_data[alg], marker='o', linewidth=2, label=alg)
    
    plt.xscale('log') 
    plt.title("Sorting Algorithm Performance Across Array Sizes")
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time")
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig("performance_line_graph.png")
    plt.show()
    

if __name__ == "__main__":
    main()