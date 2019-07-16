class Test():
    def __getitem__(self, items):
        print(f'{type(items)}, {items}')
import pdb;pdb.set_trace()
t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]

