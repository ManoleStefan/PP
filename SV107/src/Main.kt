import sun.awt.Mutex
import java.util.*
import java.util.concurrent.locks.Lock
import java.util.concurrent.locks.ReentrantLock
import kotlin.concurrent.thread

class myBarrier(private val numberOfThreads : Int){
    private val myList = mutableListOf<Thread>()
    private val myMutex = Mutex()
    private val lock = Object()

    fun addThread() {
        synchronized(lock) {
            myList.add(Thread.currentThread())
            println("${Thread.currentThread().name} was added to barrier!")
            if (myList.size == numberOfThreads) {
                println("${Thread.currentThread().name} is releasing the threads from the barrier!")
                myList.forEach {
                    print(" ${it.name} ")
                }
                print("were notified to continue!")
                myList.clear()
                //myMutex.unlock()
                lock.notifyAll()
            } else {
                println("${Thread.currentThread().name} is waiting for new threads!")
                lock.wait()
            }
        }
    }
}

val mybarrier = myBarrier(3)

fun main(args: Array<String>) {
    val jobs = List<Thread>(6){
        Thread{
            println("${Thread.currentThread().name} started!")
            mybarrier.addThread()
            println("${Thread.currentThread().name} ended!")
        }
    }
    jobs.forEach { it.start() }
    jobs.forEach { it.join() }
}