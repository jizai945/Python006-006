class Open():
    def __enter__(self):
        print('open')
    
    def __exit__(self, type, value, traceback):
        print('close')

    def __call__(self):
        print('666')
        pass

with Open() as f:
    pass

test = Open()
test()