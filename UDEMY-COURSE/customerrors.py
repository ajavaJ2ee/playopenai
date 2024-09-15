class customerror(TypeError):
    def __init__(self,message,code):
        super().__init__(f'Error code {code}:{message}')


raise customerror('This is custom error',500)


