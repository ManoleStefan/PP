import sun.misc.ConditionLock
import java.lang.Thread.currentThread
import java.util.concurrent.locks.Condition
import java.util.concurrent.locks.ReentrantLock

class Barrier()
{
    companion object{
        private val lock = java.lang.Object()
    }
    fun block() {
        synchronized(lock) {
            lock.wait()
        }
    }

    fun release()
    {
        synchronized(lock) {
            lock.notify()
        }

    }

    fun releaseAll()
    {
        synchronized(lock) {
            lock.notifyAll()
        }
    }
}