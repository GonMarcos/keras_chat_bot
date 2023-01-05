import sys

def main():
    if sys.argv[1] == "train":
        import src.training.training_model

if __name__ == "__main__":
    main()