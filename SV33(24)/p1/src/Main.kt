import java.io.File

fun main()
{
    var s = File("input.txt").readText().split(" ").toList()

    println(s.filter { it.length>=4 }.map{it-> it.substring(it.length/2-1,it.length/2+1)})
}