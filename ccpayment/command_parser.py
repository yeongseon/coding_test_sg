class Parser():

    def _parse_dollar(self, dollar_string):
        # dollar_string like $1000
        return float(dollar_string.replace("$", ""))

    def _parse_add(self, arr):
        return {"command":arr[0], "name":arr[1], "card_no":arr[2], "limit":self._parse_dollar(arr[3])}

    def _parse_charge(self, arr):
        return {"command":arr[0], "name":arr[1], "amount":self._parse_dollar(arr[2])}

    def _parse_credit(self, arr):
        return {"command":arr[0], "name":arr[1], "amount":self._parse_dollar(arr[2])}

    def get_commands(self, lines):
        commands = []
        for line in lines:
            arr = line.replace("\n", "").split(" ")
            if arr[0] == "Add":
                commands.append(self._parse_add(arr))
            elif arr[0] == "Charge":
                commands.append(self._parse_charge(arr))
            elif arr[0] == "Credit":
                commands.append(self._parse_credit(arr))
            else:
                print("not support command")
                return []

        return commands

