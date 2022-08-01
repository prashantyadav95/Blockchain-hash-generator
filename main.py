# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Blockchain hash generator coding sample.

import hashlib

class neurocoin_block:

    def __init__(self,previous_block_hash, transaction_list):
        self.previous_block_hash= previous_block_hash
        self.transaction_list = transaction_list

self.blockdata = "-".join(transaction_list) + "--" + previous_block_hash
self.blockhash = hashlib.sha256(self.blockdata.encode()).hexdigest()

#now some dummy transaction for generating hash.

t1 = " Manish sends 9 nc to rishabh"
t2 = " akshay sends 3 nc to tarak"
t3 = " tarak sends 4 nc to saurabh"

# making block and its hash
starting_block = neurocoin_block("Initial string", [t1,t2])
print(starting_block.blockdata)
print(starting_block.bockhash)

second_block = neurocoin_block("starting_block",[t2,t3])
print(second_block.blockdata)
print(seconf_block.blockhash)







