import math

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

if __name__ == '__main__':
    file_path = 'experiment result_random_M.xlsx'  # 替换成您的 Excel 文件路径
    data_result_random = pd.read_excel(file_path, 'Sheet1')
    # Add data

    layout = {'legend': {'x': 0.5, 'y': -0.1, 'orientation': 'h'}}

    map_size = data_result_random['Map Size']
    a_star_time = data_result_random['A* time (s)']
    # a_star_time = [math.log(x, 2) for x in a_star_time]
    LRTA_time = data_result_random['LRTA time (s)']
    # LRTA_time = [math.log(x, 2) for x in LRTA_time]
    tt_IDA_time = data_result_random['TT IDA time (s)']
    # tt_IDA_time = [math.log(x, 2) for x in tt_IDA_time]
    IIDA_time = data_result_random['IIDA time (s)']
    # IIDA_time = [math.log(x, 2) for x in IIDA_time]

    # a_star_current = data_result_random['A* current memory size (bytes)']
    # LRTA_current = data_result_random['LRTA current memory size']
    # tt_IDA_current = data_result_random['TT IDA current memory size']
    # IIDA_current = data_result_random['IIDA current memory size']

    a_star_peak = data_result_random['A* peak memory size']
    LRTA_peak = data_result_random['LRTA peak memory size']
    tt_IDA_peak = data_result_random['TT IDA peak memory size']
    IIDA_peak = data_result_random['IIDA peak memory size']

    # a_star_edge = data_result_random['A* traversed edges']
    # # a_star_edge = [math.log(x, 2) for x in a_star_edge]
    # LRTA_edge = data_result_random['LRTA traversed edges']
    # # LRTA_edge = [math.log(x, 2) for x in LRTA_edge]
    # tt_IDA_edge = data_result_random['TT IDA traversed edges']
    # # tt_IDA_edge = [math.log(x, 2) for x in tt_IDA_edge]
    # IIDA_edge = data_result_random['IIDA traversed edges']
    # # IIDA_edge = [math.log(x, 2) for x in IIDA_edge]
    #
    # a_star_expended = data_result_random[' A* expended nodes']
    # IIDA_expended = data_result_random[' IIDA expended nodes']
    # a_star_generated = data_result_random[' A* generated nodes']
    # IIDA_generated = data_result_random[' IIDA generated nodes']

    # dash options include 'dash', 'dot', and 'dashdot'
    trace_a_star_time = go.Scatter(x=map_size, y=a_star_time, name='A*', line=dict(color='firebrick', width=2))
    trace_LRTA_time = go.Scatter(x=map_size, y=LRTA_time, name='LRTA*', line=dict(color='royalblue', width=2))
    trace_tt_IDA_time = go.Scatter(x=map_size, y=tt_IDA_time, name='TT IDA*', line=dict(color='#f207e7', width=2))
    trace_IIDA_time = go.Scatter(x=map_size, y=IIDA_time, name='IIDA*', line=dict(color='#08bd0e', width=2))

    # trace_a_star_current = go.Scatter(x=map_size, y=a_star_current, name='A*', line=dict(color='firebrick', width=2))
    # trace_LRTA_current = go.Scatter(x=map_size, y=LRTA_current, name='LRTA*', line=dict(color='royalblue', width=2))
    # trace_tt_IDA_current = go.Scatter(x=map_size, y=tt_IDA_current, name='TT IDA*', line=dict(color='#f207e7', width=2))
    # trace_IIDA_current = go.Scatter(x=map_size, y=IIDA_current, name='IIDA*', line=dict(color='#08bd0e', width=2))

    trace_a_star_peak = go.Scatter(x=map_size, y=a_star_peak, name='A*', line=dict(color='firebrick', width=2))
    trace_LRTA_peak = go.Scatter(x=map_size, y=LRTA_peak, name='LRTA*', line=dict(color='royalblue', width=2))
    trace_tt_IDA_peak = go.Scatter(x=map_size, y=tt_IDA_peak, name='TT IDA*', line=dict(color='#f207e7', width=2))
    trace_IIDA_peak = go.Scatter(x=map_size, y=IIDA_peak, name='IIDA*', line=dict(color='#08bd0e', width=2))

    # trace_a_star_edge = go.Scatter(x=map_size, y=a_star_edge, name='A*', line=dict(color='firebrick', width=2))
    # trace_LRTA_edge = go.Scatter(x=map_size, y=LRTA_edge, name='LRTA*', line=dict(color='royalblue', width=2))
    # trace_tt_IDA_edge = go.Scatter(x=map_size, y=tt_IDA_edge, name='TT IDA*', line=dict(color='#f207e7', width=2))
    # trace_IIDA_edge = go.Scatter(x=map_size, y=IIDA_edge, name='IIDA*', line=dict(color='#08bd0e', width=2))
    #
    # trace_a_star_expended = go.Scatter(x=map_size, y=a_star_expended, name='A*', line=dict(color='firebrick', width=2))
    # trace_IIDA_expended = go.Scatter(x=map_size, y=IIDA_expended, name='IIDA*', line=dict(color='#08bd0e', width=2))
    # trace_a_star_generated = go.Scatter(x=map_size, y=a_star_generated, name='A*', line=dict(color='firebrick', width=2))
    # trace_IIDA_generated = go.Scatter(x=map_size, y=IIDA_generated, name='IIDA*', line=dict(color='#08bd0e', width=2))

    # data_result_random = pd.read_excel(file_path, 'Sheet2')
    # # Add data
    # Obstacle_rate = data_result_random['Obstacle Rate']
    # a_star_time = data_result_random['A* time (s)']
    # # a_star_time = [math.log(x, 2) for x in a_star_time]
    # LRTA_time = data_result_random['LRTA time (s)']
    # # LRTA_time = [math.log(x, 2) for x in LRTA_time]
    # tt_IDA_time = data_result_random['TT IDA time (s)']
    # # tt_IDA_time = [math.log(x, 2) for x in tt_IDA_time]
    # IIDA_time = data_result_random['IIDA time (s)']
    # # IIDA_time = [math.log(x, 2) for x in IIDA_time]
    #
    # a_star_current = data_result_random['A* current memory size (bytes)']
    # LRTA_current = data_result_random['LRTA current memory size']
    # tt_IDA_current = data_result_random['TT IDA current memory size']
    # IIDA_current = data_result_random['IIDA current memory size']
    #
    # a_star_peak = data_result_random['A* peak memory size']
    # LRTA_peak = data_result_random['LRTA peak memory size']
    # tt_IDA_peak = data_result_random['TT IDA peak memory size']
    # IIDA_peak = data_result_random['IIDA peak memory size']
    #
    # a_star_edge = data_result_random['A* traversed edges']
    # # a_star_edge = [math.log(x, 2) for x in a_star_edge]
    # LRTA_edge = data_result_random['LRTA traversed edges']
    # # LRTA_edge = [math.log(x, 2) for x in LRTA_edge]
    # tt_IDA_edge = data_result_random['TT IDA traversed edges']
    # # tt_IDA_edge = [math.log(x, 2) for x in tt_IDA_edge]
    # IIDA_edge = data_result_random['IIDA traversed edges']
    # # IIDA_edge = [math.log(x, 2) for x in IIDA_edge]
    #
    # a_star_expended_2 = data_result_random[' A* expended nodes']
    # IIDA_expended_2 = data_result_random[' IIDA expended nodes']
    # a_star_generated_2 = data_result_random[' A* generated nodes']
    # IIDA_generated_2 = data_result_random['IIDA generated nodes']

    # dash options include 'dash', 'dot', and 'dashdot'
    # trace_a_star_time_2 = go.Scatter(x=Obstacle_rate, y=a_star_time, name='A*', line=dict(color='firebrick', width=2))
    # trace_LRTA_time_2 = go.Scatter(x=Obstacle_rate, y=LRTA_time, name='LRTA*', line=dict(color='royalblue', width=2))
    # trace_tt_IDA_time_2 = go.Scatter(x=Obstacle_rate, y=tt_IDA_time, name='TT IDA*',
    #                                  line=dict(color='#f207e7', width=2))
    # trace_IIDA_time_2 = go.Scatter(x=Obstacle_rate, y=IIDA_time, name='IIDA*', line=dict(color='#08bd0e', width=2))
    #
    # trace_a_star_current_2 = go.Scatter(x=Obstacle_rate, y=a_star_current, name='A*',
    #                                     line=dict(color='firebrick', width=2))
    # trace_LRTA_current_2 = go.Scatter(x=Obstacle_rate, y=LRTA_current, name='LRTA*',
    #                                   line=dict(color='royalblue', width=2))
    # trace_tt_IDA_current_2 = go.Scatter(x=Obstacle_rate, y=tt_IDA_current, name='TT IDA*',
    #                                     line=dict(color='#f207e7', width=2))
    # trace_IIDA_current_2 = go.Scatter(x=Obstacle_rate, y=IIDA_current, name='IIDA*',
    #                                   line=dict(color='#08bd0e', width=2))
    #
    # trace_a_star_peak_2 = go.Scatter(x=Obstacle_rate, y=a_star_peak, name='A*', line=dict(color='firebrick', width=2))
    # trace_LRTA_peak_2 = go.Scatter(x=Obstacle_rate, y=LRTA_peak, name='LRTA*', line=dict(color='royalblue', width=2))
    # trace_tt_IDA_peak_2 = go.Scatter(x=Obstacle_rate, y=tt_IDA_peak, name='TT IDA*',
    #                                  line=dict(color='#f207e7', width=2))
    # trace_IIDA_peak_2 = go.Scatter(x=Obstacle_rate, y=IIDA_peak, name='IIDA*', line=dict(color='#08bd0e', width=2))
    #
    # trace_a_star_edge_2 = go.Scatter(x=Obstacle_rate, y=a_star_edge, name='A*', line=dict(color='firebrick', width=2))
    # trace_LRTA_edge_2 = go.Scatter(x=Obstacle_rate, y=LRTA_edge, name='LRTA*', line=dict(color='royalblue', width=2))
    # trace_tt_IDA_edge_2 = go.Scatter(x=Obstacle_rate, y=tt_IDA_edge, name='TT IDA*',
    #                                  line=dict(color='#f207e7', width=2))
    # trace_IIDA_edge_2 = go.Scatter(x=Obstacle_rate, y=IIDA_edge, name='IIDA*', line=dict(color='#08bd0e', width=2))
    #
    # trace_a_star_expended_2 = go.Scatter(x=Obstacle_rate, y=a_star_expended_2, name='A*', line=dict(color='firebrick', width=2))
    # trace_IIDA_expended_2 = go.Scatter(x=Obstacle_rate, y=IIDA_expended_2, name='IIDA*', line=dict(color='#08bd0e', width=2))
    # trace_a_star_generated_2 = go.Scatter(x=Obstacle_rate, y=a_star_generated_2, name='A*', line=dict(color='firebrick', width=2))
    # trace_IIDA_generated_2 = go.Scatter(x=Obstacle_rate, y=IIDA_generated_2, name='IIDA*', line=dict(color='#08bd0e', width=2))

    fig = make_subplots(rows=1, cols=2, subplot_titles=('CPU Running Time', 'CPU Running Time'))

    fig.add_trace(trace_a_star_time, row=1, col=1)
    fig.add_trace(trace_IIDA_time, row=1, col=1)
    fig.add_trace(trace_LRTA_time, row=1, col=2)
    fig.add_trace(trace_tt_IDA_time, row=1, col=2)
    fig.update_layout(height=300, width=600, font=dict(family="Arial", size=15, color="black"), legend=dict(x=0, y=-0.5, orientation='h'))
    fig.update_xaxes(title_text='Map Size (n x n)', row=1, col=1)
    fig.update_xaxes(title_text='Map Size (n x n)', row=1, col=2)
    fig.update_yaxes(title_text='Time (s)', row=1, col=1)
    # fig.update_yaxes(title_text='Time (s)', row=1, col=2)

    fig.show()

    fig = make_subplots(rows=1, cols=2, subplot_titles=('Peak Memory Usage', 'Peak Memory Usage'))

    # fig.add_trace(trace_a_star_current, row=1, col=1)
    # fig.add_trace(trace_LRTA_current, row=1, col=1)
    # fig.add_trace(trace_tt_IDA_current, row=1, col=1)
    # fig.add_trace(trace_IIDA_current, row=1, col=1)
    fig.add_trace(trace_a_star_peak, row=1, col=1)
    fig.add_trace(trace_LRTA_peak, row=1, col=2)
    fig.add_trace(trace_tt_IDA_peak, row=1, col=1)
    fig.add_trace(trace_IIDA_peak, row=1, col=1)

    fig.update_layout(height=300, width=600, font=dict(family="Arial", size=15, color="black"), legend=dict(x=0, y=-0.5, orientation='h'))
    fig.update_xaxes(title_text='Map Size (n x n)', row=1, col=1)
    fig.update_yaxes(title_text='Memory Usage (bytes)', row=1, col=1)
    fig.update_xaxes(title_text='Map Size (n x n)', row=1, col=2)
    # fig.update_yaxes(title_text='Memory Usage (bytes)', row=1, col=2)

    fig.show()

    # fig = make_subplots(rows=1, cols=2,
    #                     subplot_titles=('Traversed nodes', 'Traversed nodes'))
    #
    # fig.add_trace(trace_a_star_edge, row=1, col=1)
    # fig.add_trace(trace_IIDA_edge, row=1, col=1)
    # fig.add_trace(trace_LRTA_edge, row=1, col=2)
    # fig.add_trace(trace_tt_IDA_edge, row=1, col=2)
    #
    # fig.update_layout(height=300, width=600, font=dict(family="Arial", size=15, color="black"), legend=dict(x=0, y=-0.5, orientation='h'))
    # fig.update_xaxes(title_text='Map Size (n x n)', row=1, col=1)
    # fig.update_xaxes(title_text='Map Size (n x n)', row=1, col=2)
    # fig.update_yaxes(title_text='Node number', row=1, col=1)
    # # fig.update_yaxes(title_text='Node number', row=1, col=2)
    #
    # fig.show()

    # fig = make_subplots(rows=1, cols=2, subplot_titles=('CPU Running Time', 'CPU Running Time'))
    #
    # fig.add_trace(trace_a_star_time_2, row=1, col=1)
    # fig.add_trace(trace_IIDA_time_2, row=1, col=1)
    # fig.add_trace(trace_LRTA_time_2, row=1, col=2)
    # fig.add_trace(trace_tt_IDA_time_2, row=1, col=2)
    #
    # fig.update_layout(height=300, width=600, font=dict(family="Arial", size=15, color="black"), legend=dict(x=0, y=-0.5, orientation='h'))
    # fig.update_xaxes(title_text='Obstacle Rate (%)', row=1, col=1)
    # fig.update_xaxes(title_text='Obstacle Rate (%)', row=1, col=2)
    # fig.update_yaxes(title_text='Time (s)', row=1, col=1)
    # # fig.update_yaxes(title_text='Time (s)', row=1, col=2)
    #
    # fig.show()
    #
    # fig = go.Figure()
    #
    # # fig.add_trace(trace_a_star_current_2, row=1, col=1)
    # # fig.add_trace(trace_LRTA_current_2, row=1, col=1)
    # # fig.add_trace(trace_tt_IDA_current_2, row=1, col=1)
    # # fig.add_trace(trace_IIDA_current_2, row=1, col=1)
    # fig.add_trace(trace_a_star_peak_2)
    # fig.add_trace(trace_LRTA_peak_2)
    # fig.add_trace(trace_tt_IDA_peak_2)
    # fig.add_trace(trace_IIDA_peak_2)
    #
    # fig.update_layout(height=300, width=500, font=dict(family="Arial", size=12, color="black"),
    #                   title='Peak Memory Usage',
    #                   xaxis=dict(title='Obstacle Rate (%)'),
    #                   yaxis=dict(title='Memory Usage (bytes)'))
    #
    # fig.show()
    #
    # fig = make_subplots(rows=1, cols=2,
    #                     subplot_titles=('Traversed nodes', 'Traversed nodes'))
    #
    # fig.add_trace(trace_a_star_edge_2, row=1, col=1)
    # fig.add_trace(trace_IIDA_edge_2, row=1, col=1)
    # fig.add_trace(trace_LRTA_edge_2, row=1, col=2)
    # fig.add_trace(trace_tt_IDA_edge_2, row=1, col=2)
    #
    # fig.update_layout(height=300, width=600, font=dict(family="Arial", size=15, color="black"), legend=dict(x=0, y=-0.5, orientation='h'))
    # fig.update_xaxes(title_text='Obstacle Rate (%)', row=1, col=1)
    # fig.update_xaxes(title_text='Obstacle Rate (%)', row=1, col=2)
    # fig.update_yaxes(title_text='Node number', row=1, col=1)
    # # fig.update_yaxes(title_text='Node number', row=1, col=2)
    #
    # fig.show()
    #
    # fig = make_subplots(rows=1, cols=2, subplot_titles=('Expended Nodes', 'Generated Nodes'))
    #
    # fig.add_trace(trace_a_star_expended, row=1, col=1)
    # fig.add_trace(trace_IIDA_expended, row=1, col=1)
    # fig.add_trace(trace_a_star_generated, row=1, col=2)
    # fig.add_trace(trace_IIDA_generated, row=1, col=2)
    #
    # fig.update_layout(height=300, width=600, font=dict(family="Arial", size=15, color="black"),
    #                   legend=dict(x=0, y=-0.5, orientation='h'))
    # fig.update_xaxes(title_text='Map Size (n x n)', row=1, col=1)
    # fig.update_xaxes(title_text='Map Size (n x n)', row=1, col=2)
    # fig.update_yaxes(title_text='Node number', row=1, col=1)
    # # fig.update_yaxes(title_text='Node number', row=1, col=2)
    #
    # fig.show()
    #
    # fig = make_subplots(rows=1, cols=2, subplot_titles=('Expended Nodes', 'Generated Nodes'))
    #
    # fig.add_trace(trace_a_star_expended_2, row=1, col=1)
    # fig.add_trace(trace_IIDA_expended_2, row=1, col=1)
    # fig.add_trace(trace_a_star_generated_2, row=1, col=2)
    # fig.add_trace(trace_IIDA_generated_2, row=1, col=2)
    #
    # fig.update_layout(height=300, width=600, font=dict(family="Arial", size=15, color="black"),
    #                   legend=dict(x=0, y=-0.5, orientation='h'))
    # fig.update_xaxes(title_text='Obstacle Rate (%)', row=1, col=1)
    # fig.update_xaxes(title_text='Obstacle Rate (%)', row=1, col=2)
    # fig.update_yaxes(title_text='Node number', row=1, col=1)
    #
    # fig.show()
