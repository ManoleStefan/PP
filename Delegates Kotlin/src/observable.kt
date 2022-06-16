import kotlin.properties.Delegates

class Looser{
    var nume : String by Delegates.observable("inca nu am nume"){
        prop,old,new-> println("$old - $new")
    }
}

fun main(){
    val utilizator = Looser()
    utilizator.nume = "Cel mai prost din curtea scolii"
    utilizator.nume = "Inca si mai prost"
    utilizator.nume = "bun de avansare"
    print(utilizator.nume)
}