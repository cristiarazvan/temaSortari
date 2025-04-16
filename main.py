import os
import subprocess
import glob
import time
import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

T = 10000
SIZES = [10, 100, 1000, 10000, 100000, 1000000]
MAX_NUMS = [1000000]


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
            x = max_num - 1
            arr = [
                str(random.randint(0 if positive == 1 else -x, x))
                for _ in range(size)
            ]
            f.write(" ".join(arr) + "\n")


def run(x):
    start_time = time.perf_counter()
    subprocess.run(["./" + x], check=True)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    execs = compile_all()
    results = {x: {} for x in execs}
    
    # Dummy tests 
    dummy_size = 1000
    dummy_max = 10000
    
    # Generate a dummy test case
    gen(1, dummy_size, dummy_max, 1)
    
    for algo in execs:
        dummy_time = run(algo)
    
    for size in SIZES:
        for max_num in MAX_NUMS:
            for sgn in (1, -1):
                print(
                    f"\nGenerating tests with size = {size}, max_num = {max_num}, allow negatives = {True if sgn == -1 else False}"
                )
                gen(T, size, max_num, sgn)

                for ac in execs:
                    t = run(ac)
                    results[ac][(size, max_num, sgn)] = t
                    print(f"Time : {t:.4f} seconds with {ac}")

    data_list = []
    for alg, stats in results.items():
        for (size, max_num, sgn), time_taken in stats.items():
            sign_type = "Positive only" if sgn == 1 else "Positive and negative"
            data_list.append(
                {
                    "Algorithm": alg,
                    "Array Size": size,
                    "Max Number": max_num,
                    "Number Type": sign_type,
                    "Time": time_taken,
                }
            )

    df = pd.DataFrame(data_list)

    plt.figure(figsize=(12, 10))
    heatmap_data = df.pivot_table(
        index="Algorithm", columns="Array Size", values="Time", aggfunc="mean"
    )

    alg_order = heatmap_data.mean(axis=1).sort_values().index
    heatmap_data = heatmap_data.reindex(alg_order)

    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".4f",
        cmap="RdYlGn_r",
        cbar_kws={"label": "Time (seconds)"},
        robust=True,
    )
    plt.title("Sorting Algorithm Performance Across Array Sizes")
    plt.tight_layout()
    plt.savefig("performance_heatmap.png")
    plt.show()

    plt.figure(figsize=(14, 8))

    line_data = df.pivot_table(
        index="Array Size", columns="Algorithm", values="Time", aggfunc="mean"
    )

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
              '#1a55FF', '#FF5733', '#33FF57', '#FF33A8', '#33A8FF']

    for i, alg in enumerate(line_data.columns):
        color_idx = i % len(colors) 
        plt.plot(line_data.index, line_data[alg], marker='o', linewidth=2, 
                 label=alg, color=colors[color_idx], markersize=7)

    plt.xscale("log")
    plt.title("Sorting Algorithm Performance Across Array Sizes")
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time")
    plt.grid(True, alpha=0.3)
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.savefig("performance_line_graph.png")
    plt.show()


if __name__ == "__main__":
    main()