import java.io.IOException
import java.nio.file.Files
import java.nio.file.Paths
import java.nio.file.StandardOpenOption
import java.time.LocalDateTime
import kotlin.system.exitProcess

interface Observer {
    fun update(realUser: RealUser)
}

interface Observable{
    fun attach(o:Observer)
}

interface User{
    fun login()
}

interface Logger{
    fun writeData(data: String)
}

abstract class Product(private var price: Double){
    protected var name: String = ""

    fun getPrice(): Double {
        return this.price
    }

    fun getProductName() : String{
        return this.name
    }

    fun setPrice(price: Double){
        this.price = price
    }
}

class Tomatoes(price: Double) : Product(price) {
    init {
        this.name = "Tomatoes"
    }
}

class PriceCalc(private val p : Product) : Observer{

    private val logger = MyLogger("logger.txt")

    override fun update(realUser: RealUser){
        print("Enter the discount rate: ")

        val per = KeyboardReader.read()?.toFloat()
        if (per != null) {
            if(per>0 && per <90) {
                val new: Double = this.p.getPrice() - this.p.getPrice() * (per / 100)

                this.logger.writeData("Change made by " + realUser.getUsername() + "\n")
                this.logger.writeData("Date: "+LocalDateTime.now().toString() + "\n")
                this.logger.writeData("The price has changed for: " + this.p.getProductName() + "\n")
                this.logger.writeData("Old price: " + this.p.getPrice() + "lei/kg\n")
                this.logger.writeData("New price: " + new.toString() + "lei/kg\n")
                this.logger.writeData("Discount: $per %\n\n")
                p.setPrice(new)
            }
        }
    }
}



class KeyboardReader{
    companion object {
        fun read(): String? {
            return readLine()
        }
    }
}

class ProxyUser(private val realUser: RealUser) : User{
    override fun login(){

        print("User: ")
        val user = KeyboardReader.read()

        print("Password: ")
        val pass = KeyboardReader.read()

        if(!(user!=null && realUser.getUsername() == user)) {
            print("Invalid username!")
            return
        }

        if(!(pass!=null && pass == realUser.getPassword())){
            print("Invalid password!")
            return
        }

        realUser.login()

    }

}

class RealUser(private val user: String, private val password: String) : User, Observable{

    private val viewers = mutableListOf<Observer>()

    override fun login() {
        var i: Int
        do {
            print("1 - Apply discount for the product( in % )\n")
            print("0 - Sign Out\n")
            print("-> ")
            i = KeyboardReader.read()?.toInt()!!
            if(i == 0)
                break

            if(i == 1)
                viewers.forEach{it.update(this)}

        }while(i == 1)
    }

    fun getUsername():String{
        return this.user
    }

    fun getPassword(): String{
        return this.password
    }

    override fun attach(o: Observer) {
        this.viewers.add(o)
    }

}

class MyLogger(private val file: String) : Logger{
    override fun writeData(data: String) {
        try{
            Files.write(Paths.get(file), data.toByteArray(), StandardOpenOption.APPEND)
        }
        catch (e: IOException){
            print(e.message + "\n")
            exitProcess(0)
        }
    }
}


fun main() {
    val radu = RealUser("Raducu","123456")
    radu.attach(PriceCalc(Tomatoes(8.00)))
    val user1 = ProxyUser(radu)
    user1.login()
}