from . import session


class audioblast(object):
    def __init__(self, id):
        self.id = id

    @staticmethod
    def recordings(max_page=1, **attributes):
        path = "https://api.audioblast.org/data/recordings/?"+"&".join(
            f"{param}={value}"
            for param, value in attributes.items()
        )
        return audioblast.__abCall(path, max_page)

    @staticmethod
    def recordingstaxa(max_page=1, **attributes):
        path = "https://api.audioblast.org/data/recordingstaxa/?"+"&".join(
            f"{param}={value}"
            for param, value in attributes.items()
        )
        return audioblast.__abCall(path, max_page)
    
    @staticmethod
    def annotations(max_page=1, **attributes):
        path = "https://api.audioblast.org/data/annomate/?"+"&".join(
            f"{param}={value}"
            for param, value in attributes.items()
        )
        return audioblast.__abCall(path, max_page)
    
    @staticmethod
    def annomate(max_page=1, **attributes):
        path = "https://api.audioblast.org/data/annomate/?"+"&".join(
            f"{param}={value}"
            for param, value in attributes.items()
        )
        return audioblast.__abCall(path, max_page)
    
    @staticmethod
    def taxa(max_page=1, **attributes):
        path = "https://api.audioblast.org/data/taxa/?"+"&".join(
            f"{param}={value}"
            for param, value in attributes.items()
        )
        return audioblast.__abCall(path, max_page)

    @staticmethod
    def traits(max_page=1, **attributes):
        path = "https://api.audioblast.org/data/traits/?"+"&".join(
            f"{param}={value}"
            for param, value in attributes.items()
        )
        return audioblast.__abCall(path, max_page)

    @staticmethod
    def __abCall(path, max_page):
        response = session.get(path)
        parsed = response.json()
        d = parsed["data"]

        if max_page==0 or max_page > parsed["last_page"]:
            max_page=parsed["last_page"]
        
        if max_page==1:
            return d

        for page in range(2, max_page):
            n = session.get(path + f"&page={page}").json()
            d.extend(n["data"])
        
        return d