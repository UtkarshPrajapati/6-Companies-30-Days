class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        cities=defaultdict(lambda: defaultdict(list))
        output=[]
        for t in transactions:
            name,time,amount,city=t.split(',')
            cities[city][name].append(time)
        for t in transactions:
            name,time,amount,city=t.split(',')
            if int(amount)>1000: output.append(t);continue
            for k,v in cities.items():
                if k==city: continue
                if any([abs(int(x)-int(time))<=60 for x in v[name]]): output.append(t);break
        return output