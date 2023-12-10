import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import math

if __name__ == '__main__':
    file_path = 'experiment result_Banchmark_2.xlsx'  # 替换成您的 Excel 文件路径
    data_result_random = pd.read_excel(file_path, 'maze-128-128-2')
    # Add data
    map_name = data_result_random['Heuristics']
    a_star_time_1 = data_result_random['A* time (s)']
    # a_star_time = [math.log(x, 2) for x in a_star_time]
    IIDA_time_1 = data_result_random['IIDA time (s)']
    # IIDA_time = [math.log(x, 2) for x in IIDA_time]
    LRTA_time_1 = data_result_random['LRTA time (s)']
    # LRTA_time = [math.log(x, 2) for x in LRTA_time]
    tt_IDA_time_1 = data_result_random['TT IDA time (s)']
    # tt_IDA_time = [math.log(x, 2) for x in tt_IDA_time]
    a_star_peak_1 = data_result_random['A* peak memory size']
    a_star_peak_1 = [math.log(x, 2) for x in a_star_peak_1]
    LRTA_peak_1 = data_result_random['LRTA peak memory size']
    LRTA_peak_1 = [math.log(x, 2) for x in LRTA_peak_1]
    tt_IDA_peak_1 = data_result_random['TT IDA peak memory size']
    tt_IDA_peak_1 = [math.log(x, 2) for x in tt_IDA_peak_1]
    IIDA_peak_1 = data_result_random['IIDA peak memory size']
    IIDA_peak_1 = [math.log(x, 2) for x in IIDA_peak_1]
    a_star_edge_1 = data_result_random['A* traversed edges']
    a_star_edge_1 = [math.log(x, 2) for x in a_star_edge_1]
    LRTA_edge_1 = data_result_random['LRTA traversed edges']
    LRTA_edge_1 = [math.log(x, 2) for x in LRTA_edge_1]
    tt_IDA_edge_1 = data_result_random['TT IDA traversed edges']
    tt_IDA_edge_1 = [math.log(x, 2) for x in tt_IDA_edge_1]
    IIDA_edge_1 = data_result_random['IIDA traversed edges']
    IIDA_edge_1 = [math.log(x, 2) for x in IIDA_edge_1]
    trace_a_star_time_1 = go.Bar(x=map_name, y=a_star_time_1, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_time_1 = go.Bar(x=map_name, y=LRTA_time_1, name='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_time_1 = go.Bar(x=map_name, y=tt_IDA_time_1, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_time_1 = go.Bar(x=map_name, y=IIDA_time_1, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_peak_1 = go.Bar(x=map_name, y=a_star_peak_1, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_peak_1 = go.Bar(x=map_name, y=LRTA_peak_1, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_peak_1 = go.Bar(x=map_name, y=tt_IDA_peak_1, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_peak_1 = go.Bar(x=map_name, y=IIDA_peak_1, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_edge_1 = go.Bar(x=map_name, y=a_star_edge_1, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_edge_1 = go.Bar(x=map_name, y=LRTA_edge_1, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_edge_1 = go.Bar(x=map_name, y=tt_IDA_edge_1, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_edge_1 = go.Bar(x=map_name, y=IIDA_edge_1, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))

    data_result_random = pd.read_excel(file_path, 'maze-32-32-2')
    # Add data
    a_star_time_2 = data_result_random['A* time (s)']
    # a_star_time = [math.log(x, 2) for x in a_star_time]
    IIDA_time_2 = data_result_random['IIDA time (s)']
    # IIDA_time = [math.log(x, 2) for x in IIDA_time]
    LRTA_time_2 = data_result_random['LRTA time (s)']
    # LRTA_time = [math.log(x, 2) for x in LRTA_time]
    tt_IDA_time_2 = data_result_random['TT IDA time (s)']
    # tt_IDA_time = [math.log(x, 2) for x in tt_IDA_time]
    a_star_peak_2 = data_result_random['A* peak memory size']
    LRTA_peak_2 = data_result_random['LRTA peak memory size']
    tt_IDA_peak_2 = data_result_random['TT IDA peak memory size']
    IIDA_peak_2 = data_result_random['IIDA peak memory size']
    a_star_edge_2 = data_result_random['A* traversed edges']
    a_star_edge_2 = [math.log(x, 2) for x in a_star_edge_2]
    LRTA_edge_2 = data_result_random['LRTA traversed edges']
    LRTA_edge_2 = [math.log(x, 2) for x in LRTA_edge_2]
    tt_IDA_edge_2 = data_result_random['TT IDA traversed edges']
    tt_IDA_edge_2 = [math.log(x, 2) for x in tt_IDA_edge_2]
    IIDA_edge_2 = data_result_random['IIDA traversed edges']
    IIDA_edge_2 = [math.log(x, 2) for x in IIDA_edge_2]
    trace_a_star_time_2 = go.Bar(x=map_name, y=a_star_time_2, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_time_2 = go.Bar(x=map_name, y=LRTA_time_2, name='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_time_2 = go.Bar(x=map_name, y=tt_IDA_time_2, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_time_2 = go.Bar(x=map_name, y=IIDA_time_2, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_peak_2 = go.Bar(x=map_name, y=a_star_peak_2, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_peak_2 = go.Bar(x=map_name, y=LRTA_peak_2, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_peak_2 = go.Bar(x=map_name, y=tt_IDA_peak_2, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_peak_2 = go.Bar(x=map_name, y=IIDA_peak_2, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_edge_2 = go.Bar(x=map_name, y=a_star_edge_2, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_edge_2 = go.Bar(x=map_name, y=LRTA_edge_2, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_edge_2 = go.Bar(x=map_name, y=tt_IDA_edge_2, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_edge_2 = go.Bar(x=map_name, y=IIDA_edge_2, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))

    data_result_random = pd.read_excel(file_path, 'random-64-64-20')
    # Add data
    a_star_time_3 = data_result_random['A* time (s)']
    # a_star_time = [math.log(x, 2) for x in a_star_time]
    IIDA_time_3 = data_result_random['IIDA time (s)']
    # IIDA_time = [math.log(x, 2) for x in IIDA_time]
    LRTA_time_3 = data_result_random['LRTA time (s)']
    # LRTA_time = [math.log(x, 2) for x in LRTA_time]
    tt_IDA_time_3 = data_result_random['TT IDA time (s)']
    # tt_IDA_time = [math.log(x, 2) for x in tt_IDA_time]
    a_star_peak_3 = data_result_random['A* peak memory size']
    LRTA_peak_3 = data_result_random['LRTA peak memory size']
    tt_IDA_peak_3 = data_result_random['TT IDA peak memory size']
    IIDA_peak_3 = data_result_random['IIDA peak memory size']
    a_star_edge_3 = data_result_random['A* traversed edges']
    a_star_edge_3 = [math.log(x, 2) for x in a_star_edge_3]
    LRTA_edge_3 = data_result_random['LRTA traversed edges']
    LRTA_edge_3 = [math.log(x, 2) for x in LRTA_edge_3]
    tt_IDA_edge_3 = data_result_random['TT IDA traversed edges']
    tt_IDA_edge_3 = [math.log(x, 2) for x in tt_IDA_edge_3]
    IIDA_edge_3 = data_result_random['IIDA traversed edges']
    IIDA_edge_3 = [math.log(x, 2) for x in IIDA_edge_3]
    trace_a_star_time_3 = go.Bar(x=map_name, y=a_star_time_3, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_time_3 = go.Bar(x=map_name, y=LRTA_time_3, name='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_time_3 = go.Bar(x=map_name, y=tt_IDA_time_3, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_time_3 = go.Bar(x=map_name, y=IIDA_time_3, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_peak_3 = go.Bar(x=map_name, y=a_star_peak_3, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_peak_3 = go.Bar(x=map_name, y=LRTA_peak_3, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_peak_3 = go.Bar(x=map_name, y=tt_IDA_peak_3, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_peak_3 = go.Bar(x=map_name, y=IIDA_peak_3, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_edge_3 = go.Bar(x=map_name, y=a_star_edge_3, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_edge_3 = go.Bar(x=map_name, y=LRTA_edge_3, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_edge_3 = go.Bar(x=map_name, y=tt_IDA_edge_3, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_edge_3 = go.Bar(x=map_name, y=IIDA_edge_3, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))

    data_result_random = pd.read_excel(file_path, 'room-32-32-4')
    # Add data
    a_star_time_4 = data_result_random['A* time (s)']
    # a_star_time = [math.log(x, 2) for x in a_star_time]
    IIDA_time_4 = data_result_random['IIDA time (s)']
    # IIDA_time = [math.log(x, 2) for x in IIDA_time]
    LRTA_time_4 = data_result_random['LRTA time (s)']
    # LRTA_time = [math.log(x, 2) for x in LRTA_time]
    tt_IDA_time_4 = data_result_random['TT IDA time (s)']
    # tt_IDA_time = [math.log(x, 2) for x in tt_IDA_time]
    a_star_peak_4 = data_result_random['A* peak memory size']
    LRTA_peak_4 = data_result_random['LRTA peak memory size']
    tt_IDA_peak_4 = data_result_random['TT IDA peak memory size']
    IIDA_peak_4 = data_result_random['IIDA peak memory size']
    a_star_edge_4 = data_result_random['A* traversed edges']
    a_star_edge_4 = [math.log(x, 2) for x in a_star_edge_4]
    LRTA_edge_4 = data_result_random['LRTA traversed edges']
    LRTA_edge_4 = [math.log(x, 2) for x in LRTA_edge_4]
    tt_IDA_edge_4 = data_result_random['TT IDA traversed edges']
    tt_IDA_edge_4 = [math.log(x, 2) for x in tt_IDA_edge_4]
    IIDA_edge_4 = data_result_random['IIDA traversed edges']
    IIDA_edge_4 = [math.log(x, 2) for x in IIDA_edge_4]
    trace_a_star_time_4 = go.Bar(x=map_name, y=a_star_time_4, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_time_4 = go.Bar(x=map_name, y=LRTA_time_4, name='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_time_4 = go.Bar(x=map_name, y=tt_IDA_time_4, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_time_4 = go.Bar(x=map_name, y=IIDA_time_4, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_peak_4 = go.Bar(x=map_name, y=a_star_peak_4, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_peak_4 = go.Bar(x=map_name, y=LRTA_peak_4, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_peak_4 = go.Bar(x=map_name, y=tt_IDA_peak_4, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_peak_4 = go.Bar(x=map_name, y=IIDA_peak_4, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_edge_4 = go.Bar(x=map_name, y=a_star_edge_4, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_edge_4 = go.Bar(x=map_name, y=LRTA_edge_4, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_edge_4 = go.Bar(x=map_name, y=tt_IDA_edge_4, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_edge_4 = go.Bar(x=map_name, y=IIDA_edge_4, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))

    data_result_random = pd.read_excel(file_path, 'room-64-64-8')
    # Add data
    a_star_time_5 = data_result_random['A* time (s)']
    # a_star_time = [math.log(x, 2) for x in a_star_time]
    IIDA_time_5 = data_result_random['IIDA time (s)']
    # IIDA_time = [math.log(x, 2) for x in IIDA_time]
    LRTA_time_5 = data_result_random['LRTA time (s)']
    # LRTA_time = [math.log(x, 2) for x in LRTA_time]
    tt_IDA_time_5 = data_result_random['TT IDA time (s)']
    # tt_IDA_time = [math.log(x, 2) for x in tt_IDA_time]
    a_star_peak_5 = data_result_random['A* peak memory size']
    LRTA_peak_5 = data_result_random['LRTA peak memory size']
    tt_IDA_peak_5 = data_result_random['TT IDA peak memory size']
    IIDA_peak_5 = data_result_random['IIDA peak memory size']
    a_star_edge_5 = data_result_random['A* traversed edges']
    a_star_edge_5 = [math.log(x, 2) for x in a_star_edge_5]
    LRTA_edge_5 = data_result_random['LRTA traversed edges']
    LRTA_edge_5 = [math.log(x, 2) for x in LRTA_edge_5]
    tt_IDA_edge_5 = data_result_random['TT IDA traversed edges']
    tt_IDA_edge_5 = [math.log(x, 2) for x in tt_IDA_edge_5]
    IIDA_edge_5 = data_result_random['IIDA traversed edges']
    IIDA_edge_5 = [math.log(x, 2) for x in IIDA_edge_5]
    trace_a_star_time_5 = go.Bar(x=map_name, y=a_star_time_5, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_time_5 = go.Bar(x=map_name, y=LRTA_time_5, name='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_time_5 = go.Bar(x=map_name, y=tt_IDA_time_5, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_time_5 = go.Bar(x=map_name, y=IIDA_time_5, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_peak_5 = go.Bar(x=map_name, y=a_star_peak_5, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_peak_5 = go.Bar(x=map_name, y=LRTA_peak_5, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_peak_5 = go.Bar(x=map_name, y=tt_IDA_peak_5, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_peak_5 = go.Bar(x=map_name, y=IIDA_peak_5, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))
    trace_a_star_edge_5 = go.Bar(x=map_name, y=a_star_edge_5, name='A*', marker=dict(color=['firebrick', 'firebrick', 'firebrick', 'firebrick']))
    trace_LRTA_edge_5 = go.Bar(x=map_name, y=LRTA_edge_5, name ='LRTA*', marker=dict(color=['royalblue', 'royalblue', 'royalblue', 'royalblue']))
    trace_tt_IDA_edge_5 = go.Bar(x=map_name, y=tt_IDA_edge_5, name='TT IDA*', marker=dict(color=['#f207e7', '#f207e7', '#f207e7', '#f207e7']))
    trace_IIDA_edge_5 = go.Bar(x=map_name, y=IIDA_edge_5, name='IIDA*', marker=dict(color=['#08bd0e', '#08bd0e', '#08bd0e', '#08bd0e']))

    fig = make_subplots(rows=2, cols=5, subplot_titles=(
        'CPU Running Time (maze-128-128-2)', 'CPU Running Time (maze-32-32-2)', 'CPU Running Time (random-64-64-20)',
        'CPU Running Time (room-32-32-4)', 'CPU Running Time (room-64-64-8)', 'CPU Running Time (maze-128-128-2)',
        'CPU Running Time (maze-32-32-2)', 'CPU Running Time (random-64-64-20)',
        'CPU Running Time (room-32-32-4)', 'CPU Running Time (room-64-64-8)'))

    fig.add_trace(trace_a_star_time_1, row=1, col=1)
    fig.add_trace(trace_IIDA_time_1, row=1, col=1)
    fig.add_trace(trace_LRTA_time_1, row=2, col=1)
    fig.add_trace(trace_tt_IDA_time_1, row=2, col=1)
    fig.add_trace(trace_a_star_time_2, row=1, col=2)
    fig.add_trace(trace_IIDA_time_2, row=1, col=2)
    fig.add_trace(trace_LRTA_time_2, row=2, col=2)
    fig.add_trace(trace_tt_IDA_time_2, row=2, col=2)
    fig.add_trace(trace_a_star_time_3, row=1, col=3)
    fig.add_trace(trace_IIDA_time_3, row=1, col=3)
    fig.add_trace(trace_LRTA_time_3, row=2, col=3)
    fig.add_trace(trace_tt_IDA_time_3, row=2, col=3)
    fig.add_trace(trace_a_star_time_4, row=1, col=4)
    fig.add_trace(trace_IIDA_time_4, row=1, col=4)
    fig.add_trace(trace_LRTA_time_4, row=2, col=4)
    fig.add_trace(trace_tt_IDA_time_4, row=2, col=4)
    fig.add_trace(trace_a_star_time_5, row=1, col=5)
    fig.add_trace(trace_IIDA_time_5, row=1, col=5)
    fig.add_trace(trace_LRTA_time_5, row=2, col=5)
    fig.add_trace(trace_tt_IDA_time_5, row=2, col=5)

    fig.update_layout(height=900, width=1800, font=dict(family="Arial", size=15, color="black"))
    fig.update_layout(barmode='group')
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=1)
    fig.update_xaxes(title_text='Heuristic Function', row=2, col=1)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=2)
    fig.update_xaxes(title_text='Heuristic Function', row=2, col=2)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=3)
    fig.update_xaxes(title_text='Heuristic Function', row=2, col=3)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=4)
    fig.update_xaxes(title_text='Heuristic Function', row=2, col=4)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=5)
    fig.update_xaxes(title_text='Heuristic Function', row=2, col=5)
    fig.update_yaxes(title_text='Time (s)', row=1, col=1)
    fig.update_yaxes(title_text='Time (s)', row=2, col=1)
    fig.update_yaxes(title_text='Time (s)', row=1, col=2)
    fig.update_yaxes(title_text='Time (s)', row=2, col=2)
    fig.update_yaxes(title_text='Time (s)', row=1, col=3)
    fig.update_yaxes(title_text='Time (s)', row=2, col=3)
    fig.update_yaxes(title_text='Time (s)', row=1, col=4)
    fig.update_yaxes(title_text='Time (s)', row=2, col=4)
    fig.update_yaxes(title_text='Time (s)', row=1, col=5)
    fig.update_yaxes(title_text='Time (s)', row=2, col=5)
    fig.show()

    fig = make_subplots(rows=1, cols=5, subplot_titles=(
        'Peak Memory Used (maze-128-128-2)',
        'Peak Memory Used (maze-32-32-2)',
        'Peak Memory Used (random-64-64-20)',
        'Peak Memory Used (room-32-32-4)',
        'Peak Memory Used (room-64-64-8)'))

    fig.add_trace(trace_a_star_peak_1, row=1, col=1)
    fig.add_trace(trace_LRTA_peak_1, row=1, col=1)
    fig.add_trace(trace_tt_IDA_peak_1, row=1, col=1)
    fig.add_trace(trace_IIDA_peak_1, row=1, col=1)
    fig.add_trace(trace_a_star_peak_2, row=1, col=2)
    fig.add_trace(trace_LRTA_peak_2, row=1, col=2)
    fig.add_trace(trace_tt_IDA_peak_2, row=1, col=2)
    fig.add_trace(trace_IIDA_peak_2, row=1, col=2)
    fig.add_trace(trace_a_star_peak_3, row=1, col=3)
    fig.add_trace(trace_LRTA_peak_3, row=1, col=3)
    fig.add_trace(trace_tt_IDA_peak_3, row=1, col=3)
    fig.add_trace(trace_IIDA_peak_3, row=1, col=3)
    fig.add_trace(trace_a_star_peak_4, row=1, col=4)
    fig.add_trace(trace_LRTA_peak_4, row=1, col=4)
    fig.add_trace(trace_tt_IDA_peak_4, row=1, col=4)
    fig.add_trace(trace_IIDA_peak_4, row=1, col=4)
    fig.add_trace(trace_a_star_peak_5, row=1, col=5)
    fig.add_trace(trace_LRTA_peak_5, row=1, col=5)
    fig.add_trace(trace_tt_IDA_peak_5, row=1, col=5)
    fig.add_trace(trace_IIDA_peak_5, row=1, col=5)

    fig.update_layout(height=600, width=2000, font=dict(family="Arial", size=15, color="black"))
    fig.update_layout(barmode='group')
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=1)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=2)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=3)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=4)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=5)
    fig.update_yaxes(title_text='log_2(Memory (bytes))', row=1, col=1)
    fig.update_yaxes(title_text='Memory (bytes)', row=1, col=2)
    fig.update_yaxes(title_text='Memory (bytes)', row=1, col=3)
    fig.update_yaxes(title_text='Memory (bytes)', row=1, col=4)
    fig.update_yaxes(title_text='Memory (bytes)', row=1, col=5)
    fig.show()

    fig = make_subplots(rows=1, cols=5, subplot_titles=(
        'Traversed Edges (maze-128-128-2)',
        'Traversed Edges (maze-32-32-2)',
        'Traversed Edges (random-64-64-20)',
        'Traversed Edges (room-32-32-4)',
        'Traversed Edges (room-64-64-8)'))

    fig.add_trace(trace_a_star_edge_1, row=1, col=1)
    fig.add_trace(trace_LRTA_edge_1, row=1, col=1)
    fig.add_trace(trace_tt_IDA_edge_1, row=1, col=1)
    fig.add_trace(trace_IIDA_edge_1, row=1, col=1)
    fig.add_trace(trace_a_star_edge_2, row=1, col=2)
    fig.add_trace(trace_LRTA_edge_2, row=1, col=2)
    fig.add_trace(trace_tt_IDA_edge_2, row=1, col=2)
    fig.add_trace(trace_IIDA_edge_2, row=1, col=2)
    fig.add_trace(trace_a_star_edge_3, row=1, col=3)
    fig.add_trace(trace_LRTA_edge_3, row=1, col=3)
    fig.add_trace(trace_tt_IDA_edge_3, row=1, col=3)
    fig.add_trace(trace_IIDA_edge_3, row=1, col=3)
    fig.add_trace(trace_a_star_edge_4, row=1, col=4)
    fig.add_trace(trace_LRTA_edge_4, row=1, col=4)
    fig.add_trace(trace_tt_IDA_edge_4, row=1, col=4)
    fig.add_trace(trace_IIDA_edge_4, row=1, col=4)
    fig.add_trace(trace_a_star_edge_5, row=1, col=5)
    fig.add_trace(trace_LRTA_edge_5, row=1, col=5)
    fig.add_trace(trace_tt_IDA_edge_5, row=1, col=5)
    fig.add_trace(trace_IIDA_edge_5, row=1, col=5)

    fig.update_layout(height=600, width=2000, font=dict(family="Arial", size=15, color="black"))
    fig.update_layout(barmode='group')
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=1)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=2)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=3)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=4)
    fig.update_xaxes(title_text='Heuristic Function', row=1, col=5)
    fig.update_yaxes(title_text='log_2(Number of Edges)', row=1, col=1)
    fig.update_yaxes(title_text='log_2(Number of Edges)', row=1, col=2)
    fig.update_yaxes(title_text='log_2(Number of Edges)', row=1, col=3)
    fig.update_yaxes(title_text='log_2(Number of Edges)', row=1, col=4)
    fig.update_yaxes(title_text='log_2(Number of Edges)', row=1, col=5)
    fig.show()

    # a_star_current = data_result_random['A* current memory size (bytes)']
    # LRTA_current = data_result_random['LRTA current memory size']
    # tt_IDA_current = data_result_random['TT IDA current memory size']
    # IIDA_current = data_result_random['IIDA current memory size']
    #
    #
    # a_star_edge = data_result_random['A* traversed edges']
    # # a_star_edge = [math.log(x, 2) for x in a_star_edge]
    # LRTA_edge = data_result_random['LRTA traversed edges']
    # # LRTA_edge = [math.log(x, 2) for x in LRTA_edge]
    # tt_IDA_edge = data_result_random['TT IDA traversed edges']
    # # tt_IDA_edge = [math.log(x, 2) for x in tt_IDA_edge]
    # IIDA_edge = data_result_random['IIDA traversed edges']
    # # IIDA_edge = [math.log(x, 2) for x in IIDA_edge]

    # fig = go.Figure(data=[
    #     go.Bar(name='A*', x=map_name, y=a_star_time),
    #     go.Bar(name='LRTA*', x=map_name, y=LRTA_time),
    #     go.Bar(name='TT IDA*', x=map_name, y=tt_IDA_time),
    #     go.Bar(name='IIDA*', x=map_name, y=IIDA_time)
    # ])
    # Change the bar mode
