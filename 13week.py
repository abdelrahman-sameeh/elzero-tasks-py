# task 1
# "eeeeE llllLl lllzzZzzzz eroe operationr pollo "

# result >>>>  (\w)

# ----------------------------------------------------------
# task 2
# "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"

# result >>>>  L(Elzero)


# ----------------------------------------------------------
# task 3


# +(0100) 600-1234
# +(0100) 60-1234
# (0100) 6000-1234
# 01006001234
# 0100 600 1234
# (0100) 600-1
# (0100) 600-12

# result >>>>  \+?\(0100\) \d{2,}-\d{4}


# ----------------------------------------------------------
# task 4
# http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py
# https://elzero.com/link.py
# http://www.elzero.net
# https://elzero.net

# result >>>>    https?://(www)?.\w+.\w+(:\d+)?/link.\w+


# ----------------------------------------------------------
# task 5

# http
# https
# abcd
# abcd


# way 1 >>>>>   https?
# way 2 >>>>>   h\w+
# way 3 >>>>>   ht\w+
# way 4 >>>>>   h\w{3,4}
# way 5 >>>>>   

