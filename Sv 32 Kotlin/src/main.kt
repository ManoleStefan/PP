fun <K,V,R>HashMap<K,V>.map(func : (Map.Entry<K, V>)->R ) : HashMap<K, R>{
    val hash = hashMapOf<K,R>()
    this.forEach {
        hash.put(it.key, func(it))
    }
    println("The result of the transformation is $hash")
    return hash
}

fun main(args: Array<String>) {
    val myHash = hashMapOf<Int, Int>(
        1 to 4,
        3 to 2,
        2 to 10,
        7 to 5
    )
    println(myHash)

    val transformed = myHash.map {
        (3*it.value - 1).toString()
    }
}