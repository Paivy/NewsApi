class Articles:
    """
    This is the Articles class that defines Articles Objects
    """
    def __init__(self,source,title,author,description,urlToimage,content,publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.urlToimage = urlToimage
        self.content = content
        self.publishedAt = publishedAt


# class Sources:
#     '''
#     Sources class that defines each source object
#     '''
#     def __init__(self,id,name,description,url,category,language,country):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.url = url
#         self.category = category
#         self.language = language
#         self.country = country
