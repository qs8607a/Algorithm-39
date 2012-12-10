package question
import "eulertools"

func exp_mod(a int64, b int64, p int64)int64{
    if b == 0{
        return 1
    }else if b % 2 == 0{
        tmp := exp_mod(a, b /2, p)
        return (tmp * tmp) % p
    }else{
        return (exp_mod(a, b - 1, p) * a) % p
    }
    return 0
}

func is_factor_of_R_n(p int64)bool{
    var a int64
    a = 10
    is_cycle := make(map[int64] bool)
    for{
        var sum int64
        sum =0
        for i :=0; i<10; i++{
            sum += exp_mod(int64(a), int64(i), p)
        }
        if(sum % p == 0){
            return true
        }
        _, in_cycle := is_cycle[a % p]
        if in_cycle{
            return false
        }
        is_cycle[a % p] = true
        a = exp_mod(a, 10, p)
    }
    return false
}

func P133(n int64)int64{
    //P133(100000)
    var result int64
    result = 0
    for _, p := range eulertools.Primes(n){
        if !is_factor_of_R_n(p){
            result += p
        }
    }
    return result
}
