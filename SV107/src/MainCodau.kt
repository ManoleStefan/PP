import java.nio.IntBuffer
import java.util.concurrent.locks.ReentrantLock

var barrier = Barrier()

class Sum1(val hm:HashMap<Int,Int>) : Runnable
{
    override fun run() {

        barrier.block()
            var s = 0

            for ((k, v) in hm) {
                s += hm[k]!!
            }
            print(s)

        }
}


class Sum2(val hm:HashMap<Int,Int>) : Runnable
{
    override fun run()
    {
        barrier.block()
            var s = 0

            for((k,v) in hm)
            {
                s += hm[k]!!
            }
            print(s)
        //barrier.release()
    }

}

fun main()
{

    var hm = HashMap<Int,Int>()
    hm.put(1,2)
    hm.put(2,3)
    hm.put(3,4)

    var t1 = Thread(Sum1(hm))
    var t2 = Thread(Sum1(hm))

    t1.start()
    t2.start()

    Thread.sleep(1000)
    barrier.releaseAll()

}