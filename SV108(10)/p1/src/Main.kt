import java.util.concurrent.ConcurrentHashMap

class Memoize<in T, out R>(val f: (T) -> R):(T) -> R{

    private val values = ConcurrentHashMap<T,R>()
    override fun invoke(p1: T): R {
        return values.getOrPut(p1,{f(p1)})
    }
}

fun <T,R>((T) -> R).memoize(): (T) -> R = Memoize(this)

val memoizedSumFactors = { x:Int ->  x }.memoize()

fun main()
{
    var a = 3
    var c = 0

    while(a<=9)
    {
        c = memoizedSumFactors(a-1) + memoizedSumFactors(a-2)
        println(memoizedSumFactors(a-2))
        println(memoizedSumFactors(a-1))
        a = a+1
    }

    println(c)
}