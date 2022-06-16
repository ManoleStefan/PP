import sun.nio.ch.FileChannelImpl.open
import java.io.File
import java.io.FileWriter
import java.time.LocalDateTime.now

class PriceObserver(var price:Double) : Observer {
    override fun update(rate_of_change: Double,filename:String) {
        price += price*rate_of_change
        var f = File(filename)
        f.writeText("" + now() + ": Rata de crestere a pretului: " + rate_of_change + "; Pretul curent: " + price)
    }
}