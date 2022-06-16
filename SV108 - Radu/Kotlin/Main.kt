import java.util.concurrent.ConcurrentHashMap
import kotlin.system.measureNanoTime

class SimpleFunctionWithMemoization(var m: ConcurrentHashMap<Int, Int>){
    init {
        m[0] = 1
        m[-1] = 1
    }

    fun f(i: Int): Int {
        if(m[i] != null)
            return m[i]!!

        if (i == 0 || i == -1)
            return 1

        m.putIfAbsent(i,f(i-1) + f(i-2))
        return m[i]!!
    }
}

class SimpleFunctionWithoutMemoization{
    fun f(i: Int): Int {
        if (i == 0 || i == -1)
            return 1
        return f(i-1) + f(i-2)
    }
}

fun main(){
    val m = ConcurrentHashMap<Int, Int>()
    val a = SimpleFunctionWithMemoization(m)
    val b = SimpleFunctionWithoutMemoization()
    var time = measureNanoTime {  print(a.f(40)) }
    println(" cu timpul $time ns")
    time = measureNanoTime { print(b.f(40)) }
    println(" cu timpul $time ns")
}