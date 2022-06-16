package org.example
import kotlin.random.Random

fun main(){
    println(MutableList(100){Random.nextInt(0,15)}.filter{ it % 2 == 0 }.subList(0,5).sumBy{it * it})
}

