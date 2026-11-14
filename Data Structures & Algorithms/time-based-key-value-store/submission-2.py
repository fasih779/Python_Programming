class TimeMap:

    def __init__(self):
        
        self.ha={}
       

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ha:
            self.ha[key] = []

        self.ha[key].append([value, timestamp])
     
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ha:
            return ""
        arr=self.ha[key]
        l,r=0,len(arr)-1
        result=""
        while l<=r:
            mid=(l+r)//2
            if  arr[mid][1]<=timestamp:
                result=arr[mid][0]
                l=mid+1
            else:
                r=mid-1


        return result
       