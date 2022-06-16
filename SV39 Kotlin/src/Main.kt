import java.lang.Exception
import java.util.*
import kotlin.random.Random

fun main() {
    val nrValues = 10

    val list = List(10){Random.nextInt(0, 10) * 2}

    val buffer = Scanner(System.`in`)
    print("Inceput de interval: ")
    val start = buffer.nextInt()
    print("Final de interval: ")
    val end = buffer.nextInt()

    if(start > end)
        throw Exception("Valoarea de inceput trebuie sa fie mai mica decat cea de final")

    if(end >= nrValues || start < 0)
        throw Exception("Capetele intervalului trebuie sa fie numere pozitive mai mici strict decat 100")

    val b = ArrayList<Int>()

    // calcul primul i
    var myValue = 0
    for(i in 0 until start)
        myValue += list[i]*list[i]

    b.add(myValue)

    for(i in start until end) {
        myValue += list[i]*list[i]
        b.add(myValue)
    }

    println("list is $list")

    b.forEachIndexed{index, value ->
        println("${index + start} calculated is $value")
    }

}