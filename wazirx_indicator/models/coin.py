class Coin:

    def __init__(self):
        self.name = ""
        self.display_name = ""
        self.api_index = ""
        self.current_price = ""
        self.low_price = ""
        self.high_price = ""
        self.is_favourite = False

    def __str__(self):
        return self.name + " " + self + self.display_name + " " + self.currency

    @property
    def symbol(self):
        return self.display_name.split("/")[0]

    @property
    def currency(self):
        splits = self.display_name.split("/")
        if len(splits) > 1:
            return splits[1]
        return ""
