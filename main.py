import sys

def main():
    if sys.argv[1] == "train":
        import src.trainning.trainning_model

if __name__ == "__main__":
    main()