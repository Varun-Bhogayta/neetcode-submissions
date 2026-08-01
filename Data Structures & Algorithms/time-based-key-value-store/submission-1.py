class TimeMap:

    def __init__(self):
        self.data : dict[str,list[tuple[int,str]]] = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:    
        res = ""
        timestamps = self.data.get(key,[])
        start, end = 0,len(timestamps)-1
        
        while start <= end:
            mid = start + (end - start)//2
            if timestamps[mid][0] <= timestamp:
                res = timestamps[mid][1]
                start = mid + 1
            else:
                end = mid - 1

        return res   


