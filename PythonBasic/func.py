f = lambda x : x+1
# print(f(10))

import time
class News:
    title = None
    updatedTime = None
    def __init__(self):
        self.title = "Nothing"
        self.updatedTime = time.strftime("%H:%M", time.localtime())
    # def __init__(self, title, updateTime):
    #     self.title = title
    #     self.updatedTime = time.strftime("%H:%M", updateTime)
    
    def __str__(self) -> str:
        return f"Title : {self.title}\nLast updated at : {self.updatedTime}"
whyVietnamBeautiful = News()
# print(whyVietnamBeautiful.title)
print(whyVietnamBeautiful.updatedTime)
print(whyVietnamBeautiful, end="")

del whyVietnamBeautiful
# print(whyVietnamBeautiful)
# undefined
