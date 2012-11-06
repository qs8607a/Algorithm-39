package eulertools


func Primes(n int64)[]int64{
    result := make([]int64, 0)
    if n >= 2{
        result = append(result, 2)
        flags := make([]bool, (n - 1)/2)
        for i, _ := range flags{
            if !flags[i]{
                result = append(result, int64(2 * i + 3))
                for j:= 3*i+3;j<len(flags); j += (2*i+3){
                    if j < len(flags){
                        flags[j]=true
                    }
                }
            }
        }
    }
    return result
}
