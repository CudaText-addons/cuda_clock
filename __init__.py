from datetime import datetime
from cudatext import *

MYCELL = app_proc(PROC_GET_UNIQUE_TAG, '')

class Command:
    id_st = 0
    inited = False

    def tick(self, tag='', info=''):
        # add statusbar cell later, so it appears in the right edge
        if not self.inited:
            self.inited = True
            statusbar_proc(self.id_st, STATUSBAR_ADD_CELL, tag=MYCELL)
            statusbar_proc(self.id_st, STATUSBAR_SET_CELL_AUTOSIZE, tag=MYCELL, value=1)

        now = datetime.now()
        s = now.strftime("%H:%M:%S")
        statusbar_proc(self.id_st, STATUSBAR_SET_CELL_TEXT, tag=MYCELL, value=s)

    def on_start(self, ed_self):
        self.id_st = app_proc(PROC_GET_MAIN_STATUSBAR, '')
        timer_proc(TIMER_START, 'cuda_clock.tick', 1000, '')
