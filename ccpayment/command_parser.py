class Parser():

    def _parse_add(self, arr):
        return {"command":arr[0], "name":arr[1], "card_no":arr[2], "limit":arr[3]}

    def _parse_charge(self, arr):
        return {"command":arr[0], "name":arr[1], "amount":arr[2]}

    def _parse_credit(self, arr):
        return {"command":arr[0], "name":arr[1], "amount":arr[2]}

    def get_commands(self, file_path):
        commands = []
        file = open(file_path)
        lines = file.readlines()
        for line in lines:
            arr = line.replace("\n", "").split(" ")
            if arr[0] == "Add":
                commands.append(self._parse_add(arr))
            elif arr[0] == "Charge":
                commands.append(self._parse_charge(arr))
            elif arr[0] == "Credit":
                commands.append(self._parse_credit(arr))
        file.close()
        return commands

