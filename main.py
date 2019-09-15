import sys
import os

run_ner = os.path.join(os.getcwd(),'data')
sys.path.insert(1, run_ner)


from runner import main 


if __name__ == "__main__":
    main()