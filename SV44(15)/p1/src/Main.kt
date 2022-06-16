import java.lang.Math.random


fun main()
{
    val A = mutableListOf<Int>()
    repeat(15){
        A.add((random()*100).toInt())
    }

    val B = mutableListOf<Int>()
    repeat(15){
        B.add((random()*100).toInt())
    }

    val C = mutableListOf<List<Int>>()

    A.forEach { it -> for(i in B) C.add(listOf<Int>(it,i)) }
//    for(i in A)
//    {
//        for(j in B)
//        {
//            C.add(i)
//            C.add(j)
//        }
//    }
//
//    println(C.chunked(2))
    println(C)

}