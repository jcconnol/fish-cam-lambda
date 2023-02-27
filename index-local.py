import json
import datetime
import index
    
def main():
    print(index.endpoint({ "bucket_path": "fish-cam"}, {}))

if __name__ == "__main__":
    main()