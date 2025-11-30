import numpy as np
import pandas as pd
def main():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)
    
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nNumPy Array:")
    print(arr)

if __name__ == "__main__":
    main()
        