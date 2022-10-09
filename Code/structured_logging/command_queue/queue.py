from structured_logging.command_queue.command import Command
import threading

from Code.structured_logging.infrastructure.container import Container

from time import sleep

class Queue:
    # TODO: we also need to inject the async delay time into the constructor
    def __init__(self):
        # TODO INJECT THIS PROPERLY!!!
        self.async_wait_delay_in_seconds = 1
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
