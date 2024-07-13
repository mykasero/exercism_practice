import json
class RestAPI:
    def __init__(self, database=None):
        self.db = database
        self.url = ""
        self.template = {"name" : "x", "owes" : {}, "owed_by" : {}, "balance" : 0.0}
        self.payload = None

    def get(self, url, payload=None):
        if payload is not None:
            self.payload = json.loads(payload)

        self.url = url

        if self.url == "/users":
            if self.payload is None:
                return '{"users" : []}'

            else:
                return_val = None
                val = list(self.payload.values())[0]

                for item in self.db['users']:
                    if item['name'] == val[0]:
                        return_val = {'users' : [item]}

                return json.dumps(return_val)

    def post(self, url, payload=None):
        if payload is not None:
            self.payload = json.loads(payload)

        self.url = url

        if self.url == '/add':
            if payload is not None:
                return_val = self.template.copy()
                key,val = list(self.payload.keys()), list(self.payload.values())
                return_val['name'] = val[0]

                return json.dumps(return_val)

        elif self.url == '/iou':
            lender = self.payload['lender']
            borrower = self.payload['borrower']
            amount = self.payload['amount']

            for item in self.db['users']:

                if item['name'] == lender:
                    test1 = [person for person in item['owes'].keys() if person not in [lender, borrower]]
                    item['balance'] += amount

                    if item['owes'] != {} and test1 == []:
                        for person in list(item['owes'].keys()):
                            if person == borrower:
                                item['owes'][person] -= amount

                                if item['owes'][person] < 0:
                                    item['owed_by'].update({person : abs(item['owes'][person])})
                                    item['owes'] = {}

                                elif item['owes'][person] == 0:
                                    item['owed_by'], item['owes'] = {},{}
                    else:
                        item['owed_by'].update({borrower : amount})

                elif item['name'] == borrower:
                    test2 = [person for person in item['owed_by'].keys() if person not in [lender, borrower]]
                    item['balance'] -= amount

                    if item['owed_by'] != {} and test2 == []:
                        for person in list(item['owed_by'].keys()):
                            if person == lender:
                                item['owed_by'][person] -= amount

                                if item['owed_by'][person] < 0:
                                    item['owes'].update({person : abs(item['owed_by'][person])})
                                    item['owed_by'] = {}

                                elif item['owed_by'][person] == 0:
                                    item['owed_by'], item['owes'] = {}, {}
                    else:
                        item['owes'].update({lender : amount})

            return_val = {'users' : [item for item in self.db['users'] if item['name'] in [lender,borrower]]}

            return json.dumps(return_val)
