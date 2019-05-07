# -*- coding: utf-8 -*-
"""
utils
"""


class EarlyStopping(object):
    """early stopping"""

    def __init__(self, limit=15):
        self.stop_count = 0
        self.limit = limit
        self.best_validation_loss = float('inf')

    def check(self, loss):
        if loss < self.best_validation_loss:#如果loss比之前的loss效果好，则更新；否则不更新，并计算停止次数
            self.best_validation_loss = loss
            self.stop_count = 0
        else:
            self.stop_count += 1

        if self.stop_count > self.limit: #如果停止次数超过限制，则返回true，否则false
            return True
        else:
            return False