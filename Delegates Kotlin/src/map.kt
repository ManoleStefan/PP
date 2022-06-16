data class Carte(val delegate : Map<String,Any?>){
    val nume : String by delegate
    val autori : String by delegate
    val editura : String by delegate
    val numarPagini : Int by delegate
    val dataPublicarii : String by delegate
}

fun main(){
    val mapCarte1 = mapOf(
        Pair("nume","Nume carte"),
        Pair("autori","Creanga"),
        Pair("editura","Polidorm"),
        Pair("numarPagini",120),
        Pair("dataPublicarii","12:12:10023")
    )

    val carte1 = Carte(mapCarte1)
    println(carte1)
}