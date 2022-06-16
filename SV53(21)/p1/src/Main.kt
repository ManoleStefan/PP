

fun cartesian_prod(A:List<Int>,B:List<Int>) : List<List<Int>>
{
    var C = mutableListOf<Int>()

    for(i in A)
    {
        for(j in B)
        {
            C.add(i)
            C.add(j)
        }
    }

    return C.chunked(2)
}

fun main()
{
    var n=0
    val A = mutableListOf<Int>()
    val B = mutableListOf<Int>()

    repeat(100){
        A.add((8*n-18)/(2*n-9))
        B.add((9*n*n-48*n+16)/(3*n-8))
        n++
    }

    println(A)
    println(B)
    val C = cartesian_prod(A,B)
    println(C.union(A.intersect(B)))

}