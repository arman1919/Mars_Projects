def add_zero(num):
    return (64-len(num))*"0"+num


def check_int(input_message,min_value,max_value):
    """_summary_

    Args:
        input_message (str): input_message
        min_value (int): min_value
        max_value (int): max_value



    Returns:
        _type_: int
    """
    
    while True:
        num = input(input_message)
    
        try:
            
            num = int(num)
            
            if num > max_value or num < min_value:
                raise ValueError
            
            return num
        
        except ValueError:
            print("ValueError, enter agin")
            continue
    

class Bit_Vektor:
    def __init__(self,size:int) -> None:
        """_summary_

        Args:
            size (int): Size of bit-vektor
            
        """
        self.size = size
        list_size = size // 64 +1
        print(f"number of cells - {list_size}")
        
        print(f"number of bits - 64")
        
        self._vektor_list = []
        for _ in range(list_size):
            self._vektor_list.append(0)
        
        
    def set(self,n:int):
        """_summary_
        
        changes the value under the index to 1
        
        Args:
            n (int): bit index
            (   0 <= n < size of bit-vektor )
            
        """
        
        cell = n // 64
        
        index = n % 64
         
        
        self._vektor_list[-cell-1] |= (1 << index)
        
    
    def reset(self,n):
        """_summary_
        
        changes the value under the index to 0
        
        Args:
            n (int): bit index
            (   0 <= n < size of bit-vektor )
            
        """
    
        
        cell = n // 64
        
        index = n % 64
              
        self._vektor_list[-cell-1] &= ~(1 << index)
    
    
    def __str__(self) -> str:
        """
        print bit-vektor
        
        """
        vektor = ""
        for i in self._vektor_list[:-1]:
            
            v = str(bin(i))[2:]
            
            vektor += add_zero(v)+"-"
            
        v = str(bin(self._vektor_list[-1]))[2:]
        vektor += add_zero(v)
         
        return vektor
    
    
        

if __name__ == "__main__":
    
    input_message = "Enter size forbit-vektor - "
    
    size = check_int(input_message,0,100000)
    
    bit_vektor = Bit_Vektor(size)
            
    
    while True:
        input_message = "Enter orpeator - "
        print("1) put 1 in the specified position ")
        print("2) put 0 in the specified position")
        print("3) Print bit-vektor")
        print("0) exit")
        
        sel = check_int(input_message,0,3)

        if sel == 0:
            break
        elif sel == 1:
            input_message = f"Enter pazition 0 - {size} - "
            
            
            index = check_int(input_message,0,size)
            bit_vektor.set(index)
            print(f"the number at position {index} has been changed to 1")
        elif sel == 2:
            input_message = f"Enter pazition 0 - {size} - "
            
            
            index = check_int(input_message,0,size)
            bit_vektor.set(index)  
            print(f"the number at position {index} has been changed to 0")
        elif sel == 3:
            print(bit_vektor)
            