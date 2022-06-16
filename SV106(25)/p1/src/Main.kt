import java.io.File
import java.io.FileWriter
import java.util.concurrent.ConcurrentHashMap
import kotlin.concurrent.thread

fun main()
{
    var t1 = thread(start=false,isDaemon = true){
        val f = File("src/input.txt")
        val s = f.readText().split(" ").toList()
        println(s)

        var i = 0
        var hm = ConcurrentHashMap<Int,Int>()
        while(i<s.size)
        {
            hm.put(i,s[i].toInt())
            i++
        }


        var part = hm.size/3
        var t2 = Thread(){
            var j=0
            for(j in (0..part-1))
            {
                var aux = hm.get(j)
                aux = aux!! * 2
                hm.put(j,aux)
            }
        }

        var t3 = Thread{
            var j=0
            for(j in (part..2*part-1))
            {
                var aux = hm.get(j)
                aux = aux!! * 3
                hm.put(j,aux!!)
            }
        }

        var t4 = Thread{
            var j=0
            for(j in (2*part..3*part))
            {
                var aux = hm.get(j)
                aux = aux!! * 4
                hm.put(j,aux!!)
            }
        }

        t2.start()
        t3.start()
        t4.start()

        t2.join()
        t3.join()
        t4.join()

        println(hm)
    }
    t1.start()
    t1.join()
}