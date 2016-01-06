    def is_greater_than(self,other):
        try:
            # are they comparable (both of type int)
            if int(self.value) > int(other.value):
                return True
            else:
                return False
        except ValueError:
            # find value of card
            print(self.value)
            if self.value == "Jack" or self.value == "Queen" or self.value == "King":
                self_value = 10
            elif self.value == "Ace":
                self_value = 11
            else:
                self_value = self.value
                print(self.value)
            # find value of other card
            print(other.value)
            if other.value == "Jack" or self.value == "Queen" or self.value == "King":
                other_value = 10
            elif other.value == "Ace":
                other_value = 11
            else:
                other_value = other.value
                print(self.value)
            # compare values for return, return
            if self_value > other_value:
                return True
            else:
                return False


