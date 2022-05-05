# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:18:11 2021

@author: belie
"""

import hxdata_mod as HX
import average_convolve
from matplotlib import pyplot as plt


def select(time, value, t_min, t_max):
    select_value = value[time >= t_min]
    select_time = time[time >= t_min]
    select_value = select_value[select_time <= t_max]
    select_time = select_time[select_time <= t_max]
    return(select_time, select_value)


# %%
shot = 35442
module_num = 1  # moduleの場所
trigger = 1  # 1secにトリガー入る
gain = 8  # 信号強度のスケールを使用 詳しくは鈴川さんの修士論文に記載
lowene = 25  # 25 keV以上の信号を観測
hx_ene_array, hx_time_array, hxtime = HX.get_HX_data_with_SiO2(
    shot, module_num, trigger, gain, lowene)  # 石英窓の影響考慮
hx_int = hx_time_array['intensity'].values
hx_cot = hx_time_array['count'].values
hx_ene = hx_time_array['energy'].values
hxtime_sel, hxint_sel = select(hxtime, hx_int, 0, 5)
width = 15e-3
hx_time_ave, hx_int_ave = average_convolve.average_convolve_boxcar(
    width, hxtime_sel, hxint_sel)

plt.figure()
plt.plot(hx_time_ave, hx_int_ave)
plt.show()

plt.figure()
plt.plot(hxtime, hx_cot)
plt.show()  # test
