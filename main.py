from header import func_list, config

def main():
    # Pull the execution module from the config file, this will be passed by the args when the program starts.
    # Depending on the args passed, the program will execute the corresponding function.
    executed_func = func_list[config.exec_mudule]
    executed_func()

if __name__ == "__main__":
    main()