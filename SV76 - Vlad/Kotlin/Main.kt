import java.lang.Exception
import kotlin.reflect.jvm.internal.impl.types.AbstractTypeCheckerContext

interface ISala{
    fun setRecuzite(recuzite : List<IRecuzita>, timp : Int)
    fun intraPersoana(persoana : IPersoana, timp : Int)
    fun iesePersoana(persoana : IPersoana, timp : Int)
    fun adaugaRecuzita(recuzita : IRecuzita, timp : Int)
    fun stergeRecuzita(recuzita : IRecuzita, timp : Int)
    fun persoaneInSala()
    fun recuziteInSala()
    fun logSala()
}

interface IRecuzita{
    fun folositaDe(persoana : IPersoana?)

}

interface IPersoana{
    fun vorbeste(mesaj : String)
    fun intraSala(sala : ISala, timp : Int)
    fun ieseSala(sala : ISala, timp : Int)
    fun folosesteRecuzita(recuzita : IRecuzita, timp : Int)
    fun opresteFolosireaRecuzitei(recuzita: IRecuzita, timp: Int)
}

class SalaDeLaborator(private val numeSala : String) : ISala{
    val recuzite = mutableListOf<IRecuzita>()
    val persoane = mutableListOf<IPersoana>()
    var logText = ""

    override fun setRecuzite(recuzite: List<IRecuzita>, timp: Int) {
        recuzite.forEach {
            adaugaRecuzita(it, timp)
        }
    }

    override fun intraPersoana(persoana: IPersoana, timp: Int) {
        persoane.add(persoana)
        logText += "$timp: Intra: ${persoana}\n"
    }

    override fun iesePersoana(persoana: IPersoana, timp: Int) {
        persoane.remove(persoana)
        logText += "$timp: Iese: ${persoana}\n"
    }

    override fun adaugaRecuzita(recuzita: IRecuzita, timp: Int) {
        recuzite.add(recuzita)
        logText += "$timp: A fost adaugata: ${recuzita}\n"
    }

    override fun stergeRecuzita(recuzita: IRecuzita, timp: Int) {
        recuzite.remove(recuzita)
        logText += "$timp: A fost scoasa: ${recuzita}\n"
    }

    override fun persoaneInSala() {
        println("Persoane in $numeSala:")
        persoane.forEach {
            println("\t$it")
        }
    }

    override fun recuziteInSala() {
        println("Recuzite in $numeSala:")
        recuzite.forEach {
            println("\t$it")
        }
    }

    override fun logSala() {
        println("Log pentru sala $numeSala:")
        println(logText)
    }

}

class Student(private val numeStudent : String, private val grupa : String) : IPersoana{
    override fun vorbeste(mesaj: String) {
        println("${this.toString()} a spus: $mesaj")
    }

    override fun intraSala(sala: ISala, timp: Int) {
        sala.intraPersoana(this,timp)
    }

    override fun ieseSala(sala: ISala, timp: Int) {
        sala.iesePersoana(this, timp)
    }

    override fun folosesteRecuzita(recuzita: IRecuzita, timp: Int) {
        try {
            recuzita.folositaDe(this)
        }catch(e : Exception){
            println(e)
        }
    }

    override fun opresteFolosireaRecuzitei(recuzita: IRecuzita, timp: Int) {
        recuzita.folositaDe(null)
    }

    override fun toString(): String {
        return "Student: $numeStudent, Grupa: $grupa"
    }
}

class Profesor(private val numeProfesor : String, private val materie: String) : IPersoana{
    override fun vorbeste(mesaj: String) {
        println("${this.toString()} a spus: $mesaj")
    }

    override fun intraSala(sala: ISala, timp: Int) {
        sala.intraPersoana(this,timp)
    }

    override fun ieseSala(sala: ISala, timp: Int) {
        sala.iesePersoana(this, timp)
    }

    override fun folosesteRecuzita(recuzita: IRecuzita, timp: Int) {
        try {
            recuzita.folositaDe(this)
        }catch(e : Exception){
            println(e)
        }
    }

    override fun toString(): String {
        return "Profesor: $numeProfesor, Materie: $materie"
    }

    override fun opresteFolosireaRecuzitei(recuzita: IRecuzita, timp: Int) {
        recuzita.folositaDe(null)
    }
}

class Calculator(private val numarStatie : Int) : IRecuzita{
    private var persoana : IPersoana? = null
    override fun folositaDe(persoana: IPersoana?) {
        if(persoana == null) {
            this.persoana = null
            return
        }
        if(this.persoana != null)
            throw Exception("$persoana deja foloseste $this")
        else
            this.persoana = persoana
    }

    override fun toString(): String {
        return "Calculator: S$numarStatie"
    }

}


fun main(args: Array<String>) {
    val laborator1 : ISala = SalaDeLaborator("C43")

    var timpCurent = 0

    val calc1 = Calculator(1)
    val calc2 = Calculator(2)
    val calc3 = Calculator(3)

    laborator1.setRecuzite(listOf<IRecuzita>(
        calc1,
        calc2,
        calc3
    ), timpCurent)

    val marcel = Student("Marcel", "1211A")
    val vlad = Student("Vlad", "1211B")
    val mike = Profesor("Mike", "Paradigme de programare")

    timpCurent += 10
    vlad.intraSala(laborator1, timpCurent)
    timpCurent += 1
    vlad.folosesteRecuzita(calc1,timpCurent)
    timpCurent += 10
    marcel.intraSala(laborator1,timpCurent)
    timpCurent += 1
    marcel.vorbeste("Ce faci, Vlad? Gata de examen?")
    timpCurent += 2
    marcel.folosesteRecuzita(calc1,timpCurent)
    marcel.folosesteRecuzita(calc2, timpCurent)
    timpCurent += 1
    vlad.vorbeste("Ce sa fac? Oleaca pe la examen...")

    timpCurent += 2
    mike.vorbeste("Treceti la injurat!")
    timpCurent += 10
    mike.intraSala(laborator1, timpCurent)

    timpCurent+=1
    vlad.vorbeste("Fugi!")
    vlad.opresteFolosireaRecuzitei(calc1,timpCurent)
    marcel.opresteFolosireaRecuzitei(calc2, timpCurent)
    vlad.ieseSala(laborator1,timpCurent)
    marcel.ieseSala(laborator1, timpCurent)

    timpCurent+=10
    mike.vorbeste("Da unde plecati, domnilor? Examenul e aici!")
    timpCurent += 10
    mike.vorbeste("Deci sa inteleg ca nu dati examen ... Ia sa vedem ce s a intamplat in sala asta (Aprinde camera)")

    laborator1.logSala()

}