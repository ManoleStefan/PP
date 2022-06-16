

fun getSubset(A:List<Int>):List<List<Int>>
{
    var C = mutableListOf<List<Int>>()
    for( i in 0..A.size-4)
    {
        for( j in i+1..A.size-3)
        {
            for( k in j+1..A.size-2)
            {
                for( l in k+1..A.size-1)
                {
                    var B = mutableListOf<Int>()
                    B.add(A[i])
                    B.add(A[j])
                    B.add(A[k])
                    B.add(A[l])
                    C.add(B)
                }
            }
        }
    }

    return C
}

fun main()
{
    var A = mutableListOf<Int>()

    for(i in 1..10)
    {
        A.add(i)
    }

    var B = getSubset(A)

    println(B.filter{it.contains(1)})

}