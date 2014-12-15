__author__ = 'aouyang1'


from util.strategies import *
from util.indicators import *


# Define general backtesting parameters
def set_backtest_options(bt):
    bt.instr_name = 'GC'
    bt.RANGE = 10
    bt.init_day = '2013-09-10 17:00:00'
    bt.final_day = '2013-09-30 16:59:59'

    bt.optimization = True
    bt.log_intrabar_data = False
    bt.write_trade_data = False
    # TODO: manage how to declare a folder name for trade data
    bt.write_bar_data = False
    # TODO: manage how to declare a file name for bar data


# Setup number of strategies and indicators
def set_strategies(bt):

    # FT_QUICKY_BASE for GC
    indicators = {}
    indicators['FT'] = FisherTransform(bt, bt.range_bar.Close, 15)
    indicators['FTD'] = Diff(bt, indicators['FT'].val, 2)
    for PL in range(17, 18):
        bt.strategies['FT_Quicky_Base_PL' + str(PL)] = FT_Quicky_Base(backtest=bt,
                                                                      indicators=indicators,
                                                                      PL=PL,
                                                                      offset=3,
                                                                      FTdthresh=0.1,
                                                                      FTthresh=2.5,
                                                                      maxBars=1)

