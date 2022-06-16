package org.example
import java.io.File

fun main()
{
    val fisier = File("src/fis.txt")
    /*
   val scan = Scanner(f)
   while(scan.hasNext())
   {
       lista.add(scan.next())
   }
   */

    val lista = mutableListOf<String>()
    lista.add("Cuvant")
    lista.add("s")
    lista.add("Altceva")
    lista.add("Unalta")
    lista.add("a")
    lista.add("Website")
    lista.add("b")
    println(lista.filter { it.length > 4 }.map{ it.substring(2,it.length)})
}

