from Code.structured_logging.command_queue.command import Command
import threading

from time import sleep

class Queue:
    def __init__(self, async_wait_delay_in_seconds):
        self.async_wait_delay_in_seconds = async_wait_delay_in_seconds
        self.__commands:list[Command] = []
        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()

    def add(self, command: Command):
        self.__commands.append(command)

    def __process(self):
        while True:
            while self.__commands != []:
                self.__commands.pop(0).execute()
            sleep(self.async_wait_delay_in_seconds)
