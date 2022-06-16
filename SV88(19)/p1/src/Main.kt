import java.util.concurrent.locks.Lock
import java.util.concurrent.locks.ReentrantLock

class Invoker(val commands: MutableList<Command>)
{
    fun setCommand(c:Command)
    {
        commands.add(c)
    }

    fun executeAll()
    {
        for(c in commands)
        {
            val t = Thread(c)
            t.start()
        }
    }
}

fun main()
{
    val hm = HashMap<Int,Int>()

    hm.put(1,12)
    hm.put(2,20)
    hm.put(3,7)
    val r = ReentrantLock()
    val inv = Invoker(mutableListOf<Command>(AddCommand(hm,1,r),SubCommand(hm,2,r)))
    inv.executeAll()
}
