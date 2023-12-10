# if __name__ == '__main__':
#     # Recursive factorial function
#     def factorial_recursive(n):
#         if n <= 1:
#             return 1
#         return n * factorial_recursive(n - 1)
#
#
#     # Iterative factorial function
#     def factorial_iterative(n):
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#
#
#     # Compare space usage of recursive and iterative factorial
#     import tracemalloc
#
#     tracemalloc.start()
#
#     # Measure memory usage for recursive factorial
#     # snapshot_before_recursive = tracemalloc.take_snapshot()
#     result_recursive = factorial_recursive(10)
#     # snapshot_after_recursive = tracemalloc.take_snapshot()
#     memory_change_recursive = tracemalloc.get_traced_memory()
#     tracemalloc.stop()
#
#     tracemalloc.start()
#     # Measure memory usage for iterative factorial
#     snapshot_before_iterative = tracemalloc.take_snapshot()
#     result_iterative = factorial_iterative(10)
#     snapshot_after_iterative = tracemalloc.take_snapshot()
#     # memory_change_iterative = tracemalloc.get_traced_memory()
#     tracemalloc.stop()
#
#     # stats_recursive = snapshot_after_recursive.compare_to(snapshot_before_recursive, 'filename')
#     # memory_change_recursive = sum(stat.size_diff for stat in stats_recursive)
#
#     stats_iterative = snapshot_after_iterative.compare_to(snapshot_before_iterative, 'filename')
#     memory_change_iterative = sum(stat.size_diff for stat in stats_iterative)
#
#     print(f"Memory change for recursive factorial: {memory_change_recursive[0] / (1024)} KB")
#     print(f"Memory change for iterative factorial: {memory_change_iterative / (1024)} KB")
#
#     tracemalloc.stop()

# import tracemalloc
#
# # 示例函数，分配一些内存
# def allocate_memory():
#     a = [i for i in range(10000)]
#     return a
#
# if __name__ == '__main__':
#     # 启动内存跟踪
#     tracemalloc.start()
#
#     # 执行函数
#     some_data = allocate_memory()
#
#     # 获取内存使用情况
#     memory_usage = tracemalloc.get_traced_memory()
#     print(f"Memory usage: {memory_usage / 10**6} MB")  # 将字节转换为兆字节
#
#     # 停止内存跟踪
#     tracemalloc.stop()

import plotly.graph_objects as go
from plotly.subplots import make_subplots

if __name__ == '__main__':
    # 准备数据
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 13, 18, 20]

    # 创建图表
    fig = go.Figure()

    # 添加散点图
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=dict(size=12, color='blue')
    ))

    # 添加方框和标签
    fig.add_shape(
        type="rect",
        xref="x",
        yref="y",
        x0=2,  # 方框左下角 x 坐标
        y0=12,  # 方框左下角 y 坐标
        x1=4,  # 方框右上角 x 坐标
        y1=19,  # 方框右上角 y 坐标
        line=dict(color="black", width=2),
        fillcolor="lightgrey"
    )

    fig.add_annotation(
        x=3,  # 标签 x 坐标
        y=15,  # 标签 y 坐标
        text="区域 A",  # 标签文本
        showarrow=False,
        font=dict(color="black", size=12)
    )

    # 设置布局
    fig.update_layout(
        title="带标签的方框示例",
        xaxis_title="X 轴",
        yaxis_title="Y 轴"
    )

    # 显示图表
    fig.show()


