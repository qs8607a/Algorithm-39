package question

import "eulertools"

func P5(n int64) int64{
    result := int64(1)
    for _, p := range eulertools.Primes(n){
        var b int64
        for b=p;b * p<=n;b *=p {
        }
        result *= b
    }
    return result
}

