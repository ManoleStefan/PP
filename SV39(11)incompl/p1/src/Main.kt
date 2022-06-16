import java.lang.Math.random

fun main()
{
    val n = 100
    var i = 1
    val A = mutableListOf<Int>()

    repeat(100){
        A.add((random()*1000).toInt())
    }

    println(A)
    var B = A.asSequence().map{it+it%2}.toList()
    println(B)
    var s = 0
    while(i<n)
    {
        s = s + B[i]*B[i]
        i++
    }

    println(s)
}