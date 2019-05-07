import os

class HyperParams:
    """Hyper-Parameters"""
    # data path
    HOME_DIR =  "D:\pycharm\residual-attention-network-master"
    DATASET_DIR = HOME_DIR + "/dataset/"
    SAVED_PATH = HOME_DIR + "trained_models/model.ckpt"

    # dataset
    target_dataset = "CIFAR-10"

    # setting
    RANDOM_STATE = 42
    NUM_EPOCHS = 10000
    BATCH_SIZE = 64
    VALID_BATCH_SIZE = 100