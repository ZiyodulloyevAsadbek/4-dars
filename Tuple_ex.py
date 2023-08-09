from collections import namedtuple
Phone_info = namedtuple('Phone_info', 'sim_name, sim_price')

Phone_1 = ['Uzmobile', '30$']

Phone_info._make(Phone_1)
print(Phone_info)