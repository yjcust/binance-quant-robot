import time
class LiveData:
    _instance = None   # 单例实例
    _my_spot_amount = {"USDT":1000,"DOGE":0,"DOGEUSDT":0}  # 字段，初始值为0
    _my_time = time.time()  # 字段，初始值为0
    _now_price = 0.0  # 字段，初始值为0
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LiveData, cls).__new__(cls)
        return cls._instance

    # 读取方法
    def get_spot_amount(self):
        return self._my_spot_amount

    # 更新方法
    def set_spot_amount(self, value):
        self._my_spot_amount = value
    # 读取方法
    def get_time(self):
        return self._my_time

    # 更新方法
    def set_time(self, my_time):
        self._my_time = my_time


    def get_now_price(self):
        return self._now_price

    # 更新方法
    def set_now_price(self, now_price):
        self._now_price = now_price
