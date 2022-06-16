import java.io.File
import java.time.LocalDate
import java.util.*
import kotlin.collections.ArrayList

interface IObserver{
    fun update(subject : IObservable)
}

class Logger(private val filename : String) : IObserver{
    private val file = File(filename)

    override fun update(subject: IObservable) {
        val data = subject.getData().toString()
        val user = subject.getUser()

        val currentDate = LocalDate.now()
        val line = currentDate.year.toString() + "-" + currentDate.month.toString() + "-" + currentDate.dayOfMonth.toString() +
                ": [" + user + "] modified value to: " + data + "\n"

        file.appendText(line)
    }
}

interface IObservable{
    fun getData() : Double
    fun getUser() : String?
    fun attach(observer : IObserver)
    fun detach(observer : IObserver)
    fun updateAll()
}

interface ICurrentPrice{
    fun changePrice(rate : Double)
}

class CurrentPrice(private var price : Double) : ICurrentPrice, IObservable {
    private var user:String? = null
    private val observers = ArrayList<IObserver>()

    override fun getData(): Double {
        return price
    }

    override fun getUser(): String? {
        return user
    }

    override fun attach(observer: IObserver) {
        observers.add(observer)
    }

    override fun detach(observer: IObserver) {
        observers.remove(observer)
    }

    override fun updateAll() {
        observers.forEach{
            it.update(this)
        }
    }

    override fun changePrice(rate: Double) {
        price *= rate
        updateAll()
    }

    fun setUser(user : String){
        this.user = user
    }

}

class MyProxy(private var price : Double) : ICurrentPrice, IObservable{
    private val currentPrice = CurrentPrice(price)
    private val usersAccounts = mapOf<String, String>(
        "vlad_batalan" to "bors123",
        "george_butnariu" to "trifoi"
    )


    override fun getData(): Double {
        return currentPrice.getData()
    }

    override fun getUser(): String? {
        return currentPrice.getUser()
    }

    override fun attach(observer: IObserver) {
        currentPrice.attach(observer)
    }

    override fun detach(observer: IObserver) {
        currentPrice.detach(observer)
    }

    override fun updateAll() {
        currentPrice.updateAll()
    }

    override fun changePrice(rate: Double) {
        if(checkAccess()){
            currentPrice.changePrice(rate)
            println("The rate has been changed!")
        }
        else {
            println("Nu sunt destule permisiuni pentru aceasta actiune!")
        }
    }

    private fun checkAccess() : Boolean{
        var logging = true
        val buffer = Scanner(System.`in`)

        while(logging){
            print("Username: ")
            val user = buffer.next()
            println("You typed: $user")
            print("Password: ")
            val password = buffer.next()
            println("You typed: $password")

            if(usersAccounts.containsKey(user)){
                if(usersAccounts.getValue(user) == password) {
                    currentPrice.setUser(user)
                    return true
                }
            }

            println("Invalid username or password!")
            println("Introduce again? Y/n")

            val option = buffer.next()
            if(!option.equals("Y"))
                logging = false
        }
        return false
    }

}

fun main(args: Array<String>) {
    val log = Logger("log.txt")

    val marketPrice:MyProxy = MyProxy(15.0)
    marketPrice.attach(log)

    var insert = true
    val buffer = Scanner(System.`in`)
    while(insert){
        print("\nInsert the rate: ")
        val rate = buffer.nextDouble()

        marketPrice.changePrice(rate)

        println("Introduce rate again? Y/n")
        val option = buffer.next()
        if(!option.equals("Y"))
            insert = false
    }

}