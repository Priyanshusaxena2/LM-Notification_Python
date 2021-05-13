from service import ConsoleService

if __name__ == '__main__':
    console_service = ConsoleService()
    while True:
        command_input = input()
        console_service.process_command(command_input)