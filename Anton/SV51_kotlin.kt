package org.example

fun main(){
    val a = setOf(3,4,5,6)
    val b = setOf(1,2,3,4)
    println((a intersect b) intersect (b union a))
    println((a intersect b) union (b intersect b))
    //add to dictionary e useless in this context
}
