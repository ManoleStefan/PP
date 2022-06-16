
class Student(val nume:String,var stare:Stare) {
    enum class Stare{
        PREZENT,
        ABSENT
    }

    override fun toString(): String {
        return "Nume: " + nume + "; Stare: " + stare + "\n"
    }
}

class SalaCurs(val students:MutableList<Student>)
{
    fun adaugaStudent(s:Student)
    {
        students.add(s)
    }

    fun eliminaStudent(s:Student)
    {
        students.remove(s)
    }

    fun eliminaStudend(index:Int)
    {
        students.removeAt(index)
    }

    fun afiseazaStudenti()
    {
        for(std in students)
        {
            print(std)
        }
    }
}

fun main()
{
    val s1 = Student("Codau",Student.Stare.PREZENT)
    val s2 = Student("Popica",Student.Stare.PREZENT)
    val s3 = Student("Lupu",Student.Stare.ABSENT)

    val studenti = mutableListOf<Student>(s1,s2,s3)

    val sala = SalaCurs(studenti)

    sala.adaugaStudent(Student("Marinica",Student.Stare.PREZENT))
    sala.afiseazaStudenti()
    println()
    
    sala.eliminaStudend(2)
    sala.afiseazaStudenti()
}
