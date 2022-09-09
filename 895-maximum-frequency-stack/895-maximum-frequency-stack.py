class FreqStack:

    def __init__(self):
        self.freq_counter = dict()
        self.freq_stack = dict() # dict of frequency to stack of elements with that freq
        self.max_freq = -float("inf")

    def push(self, val: int) -> None:
        
        if val not in self.freq_counter:
            self.freq_counter[val] = 0
        self.freq_counter[val] += 1
        
        if self.freq_counter[val] not in self.freq_stack:
            self.freq_stack[self.freq_counter[val]] = []
            
        self.freq_stack[self.freq_counter[val]] += [val]
        
        if self.freq_counter[val] > self.max_freq:
            self.max_freq = self.freq_counter[val]

    def pop(self) -> int:
        # print(self.max_freq,self.freq_stack)
        val = self.freq_stack[self.max_freq].pop()
        if len(self.freq_stack[self.max_freq]) == 0:
            self.freq_stack.pop(self.max_freq)
            self.max_freq -= 1
        self.freq_counter[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()