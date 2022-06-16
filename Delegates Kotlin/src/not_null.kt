import kotlin.properties.Delegates
class Loser{
    var nume : String by Delegates.notNull()
    fun initializare(nume : String){
        this.nume = nume
    }
}

fun main(){
    val user = Loser()
    user.initializare("Bibistrocel")
    println(user.nume)
}