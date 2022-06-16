
fun main(args: Array<String>) {
    val a = listOf(1, 2, 3)
    val b = listOf(2, 3, 4)

    println(a)
    println(b)

    val AxB = a.map { itA -> b.map { itB -> Pair(itA, itB) } }.flatMap { it }.distinct()
    val BxA = b.map { itB -> a.map { itA -> Pair(itB, itA) } }.flatMap { it }.distinct()

    println(AxB)
    println(BxA)

    val intersect = AxB.filter{
        BxA.contains(it)
    }
    println(intersect)

    val myMap = intersect.groupBy { it.first }.map {
        Pair(it.key, it.value.map {index ->
            index.second
        })
    }.toMap()
    println(myMap)
}