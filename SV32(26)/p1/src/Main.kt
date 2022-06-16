import kotlin.properties.Delegates

class HashMapFunctor<K,V>(val hm:HashMap<K,V>)
{
    fun map(f : (V) -> V) : HashMapFunctor<K,V>
    {
        var result = HashMap<K,V>()

        for( (k,v) in hm )
        {
            result[k] = f(hm[k]!!)
        }

        return HashMapFunctor(result)
    }
}

fun f(x:Int):Int
{
    return 3*x-1
}

fun main()
{
    var hm = HashMap<Int,Int>()
    hm.put(0,2)
    hm.put(1,5)
    hm.put(2,10)

    println(HashMapFunctor(hm).map(::f).hm)
}