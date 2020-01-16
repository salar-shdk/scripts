from time import time, process_time, strftime, localtime
from datetime import timedelta


def time_to_str(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))


class EvaluationLog():

    def start_log(self, s="Start Program"):
        self.start = time()
        self.cpu_start = process_time()
        self.log(s)

    def end_log(self, s="End Program"):
        self.end = time()
        self.cpu_end = process_time()
        elapsed_time = self.end - self.start
        cpu_time = self.cpu_end - self.cpu_start
        self.log(s, time_to_str(elapsed_time), time_to_str(cpu_time))

    @staticmethod
    def log(s, elapsed_time=None, cpu_time=None):
        line = "=" * 40
        print(line)
        print(time_to_str(), '-', s)

        if elapsed_time:
            print("Elapsed time:", elapsed_time)
        if cpu_time:
            print("CPU time:", cpu_time)

        print(line)

