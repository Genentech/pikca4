# TODO LIST
# 1. How to cope with multiple input
# 2. How to cope with multiple levels of brackets


# (xyz)*
# Example:
# text "parse"
# linerad = 10px
# linewid *= 0.5
# $h = 0.21
# C1:  circle radius 10%
# A0: arrow right linerad*2
# SSL: box "sql_stmt_list" fit with .w at (linewid right of C1.e, $h below C1)
# A1: arrow from C1.e right last box.width*2
# A2: arrow from A1.c right last box.width/2*1.3 then down even with SSL then to SSL.e
# A3: line from SSL.w left even with C1.e then up even with A1 then right to A1.c
def star(nin, nout):
    pass

# (X)?
# Example:
# linerad = 10px
# linewid *= 0.5
# $h = 0.21
# C1:  circle radius 10%
# A0:  arrow right $h from C1.e then down 1.25*$h then right $h
# SSL: box "sql_stmt_list" fit 
# A1:  arrow right $h then up 1.25*$h then right $h
# A2:  arrow from C1.e right to A1.end
def questionMark(nin, nout):
    pass

# (X|Y)
# linerad = 10px
# linewid *= 0.5
# $h = 0.21
# C1:  circle radius 10%
# A0: arrow right linerad*2
# SSL: box "sql_stmt_list" fit with .w at (linewid right of C1.e, $h below C1)
# A1: arrow from C1.e right last box.width*2
# A2: arrow from A1.c right last box.width/2*1.3 then down even with SSL then to SSL.e
# A3: line from SSL.w left even with C1.e then up even with A1 then right to A1.c
def eitherOr(nin, nout):
    pass

# (XY) chain
# text "parse"
# linerad = 10px
# # linewid *= 0.5
# $h = 0.21
# C1:  circle radius 10%
# A0: arrow right linewid
# B1: box "XYZ" fit 
# A1: arrow right linewid
# B2: box "ZYXXYZ" fit
# A2: arrow right linewid
def chain(nin, nout):
    pass

def start():
    pass
    # return nout

class convertor:
    def __init__(self):
        pass

