class MFPerformance:
    def __init__(self, schemename = "", crisilrank=0, ytdreturn=0,oneyreturn=0,twoyreturn=0,threeyreturn=0, fiveyreturn=0):
        self._schemename = schemename
        self._crisilrank = crisilrank
        self._ytdreturn = ytdreturn
        self._oneyreturn = oneyreturn
        self._twoyreturn = twoyreturn
        self._threeyreturn = threeyreturn
        self._fiveyreturn = fiveyreturn

    def get_schemename(self):
        return self._schemename    
    def set_schemename(self, x):
        self._schemename = x

    def get_crisilrank(self):
        return self._crisilrank
    def set_crisilrank(self, x):
        self._crisilrank = x

    def get_ytdreturn(self):
        return self._ytdreturn
    def set_ytdreturn(self, x):
        self._ytdreturn = x

    def get_oneyreturn(self):
        return self._oneyreturn
    def set_oneyreturn(self, x):
        self._oneyreturn = x

    def get_twoyreturn(self):
        return self._twoyreturn
    def set_twoyreturn(self, x):
        self._twoyreturn = x

    def get_threeyreturn(self):
        return self._threeyreturn
    def set_threeyreturn(self, x):
        self._threeyreturn = x

    def get_fiveyreturn(self):
        return self._fiveyreturn
    def set_fiveyreturn(self, x):
        self._fiveyreturn = x
