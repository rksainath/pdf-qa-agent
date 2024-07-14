import threading
import time
import sys


class ProgressIndicator:
    def __init__(self):
        self.is_running = False
        self.status = "Starting..."
        self.thread = None

    def start(self):
        self.is_running = True
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join()
        sys.stdout.write('\r' + ' ' * 50 + '\r')
        sys.stdout.flush()

    def update_status(self, status):
        self.status = status

    def _animate(self):
        symbols = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        i = 0
        while self.is_running:
            i = (i + 1) % len(symbols)
            sys.stdout.write(f'\r{symbols[i]} {self.status}')
            sys.stdout.flush()
            time.sleep(0.1)
