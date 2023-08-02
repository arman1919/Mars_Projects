def add_zero(num):
    return (64-len(num))*"0"+num


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
        
        if n > self.size or n < 0:
            print("Index out of range")
            raise IndexError
        
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
        
        if n > self.size or n < 0:
            print("Index out of range")
            raise IndexError
        
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
    
    v = Bit_Vektor(459)

    v.set(32)
    print(v)

    print()

    v.reset(32)
    print(v)
