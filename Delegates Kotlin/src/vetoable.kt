import java.time.Period
import kotlin.properties.Delegates

class Pierzator{
    var valoareaCrescatoare : Int by Delegates.vetoable(0){
        prop,old,new ->
        if(old < new) {
            println("corect")
            true
        }
        else throw IllegalArgumentException("Noua valoarea trebuie sa fie mai mare decat vechea")
    }
}

fun main(){
    var x = Pierzator()
    x.valoareaCrescatoare = 10
    x.valoareaCrescatoare = 12
    try{
        x.valoareaCrescatoare = 6
    }
    catch (e : IllegalArgumentException){
        println("Exceptieeeeeeeeeeee")
    }
    x.valoareaCrescatoare = 15
    println(x.valoareaCrescatoare)
}