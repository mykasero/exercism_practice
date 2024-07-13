#STATUS 5/9 passed

import json
class RestAPI:
    def __init__(self, database=None):
        self.db = database
        self.url = ""
        self.template = {"name" : "x", "owes" : {}, "owed_by" : {}, "balance" : 0.0}
        self.payload = None

    def get(self, url, payload=None):
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
        self.payload = json.loads(payload)
        self.url = url

        if self.url == '/add':
            if payload is not None:
                return_val = self.template.copy()
                key,val = list(self.payload.keys()), list(self.payload.values())
                return_val['name'] = val[0]
                stop = "stop"
                return json.dumps(return_val)

        elif self.url == '/iou':
            lender = self.payload['lender']
            borrower = self.payload['borrower']
            amount = self.payload['amount']

            for item in self.db['users']:
                if item['name'] == lender:
                    item['balance'] += amount
                    item['owed_by'].update({borrower : amount})
                elif item['name'] == borrower:
                    item['balance'] -= amount
                    item['owes'].update({lender : amount})

            return_val = {'users' : [item for item in self.db['users'] if item['name'] in [lender,borrower]]}

            stop = "stop"
            return json.dumps(return_val)
