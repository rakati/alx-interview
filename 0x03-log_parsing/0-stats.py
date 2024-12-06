#!/usr/bin/python3
'''
Writing log parsing script that handle the following
- Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these
  statistics from the beginning:
    - Total file size: File size: <total size>
    - where <total size> is the sum of all previous <file size> (see input
      format above)
    - Number of lines by status code:
        - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        - if a status code doesn’t appear or is not an integer, don’t print
          anything for this status code
        - format: <status code>: <number>
        - status codes should be printed in ascending order
'''

if __name__ == "__main__":
    import re
    import fileinput
    import signal

    # count the number of lines read
    c = 0
    # ip = r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'
    # date = r'\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}.\d{1,6}'
    log_pattern = r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3} - '\
                  r'\[\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}.\d{1,6}\]'\
                  r' "GET \/projects\/260 HTTP\/1.1" \d{3} \d{1,4}'
    st = {
            '200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
            '405': 0, '500': 0
        }
    all_status = ['200', '301', '400', '401', '403', '404', '405', '500']
    d = st.copy()
    fs = 0
    for line in fileinput.input():
        # checking line format
        # "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n
        # increment counter only for valid lines
        c += 1
        if re.match(log_pattern, line):
            status_code, size = line.split()[-2:]
            fs += int(size)
            if status_code in all_status:
                d[status_code] += 1

        def print_log_info(sig, frame):
            """print log info"""
            print("File size:", fs)
            for status in all_status:
                if d[status] > 0:
                    print(f'{status}: {d[status]}')
        if c == 10:
            print_log_info(0, 0)
            # reset log counter
            c = 0
            # reset status counter
            d = st.copy()
            # reset file size to 0
            fs = 0
        signal.signal(signal.SIGINT, print_log_info)
