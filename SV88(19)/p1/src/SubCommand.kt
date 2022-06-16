import java.util.concurrent.locks.Lock
import java.util.concurrent.locks.ReentrantLock

class SubCommand(val hm:HashMap<Int,Int>, var a:Int, val r : Lock) : Command
{
    override fun run():Unit
    {
        r.lock()
        for((k,v) in hm)
        {
            hm[k] = v - a
        }

        println(hm)
        r.unlock()
    }
}