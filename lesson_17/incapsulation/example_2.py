class Car:
    def __init__(self, model, year, win_code):
        self.__win_code = win_code
        self.model = model
        self.year = year
        self.status = None

    def get_win_code(self):
        self.open_hood()
        self._take_off_case()
        return self.__win_code

    def set_win_code(self):
        # raise NotImplementedError()
        ...


    def open_hood(self):
        ...

    def _take_off_case(self):
        ...

    def drive(self):
        if self.status == "READY" and self.SHIFT == "D":
            self.__drive()

    def start_engine(self):
        if self.__pump_fuel_in_system() is False:
            raise Exception("FUEL CHECK")


        if self.__start_electronics() is False:
            raise Exception("ELECTRO CHECK")


        if self.__ignite_candles() is False:
            raise Exception

        self.status = "READY"
        return


    def __pump_fuel_in_system(self):
        ...

    def __start_electronics(self):
        ...

    def __ignite_candles(self):
        ...



