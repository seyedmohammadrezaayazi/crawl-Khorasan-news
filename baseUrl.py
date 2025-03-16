class URL():

    def __init__(self, url, name, pages, UpVersionNumber, downVersionNumber):
        # 'http://khorasannews.com/?nid=' + str(id) + '&pid=3&type=0'
        self.baseUrl = url
        self.name = name
        self.pages = pages
        self.UpVersionNumber = UpVersionNumber
        self.downVersionNumber = downVersionNumber
