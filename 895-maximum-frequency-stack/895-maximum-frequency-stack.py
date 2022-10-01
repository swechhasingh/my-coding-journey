class FreqStack:

    def __init__(self):
        self.freq_counter = dict()
        self.freq_stack = dict() # dict of frequency to stack of elements with that freq
        self.max_freq = 0

    def push(self, val: int) -> None:
        
        if val not in self.freq_counter:
            self.freq_counter[val] = 0
        self.freq_counter[val] += 1
        
        curr_freq = self.freq_counter[val]
        
        if curr_freq not in self.freq_stack:
            self.freq_stack[curr_freq] = []
            
        self.freq_stack[curr_freq] += [val]
        
        if curr_freq > self.max_freq:
            self.max_freq = curr_freq

    def pop(self) -> int:
        val = self.freq_stack[self.max_freq].pop()
        if not len(self.freq_stack[self.max_freq]):
            self.freq_stack.pop(self.max_freq)
            self.max_freq -= 1
        self.freq_counter[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()