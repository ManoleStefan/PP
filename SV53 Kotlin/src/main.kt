import java.util.*

fun main(args: Array<String>) {
    val a = generateSequence(0) { it+1 }.filter {
        (8*it - 18) % (2*it - 9) == 0 && (8*it - 18) / (2*it - 9) >= 0
    }.take(4).map { (8*it - 18) / (2*it - 9) }.sorted().toList()
    println(a)

    val b = generateSequence(0) { it + 1 }.filter {
        (9*it*it - 48*it + 16) % (3*it - 8) == 0
    }.take(13).map{  (9*it*it - 48*it + 16) / (3*it - 8) }.sorted().toList()
    println(b)

    val maxSize = 5

    val A = List(maxSize){
        val nrElem = Random().nextInt(a.size + b.size)
        (a + b).shuffled().get(nrElem)
    }

    val B = List(maxSize){
        val nrElem = Random().nextInt(a.size + b.size)
        (a + b).shuffled().get(nrElem)
    }

    println(A)
    println(B)

    val AxB = A.asSequence().map { itA -> B.map { itB -> Pair(itA, itB) } }.toList().flatMap { it }

    println(AxB)

    val BintA = B.intersect(A)

    println(BintA)

    val AxB_reu_BintA = AxB.union(BintA)

    println(AxB_reu_BintA)
}