# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
            
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.data:
            data = self.data[key]
            l = 0
            r = len(data) - 1

            while l <= r:
                mid = l + int((r - l + 1) / 2)
                data_timestamp, data_value = data[mid]

                if timestamp < data_timestamp:
                    r = mid - 1

                elif timestamp >= data_timestamp:
                    res = data_value
                    l = mid + 1
        
        return res
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)