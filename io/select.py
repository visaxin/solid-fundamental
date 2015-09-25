
POLL_NULL = 0x00
POLL_IN = 0x01
POLL_OUT = 0x04
POLL_ERR = 0x08


class Select(object):
    def __init__(self):
        self.read_list = set()
        self.write_list = set()
        self.error_list = set()

    def poll(self,timeout):
        r,w,x = select.select(self.read_list,self.write_list,self.error_list,
                                timeout)
        results = defaultdict(lambda:POLL_NULL)

        for p in [(r, POLL_IN), (w, POLL_OUT),(e,POLL_ERR)]:
            for fd in p[0]:
                results[fd] |= p[1]
        return results.items()

    def register(self,fd,mode):
        if mode & POLL_IN:
            self.read_list.add(fd)
        if mode & POLL_OUT:
            self.write_list.add(fd)
        if mode & POLL_ERR:
            self.error_list.add(fd)
