import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import math

if __name__ == '__main__':
    file_path = 'maze-32-32-2_D.csv'  # 替换成您的 Excel 文件路径

    data_result_random = pd.read_csv('maze-32-32-2_D.csv')
    # Add data
    a_star_time_D_1 = data_result_random[' A* time (s)']
    # a_star_time_2 = [math.log(x, 2) for x in a_star_time_2]
    IIDA_time_D_1 = data_result_random[' IIDA time (s)']
    # IIDA_time_2 = [math.log(x, 2) for x in IIDA_time_2]
    LRTA_time_D_1 = data_result_random[' LRTA time (s)']
    # LRTA_time_2 = [math.log(x, 2) for x in LRTA_time_2]
    tt_IDA_time_D_1 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_2 = [math.log(x, 2) for x in tt_IDA_time_2]
    a_star_peak_D_1 = data_result_random[' A* peak memory used']
    LRTA_peak_D_1 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_D_1 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_D_1 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('maze-32-32-2_E.csv')
    # Add data
    a_star_time_E_1 = data_result_random[' A* time (s)']
    # a_star_time_3 = [math.log(x, 2) for x in a_star_time_3]
    IIDA_time_E_1 = data_result_random[' IIDA time (s)']
    # IIDA_time_3 = [math.log(x, 2) for x in IIDA_time_3]
    LRTA_time_E_1 = data_result_random[' LRTA time (s)']
    # LRTA_time_3 = [math.log(x, 2) for x in LRTA_time_3]
    tt_IDA_time_E_1 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_3 = [math.log(x, 2) for x in tt_IDA_time_3]
    a_star_peak_E_1 = data_result_random[' A* peak memory used']
    LRTA_peak_E_1 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_E_1 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_E_1 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('maze-32-32-2_M.csv')
    # Add data
    a_star_time_M_1 = data_result_random[' A* time (s)']
    # a_star_time_4 = [math.log(x, 2) for x in a_star_time_4]
    IIDA_time_M_1 = data_result_random[' IIDA time (s)']
    # IIDA_time_4 = [math.log(x, 2) for x in IIDA_time_4]
    LRTA_time_M_1 = data_result_random[' LRTA time (s)']
    # LRTA_time_4 = [math.log(x, 2) for x in LRTA_time_4]
    tt_IDA_time_M_1 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_4 = [math.log(x, 2) for x in tt_IDA_time_4]
    a_star_peak_M_1 = data_result_random[' A* peak memory used']
    LRTA_peak_M_1 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_M_1 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_M_1 = data_result_random[' IIDA peak memory used']

    # data_result_random = pd.read_csv('maze-32-32-2_O.csv')
    # # Add data
    # a_star_time_O_1 = data_result_random[' A* time (s)']
    # # a_star_time_5 = [math.log(x, 2) for x in a_star_time_5]
    # IIDA_time_O_1 = data_result_random[' IIDA time (s)']
    # # IIDA_time_5 = [math.log(x, 2) for x in IIDA_time_5]
    # LRTA_time_O_1 = data_result_random[' LRTA time (s)']
    # # LRTA_time += [math.log(x, 2) for x in LRTA_time_5]
    # tt_IDA_time_O_1 = data_result_random[' TT IDA time (s)']
    # # tt_IDA_time_5 = [math.log(x, 2) for x in tt_IDA_time_5]
    # a_star_peak_O_1 = data_result_random[' A* peak memory used']
    # LRTA_peak_O_1 = data_result_random[' LRTA peak memory used']
    # tt_IDA_peak_O_1 = data_result_random[' TT IDA peak memory used']
    # IIDA_peak_O_1 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('random-64-64-20_D.csv')
    # Add data
    a_star_time_D_2 = data_result_random[' A* time (s)']
    # a_star_time_2 = [math.log(x, 2) for x in a_star_time_2]
    IIDA_time_D_2 = data_result_random[' IIDA time (s)']
    # IIDA_time_2 = [math.log(x, 2) for x in IIDA_time_2]
    LRTA_time_D_2 = data_result_random[' LRTA time (s)']
    # LRTA_time_2 = [math.log(x, 2) for x in LRTA_time_2]
    tt_IDA_time_D_2 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_2 = [math.log(x, 2) for x in tt_IDA_time_2]
    a_star_peak_D_2 = data_result_random[' A* peak memory used']
    LRTA_peak_D_2 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_D_2 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_D_2 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('random-64-64-20_E.csv')
    # Add data
    a_star_time_E_2 = data_result_random[' A* time (s)']
    # a_star_time_3 = [math.log(x, 2) for x in a_star_time_3]
    IIDA_time_E_2 = data_result_random[' IIDA time (s)']
    # IIDA_time_3 = [math.log(x, 2) for x in IIDA_time_3]
    LRTA_time_E_2 = data_result_random[' LRTA time (s)']
    # LRTA_time_3 = [math.log(x, 2) for x in LRTA_time_3]
    tt_IDA_time_E_2 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_3 = [math.log(x, 2) for x in tt_IDA_time_3]
    a_star_peak_E_2 = data_result_random[' A* peak memory used']
    LRTA_peak_E_2 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_E_2 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_E_2 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('random-64-64-20_M.csv')
    # Add data
    a_star_time_M_2 = data_result_random[' A* time (s)']
    # a_star_time_4 = [math.log(x, 2) for x in a_star_time_4]
    IIDA_time_M_2 = data_result_random[' IIDA time (s)']
    # IIDA_time_4 = [math.log(x, 2) for x in IIDA_time_4]
    LRTA_time_M_2 = data_result_random[' LRTA time (s)']
    # LRTA_time_4 = [math.log(x, 2) for x in LRTA_time_4]
    tt_IDA_time_M_2 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_4 = [math.log(x, 2) for x in tt_IDA_time_4]
    a_star_peak_M_2 = data_result_random[' A* peak memory used']
    LRTA_peak_M_2 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_M_2 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_M_2 = data_result_random[' IIDA peak memory used']

    # data_result_random = pd.read_csv('random-64-64-20_O.csv')
    # # Add data
    # a_star_time_O_2 = data_result_random[' A* time (s)']
    # # a_star_time_5 = [math.log(x, 2) for x in a_star_time_5]
    # IIDA_time_O_2 = data_result_random[' IIDA time (s)']
    # # IIDA_time_5 = [math.log(x, 2) for x in IIDA_time_5]
    # LRTA_time_O_2 = data_result_random[' LRTA time (s)']
    # # LRTA_time += [math.log(x, 2) for x in LRTA_time_5]
    # tt_IDA_time_O_2 = data_result_random[' TT IDA time (s)']
    # # tt_IDA_time_5 = [math.log(x, 2) for x in tt_IDA_time_5]
    # a_star_peak_O_2 = data_result_random[' A* peak memory used']
    # LRTA_peak_O_2 = data_result_random[' LRTA peak memory used']
    # tt_IDA_peak_O_2 = data_result_random[' TT IDA peak memory used']
    # IIDA_peak_O_2 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('room-32-32-4_D.csv')
    # Add data
    a_star_time_D_3 = data_result_random[' A* time (s)']
    # a_star_time_2 = [math.log(x, 2) for x in a_star_time_2]
    IIDA_time_D_3 = data_result_random[' IIDA time (s)']
    # IIDA_time_2 = [math.log(x, 2) for x in IIDA_time_2]
    LRTA_time_D_3 = data_result_random[' LRTA time (s)']
    # LRTA_time_2 = [math.log(x, 2) for x in LRTA_time_2]
    tt_IDA_time_D_3 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_2 = [math.log(x, 2) for x in tt_IDA_time_2]
    a_star_peak_D_3 = data_result_random[' A* peak memory used']
    LRTA_peak_D_3 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_D_3 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_D_3 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('room-32-32-4_E.csv')
    # Add data
    a_star_time_E_3 = data_result_random[' A* time (s)']
    # a_star_time_3 = [math.log(x, 2) for x in a_star_time_3]
    IIDA_time_E_3 = data_result_random[' IIDA time (s)']
    # IIDA_time_3 = [math.log(x, 2) for x in IIDA_time_3]
    LRTA_time_E_3 = data_result_random[' LRTA time (s)']
    # LRTA_time_3 = [math.log(x, 2) for x in LRTA_time_3]
    tt_IDA_time_E_3 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_3 = [math.log(x, 2) for x in tt_IDA_time_3]
    a_star_peak_E_3 = data_result_random[' A* peak memory used']
    LRTA_peak_E_3 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_E_3 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_E_3 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('room-32-32-4_M.csv')
    # Add data
    a_star_time_M_3 = data_result_random[' A* time (s)']
    # a_star_time_4 = [math.log(x, 2) for x in a_star_time_4]
    IIDA_time_M_3 = data_result_random[' IIDA time (s)']
    # IIDA_time_4 = [math.log(x, 2) for x in IIDA_time_4]
    LRTA_time_M_3 = data_result_random[' LRTA time (s)']
    # LRTA_time_4 = [math.log(x, 2) for x in LRTA_time_4]
    tt_IDA_time_M_3 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_4 = [math.log(x, 2) for x in tt_IDA_time_4]
    a_star_peak_M_3 = data_result_random[' A* peak memory used']
    LRTA_peak_M_3 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_M_3 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_M_3 = data_result_random[' IIDA peak memory used']

    # data_result_random = pd.read_csv('room-32-32-4_O.csv')
    # # Add data
    # a_star_time_O_3 = data_result_random[' A* time (s)']
    # # a_star_time_5 = [math.log(x, 2) for x in a_star_time_5]
    # IIDA_time_O_3 = data_result_random[' IIDA time (s)']
    # # IIDA_time_5 = [math.log(x, 2) for x in IIDA_time_5]
    # LRTA_time_O_3 = data_result_random[' LRTA time (s)']
    # # LRTA_time += [math.log(x, 2) for x in LRTA_time_5]
    # tt_IDA_time_O_3 = data_result_random[' TT IDA time (s)']
    # # tt_IDA_time_5 = [math.log(x, 2) for x in tt_IDA_time_5]
    # a_star_peak_O_3 = data_result_random[' A* peak memory used']
    # LRTA_peak_O_3 = data_result_random[' LRTA peak memory used']
    # tt_IDA_peak_O_3 = data_result_random[' TT IDA peak memory used']
    # IIDA_peak_O_3 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('room-64-64-8_D.csv')
    # Add data
    a_star_time_D_4 = data_result_random[' A* time (s)']
    # a_star_time_2 = [math.log(x, 2) for x in a_star_time_2]
    IIDA_time_D_4 = data_result_random[' IIDA time (s)']
    # IIDA_time_2 = [math.log(x, 2) for x in IIDA_time_2]
    LRTA_time_D_4 = data_result_random[' LRTA time (s)']
    # LRTA_time_2 = [math.log(x, 2) for x in LRTA_time_2]
    tt_IDA_time_D_4 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_2 = [math.log(x, 2) for x in tt_IDA_time_2]
    a_star_peak_D_4 = data_result_random[' A* peak memory used']
    LRTA_peak_D_4 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_D_4 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_D_4 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('room-64-64-8_E.csv')
    # Add data
    a_star_time_E_4 = data_result_random[' A* time (s)']
    # a_star_time_3 = [math.log(x, 2) for x in a_star_time_3]
    IIDA_time_E_4 = data_result_random[' IIDA time (s)']
    # IIDA_time_3 = [math.log(x, 2) for x in IIDA_time_3]
    LRTA_time_E_4 = data_result_random[' LRTA time (s)']
    # LRTA_time_3 = [math.log(x, 2) for x in LRTA_time_3]
    tt_IDA_time_E_4 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_3 = [math.log(x, 2) for x in tt_IDA_time_3]
    a_star_peak_E_4 = data_result_random[' A* peak memory used']
    LRTA_peak_E_4 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_E_4 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_E_4 = data_result_random[' IIDA peak memory used']

    data_result_random = pd.read_csv('room-64-64-8_M.csv')
    # Add data
    a_star_time_M_4 = data_result_random[' A* time (s)']
    # a_star_time_4 = [math.log(x, 2) for x in a_star_time_4]
    IIDA_time_M_4 = data_result_random[' IIDA time (s)']
    # IIDA_time_4 = [math.log(x, 2) for x in IIDA_time_4]
    LRTA_time_M_4 = data_result_random[' LRTA time (s)']
    # LRTA_time_4 = [math.log(x, 2) for x in LRTA_time_4]
    tt_IDA_time_M_4 = data_result_random[' TT IDA time (s)']
    # tt_IDA_time_4 = [math.log(x, 2) for x in tt_IDA_time_4]
    a_star_peak_M_4 = data_result_random[' A* peak memory used']
    LRTA_peak_M_4 = data_result_random[' LRTA peak memory used']
    tt_IDA_peak_M_4 = data_result_random[' TT IDA peak memory used']
    IIDA_peak_M_4 = data_result_random[' IIDA peak memory used']

    # data_result_random = pd.read_csv('room-64-64-8_O.csv')
    # # Add data
    # a_star_time_O_4 = data_result_random[' A* time (s)']
    # # a_star_time_5 = [math.log(x, 2) for x in a_star_time_5]
    # IIDA_time_O_4 = data_result_random[' IIDA time (s)']
    # # IIDA_time_5 = [math.log(x, 2) for x in IIDA_time_5]
    # LRTA_time_O_4 = data_result_random[' LRTA time (s)']
    # # LRTA_time += [math.log(x, 2) for x in LRTA_time_5]
    # tt_IDA_time_O_4 = data_result_random[' TT IDA time (s)']
    # # tt_IDA_time_5 = [math.log(x, 2) for x in tt_IDA_time_5]
    # a_star_peak_O_4 = data_result_random[' A* peak memory used']
    # LRTA_peak_O_4 = data_result_random[' LRTA peak memory used']
    # tt_IDA_peak_O_4 = data_result_random[' TT IDA peak memory used']
    # IIDA_peak_O_4 = data_result_random[' IIDA peak memory used']

    # a_star_data_1 = {'x_values': a_star_time, 'y_values': a_star_peak}
    # LRTA_data_1 = {'x_values': LRTA_time, 'y_values': LRTA_peak}
    # TTIDA_data_1 = {'x_values': tt_IDA_time, 'y_values': tt_IDA_peak}
    # IIDA_data_1 = {'x_values': IIDA_time, 'y_values': IIDA_peak}
    o = 0.5
    s = 8
    trace_a_star_D_1 = go.Scatter(x=a_star_time_D_1, y=a_star_peak_D_1, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_D_1 = go.Scatter(x=LRTA_time_D_1, y=LRTA_peak_D_1, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_D_1 = go.Scatter(x=tt_IDA_time_D_1, y=tt_IDA_peak_D_1, mode='markers', name='TTIDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_D_1 = go.Scatter(x=IIDA_time_D_1, y=IIDA_peak_D_1, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_D_2 = go.Scatter(x=a_star_time_D_2, y=a_star_peak_D_2, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_D_2 = go.Scatter(x=LRTA_time_D_2, y=LRTA_peak_D_2, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_D_2 = go.Scatter(x=tt_IDA_time_D_2, y=tt_IDA_peak_D_2, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_D_2 = go.Scatter(x=IIDA_time_D_2, y=IIDA_peak_D_2, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_D_3 = go.Scatter(x=a_star_time_D_3, y=a_star_peak_D_3, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_D_3 = go.Scatter(x=LRTA_time_D_3, y=LRTA_peak_D_3, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_D_3 = go.Scatter(x=tt_IDA_time_D_3, y=tt_IDA_peak_D_3, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_D_3 = go.Scatter(x=IIDA_time_D_3, y=IIDA_peak_D_3, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_D_4 = go.Scatter(x=a_star_time_D_4, y=a_star_peak_D_4, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_D_4 = go.Scatter(x=LRTA_time_D_4, y=LRTA_peak_D_4, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_D_4 = go.Scatter(x=tt_IDA_time_D_4, y=tt_IDA_peak_D_4, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_D_4 = go.Scatter(x=IIDA_time_D_4, y=IIDA_peak_D_4, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_M_1 = go.Scatter(x=a_star_time_M_1, y=a_star_peak_M_1, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_M_1 = go.Scatter(x=LRTA_time_M_1, y=LRTA_peak_M_1, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_M_1 = go.Scatter(x=tt_IDA_time_M_1, y=tt_IDA_peak_M_1, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_M_1 = go.Scatter(x=IIDA_time_M_1, y=IIDA_peak_M_1, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_M_2 = go.Scatter(x=a_star_time_M_2, y=a_star_peak_M_2, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_M_2 = go.Scatter(x=LRTA_time_M_2, y=LRTA_peak_M_2, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_M_2 = go.Scatter(x=tt_IDA_time_M_2, y=tt_IDA_peak_M_2, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_M_2 = go.Scatter(x=IIDA_time_M_2, y=IIDA_peak_M_2, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_M_3 = go.Scatter(x=a_star_time_M_3, y=a_star_peak_M_3, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_M_3 = go.Scatter(x=LRTA_time_M_3, y=LRTA_peak_M_3, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_M_3 = go.Scatter(x=tt_IDA_time_M_3, y=tt_IDA_peak_M_3, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_M_3 = go.Scatter(x=IIDA_time_M_3, y=IIDA_peak_M_3, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_M_4 = go.Scatter(x=a_star_time_M_4, y=a_star_peak_M_4, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_M_4 = go.Scatter(x=LRTA_time_M_4, y=LRTA_peak_M_4, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_M_4 = go.Scatter(x=tt_IDA_time_M_4, y=tt_IDA_peak_M_4, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_M_4 = go.Scatter(x=IIDA_time_M_4, y=IIDA_peak_M_4, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_E_1 = go.Scatter(x=a_star_time_E_1, y=a_star_peak_E_1, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_E_1 = go.Scatter(x=LRTA_time_E_1, y=LRTA_peak_E_1, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_E_1 = go.Scatter(x=tt_IDA_time_E_1, y=tt_IDA_peak_E_1, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_E_1 = go.Scatter(x=IIDA_time_E_1, y=IIDA_peak_E_1, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_E_2 = go.Scatter(x=a_star_time_E_2, y=a_star_peak_E_2, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_E_2 = go.Scatter(x=LRTA_time_E_2, y=LRTA_peak_E_2, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_E_2 = go.Scatter(x=tt_IDA_time_E_2, y=tt_IDA_peak_E_2, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_E_2 = go.Scatter(x=IIDA_time_E_2, y=IIDA_peak_E_2, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_E_3 = go.Scatter(x=a_star_time_E_3, y=a_star_peak_E_3, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_E_3 = go.Scatter(x=LRTA_time_E_3, y=LRTA_peak_E_3, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_E_3 = go.Scatter(x=tt_IDA_time_E_3, y=tt_IDA_peak_E_3, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_E_3 = go.Scatter(x=IIDA_time_E_3, y=IIDA_peak_E_3, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    trace_a_star_E_4 = go.Scatter(x=a_star_time_E_4, y=a_star_peak_E_4, mode='markers', name='A*', marker=dict(color='firebrick', opacity=o, size=s))
    trace_LRTA_E_4 = go.Scatter(x=LRTA_time_E_4, y=LRTA_peak_E_4, mode='markers', name='LRTA*', marker=dict(color='royalblue', opacity=o, size=s))
    trace_tt_IDA_E_4 = go.Scatter(x=tt_IDA_time_E_4, y=tt_IDA_peak_E_4, mode='markers', name='TT IDA*', marker=dict(color='#f207e7', opacity=o, size=s))
    trace_IIDA_E_4 = go.Scatter(x=IIDA_time_E_4, y=IIDA_peak_E_4, mode='markers', name='IIDA*', marker=dict(color='#08bd0e', opacity=o, size=s))

    # a_star_data_1 = {'x_values': a_star_time, 'y_values': a_star_peak}
    # LRTA_data_1 = {'x_values': LRTA_time, 'y_values': LRTA_peak}
    # TTIDA_data_1 = {'x_values': tt_IDA_time, 'y_values': tt_IDA_peak}
    # IIDA_data_1 = {'x_values': IIDA_time, 'y_values': IIDA_peak}

    fig = make_subplots(rows=3, cols=4, subplot_titles=('maze-32-32-2 with Dijkstra', 'random-64-64-20 with Dijkstra', 'room-32-32-4 with Dijkstra', 'room-64-64-8 with Dijkstra',
                                                        'maze-32-32-2 with Manhattan', 'random-64-64-20 with Manhattan', 'room-32-32-4 with Manhattan', 'room-64-64-8 with Manhattan',
                                                        'maze-32-32-2 with Euclidean', 'random-64-64-20 with Euclidean', 'room-32-32-4 with Euclidean', 'room-64-64-8 with Euclidean'), vertical_spacing=0.1)

    fig.add_trace(trace_a_star_D_1, row=1, col=1)
    fig.add_trace(trace_LRTA_D_1, row=1, col=1)
    fig.add_trace(trace_tt_IDA_D_1, row=1, col=1)
    fig.add_trace(trace_IIDA_D_1, row=1, col=1)

    fig.add_trace(trace_a_star_D_2, row=1, col=2)
    fig.add_trace(trace_LRTA_D_2, row=1, col=2)
    fig.add_trace(trace_tt_IDA_D_2, row=1, col=2)
    fig.add_trace(trace_IIDA_D_2, row=1, col=2)

    fig.add_trace(trace_a_star_D_3, row=1, col=3)
    fig.add_trace(trace_LRTA_D_3, row=1, col=3)
    fig.add_trace(trace_tt_IDA_D_3, row=1, col=3)
    fig.add_trace(trace_IIDA_D_3, row=1, col=3)

    fig.add_trace(trace_a_star_D_4, row=1, col=4)
    fig.add_trace(trace_LRTA_D_4, row=1, col=4)
    fig.add_trace(trace_tt_IDA_D_4, row=1, col=4)
    fig.add_trace(trace_IIDA_D_4, row=1, col=4)

    fig.add_trace(trace_a_star_M_1, row=2, col=1)
    fig.add_trace(trace_LRTA_M_1, row=2, col=1)
    fig.add_trace(trace_tt_IDA_M_1, row=2, col=1)
    fig.add_trace(trace_IIDA_M_1, row=2, col=1)

    fig.add_trace(trace_a_star_M_2, row=2, col=2)
    fig.add_trace(trace_LRTA_M_2, row=2, col=2)
    fig.add_trace(trace_tt_IDA_M_2, row=2, col=2)
    fig.add_trace(trace_IIDA_M_2, row=2, col=2)

    fig.add_trace(trace_a_star_M_3, row=2, col=3)
    fig.add_trace(trace_LRTA_M_3, row=2, col=3)
    fig.add_trace(trace_tt_IDA_M_3, row=2, col=3)
    fig.add_trace(trace_IIDA_M_3, row=2, col=3)

    fig.add_trace(trace_a_star_M_4, row=2, col=4)
    fig.add_trace(trace_LRTA_M_4, row=2, col=4)
    fig.add_trace(trace_tt_IDA_M_4, row=2, col=4)
    fig.add_trace(trace_IIDA_M_4, row=2, col=4)

    fig.add_trace(trace_a_star_E_1, row=3, col=1)
    fig.add_trace(trace_LRTA_E_1, row=3, col=1)
    fig.add_trace(trace_tt_IDA_E_1, row=3, col=1)
    fig.add_trace(trace_IIDA_E_1, row=3, col=1)

    fig.add_trace(trace_a_star_E_2, row=3, col=2)
    fig.add_trace(trace_LRTA_E_2, row=3, col=2)
    fig.add_trace(trace_tt_IDA_E_2, row=3, col=2)
    fig.add_trace(trace_IIDA_E_2, row=3, col=2)

    fig.add_trace(trace_a_star_E_3, row=3, col=3)
    fig.add_trace(trace_LRTA_E_3, row=3, col=3)
    fig.add_trace(trace_tt_IDA_E_3, row=3, col=3)
    fig.add_trace(trace_IIDA_E_3, row=3, col=3)

    fig.add_trace(trace_a_star_E_4, row=3, col=4)
    fig.add_trace(trace_LRTA_E_4, row=3, col=4)
    fig.add_trace(trace_tt_IDA_E_4, row=3, col=4)
    fig.add_trace(trace_IIDA_E_4, row=3, col=4)

    fig.update_layout(height=700, width=1400, legend=dict(x=0, y=-0.1, orientation='h'))
    fig.update_xaxes(title_text='Time (s)', row=3, col=1)
    fig.update_xaxes(title_text='Time (s)', row=3, col=2)
    fig.update_xaxes(title_text='Time (s)', row=3, col=3)
    fig.update_xaxes(title_text='Time (s)', row=3, col=4)
    fig.update_yaxes(title_text='Memory (bytes)', row=1, col=1)
    fig.update_yaxes(title_text='Memory (bytes)', row=2, col=1)
    fig.update_yaxes(title_text='Memory (bytes)', row=3, col=1)

    fig.show()

    # fig.add_trace(trace_a_star_time_1, row=1, col=1)
    # fig.add_trace(trace_LRTA_time_1, row=1, col=1)
    # fig.add_trace(trace_tt_IDA_time_1, row=1, col=1)
    # fig.add_trace(trace_IIDA_time_1, row=1, col=1)
    # fig.add_trace(trace_a_star_time_2, row=1, col=1)
    # fig.add_trace(trace_LRTA_time_2, row=1, col=1)
    # fig.add_trace(trace_tt_IDA_time_2, row=1, col=1)
    # fig.add_trace(trace_IIDA_time_2, row=1, col=1)
    # fig.add_trace(trace_a_star_time_3, row=1, col=2)
    # fig.add_trace(trace_LRTA_time_3, row=1, col=2)
    # fig.add_trace(trace_tt_IDA_time_3, row=1, col=2)
    # fig.add_trace(trace_IIDA_time_3, row=1, col=2)
    # fig.add_trace(trace_a_star_time_4, row=1, col=3)
    # fig.add_trace(trace_LRTA_time_4, row=1, col=3)
    # fig.add_trace(trace_tt_IDA_time_4, row=1, col=3)
    # fig.add_trace(trace_IIDA_time_4, row=1, col=3)
    # fig.add_trace(trace_a_star_time_5, row=1, col=4)
    # fig.add_trace(trace_LRTA_time_5, row=1, col=4)
    # fig.add_trace(trace_tt_IDA_time_5, row=1, col=4)
    # fig.add_trace(trace_IIDA_time_5, row=1, col=4)

    # fig.update_layout(height=600, width=2000, font=dict(family="Arial", size=15, color="black"))
    # fig.update_layout(barmode='group')
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=1)
    # # fig.update_xaxes(title_text='Heuristic Function', row=2, col=1)
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=2)
    # # fig.update_xaxes(title_text='Heuristic Function', row=2, col=2)
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=3)
    # # fig.update_xaxes(title_text='Heuristic Function', row=2, col=3)
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=4)
    # # fig.update_xaxes(title_text='Heuristic Function', row=2, col=4)
    # # fig.update_xaxes(title_text='Heuristic Function', row=1, col=5)
    # # fig.update_xaxes(title_text='Heuristic Function', row=2, col=5)
    # fig.update_yaxes(title_text='Time (s)', row=1, col=1)
    # # fig.update_yaxes(title_text='Time (s)', row=2, col=1)
    # fig.update_yaxes(title_text='Time (s)', row=1, col=2)
    # # fig.update_yaxes(title_text='Time (s)', row=2, col=2)
    # fig.update_yaxes(title_text='Time (s)', row=1, col=3)
    # # fig.update_yaxes(title_text='Time (s)', row=2, col=3)
    # fig.update_yaxes(title_text='Time (s)', row=1, col=4)
    # # fig.update_yaxes(title_text='Time (s)', row=2, col=4)
    # # fig.update_yaxes(title_text='Time (s)', row=1, col=5)
    # # fig.update_yaxes(title_text='Time (s)', row=2, col=5)
    # fig.show()
    #
    # fig = make_subplots(rows=1, cols=4, subplot_titles=(
    #     'Peak Memory Used (maze-32-32-2)',
    #     'Peak Memory Used (random-64-64-20)',
    #     'Peak Memory Used (room-32-32-4)',
    #     'Peak Memory Used (room-64-64-8)'))

    # fig.add_trace(trace_a_star_peak_1, row=1, col=1)
    # fig.add_trace(trace_LRTA_peak_1, row=1, col=1)
    # fig.add_trace(trace_tt_IDA_peak_1, row=1, col=1)
    # fig.add_trace(trace_IIDA_peak_1, row=1, col=1)
    # fig.add_trace(trace_a_star_peak_2, row=1, col=1)
    # fig.add_trace(trace_LRTA_peak_2, row=1, col=1)
    # fig.add_trace(trace_tt_IDA_peak_2, row=1, col=1)
    # fig.add_trace(trace_IIDA_peak_2, row=1, col=1)
    # fig.add_trace(trace_a_star_peak_3, row=1, col=2)
    # fig.add_trace(trace_LRTA_peak_3, row=1, col=2)
    # fig.add_trace(trace_tt_IDA_peak_3, row=1, col=2)
    # fig.add_trace(trace_IIDA_peak_3, row=1, col=2)
    # fig.add_trace(trace_a_star_peak_4, row=1, col=3)
    # fig.add_trace(trace_LRTA_peak_4, row=1, col=3)
    # fig.add_trace(trace_tt_IDA_peak_4, row=1, col=3)
    # fig.add_trace(trace_IIDA_peak_4, row=1, col=3)
    # fig.add_trace(trace_a_star_peak_5, row=1, col=4)
    # fig.add_trace(trace_LRTA_peak_5, row=1, col=4)
    # fig.add_trace(trace_tt_IDA_peak_5, row=1, col=4)
    # fig.add_trace(trace_IIDA_peak_5, row=1, col=4)

    # fig.update_layout(height=600, width=2000, font=dict(family="Arial", size=15, color="black"))
    # fig.update_layout(barmode='group')
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=1)
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=2)
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=3)
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=4)
    # # fig.update_xaxes(title_text='Heuristic Function', row=1, col=5)
    # fig.update_yaxes(title_text='log_2(Memory (bytes))', row=1, col=1)
    # fig.update_yaxes(title_text='Memory (bytes)', row=1, col=2)
    # fig.update_yaxes(title_text='Memory (bytes)', row=1, col=3)
    # fig.update_yaxes(title_text='Memory (bytes)', row=1, col=4)
    # # fig.update_yaxes(title_text='Memory (bytes)', row=1, col=5)
    # fig.show()
    #
    # fig = make_subplots(rows=1, cols=4, subplot_titles=(
    #     'Traversed Nodes (maze-32-32-2)',
    #     'Traversed Nodes (random-64-64-20)',
    #     'Traversed Nodes (room-32-32-4)',
    #     'Traversed Nodes (room-64-64-8)'))

    # fig.add_trace(trace_a_star_edge_1, row=1, col=1)
    # fig.add_trace(trace_LRTA_edge_1, row=1, col=1)
    # fig.add_trace(trace_tt_IDA_edge_1, row=1, col=1)
    # fig.add_trace(trace_IIDA_edge_1, row=1, col=1)
    # fig.add_trace(trace_a_star_edge_2, row=1, col=1)
    # fig.add_trace(trace_LRTA_edge_2, row=1, col=1)
    # fig.add_trace(trace_tt_IDA_edge_2, row=1, col=1)
    # fig.add_trace(trace_IIDA_edge_2, row=1, col=1)
    # fig.add_trace(trace_a_star_edge_3, row=1, col=2)
    # fig.add_trace(trace_LRTA_edge_3, row=1, col=2)
    # fig.add_trace(trace_tt_IDA_edge_3, row=1, col=2)
    # fig.add_trace(trace_IIDA_edge_3, row=1, col=2)
    # fig.add_trace(trace_a_star_edge_4, row=1, col=3)
    # fig.add_trace(trace_LRTA_edge_4, row=1, col=3)
    # fig.add_trace(trace_tt_IDA_edge_4, row=1, col=3)
    # fig.add_trace(trace_IIDA_edge_4, row=1, col=3)
    # fig.add_trace(trace_a_star_edge_5, row=1, col=4)
    # fig.add_trace(trace_LRTA_edge_5, row=1, col=4)
    # fig.add_trace(trace_tt_IDA_edge_5, row=1, col=4)
    # fig.add_trace(trace_IIDA_edge_5, row=1, col=4)

    # fig.update_layout(height=600, width=2000, font=dict(family="Arial", size=15, color="black"))
    # fig.update_layout(barmode='group')
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=1)
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=2)
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=3)
    # fig.update_xaxes(title_text='Heuristic Function', row=1, col=4)
    # # fig.update_xaxes(title_text='Heuristic Function', row=1, col=5)
    # fig.update_yaxes(title_text='log_2(Number of Nodes)', row=1, col=1)
    # fig.update_yaxes(title_text='log_2(Number of Nodes)', row=1, col=2)
    # fig.update_yaxes(title_text='log_2(Number of Nodes)', row=1, col=3)
    # fig.update_yaxes(title_text='log_2(Number of Nodes)', row=1, col=4)
    # # fig.update_yaxes(title_text='log_2(Number of Nodes)', row=1, col=5)
    # fig.show()

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
