interface Persoana{
    fun afiseazaNume()
}

class ImplementarePersoana(val nume :String) : Persoana{
    override fun afiseazaNume() {
        println(nume)
    }
}

class Utilizator(val persoana : Persoana) : Persoana by persoana{
    override fun afiseazaNume() {
        println("Numele este : ")
        persoana.afiseazaNume()
    }
}

fun main(){
    val persoana = ImplementarePersoana("Bugs Bunny")
    persoana.afiseazaNume()
    val utilizator = Utilizator(persoana)
    utilizator.afiseazaNume()
}