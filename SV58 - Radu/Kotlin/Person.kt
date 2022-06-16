class Person(private val name : String, private val gender: String) {
    private var food : String = ""
    private var drink: String = ""
    private var dancingPartner : String = ""

    fun eat(food : String){
        this.food = food
    }

    fun drink(drink : String){
        this.drink = drink
    }

    fun dance(partner : String){
        this.dancingPartner = partner
    }

    fun whatIdo(){
        println("Eu sunt " + this.name +" - mananc "+this.food +", beau " + this.drink + " si dansez cu " +this.dancingPartner)
    }

    fun getName() : String{
        return this.name
    }

    fun getDancingPartner() : String{
        return this.dancingPartner
    }

    fun getGender() : String{
        return this.gender
    }

    fun getFood() : String{
        return this.food
    }
}

class PersonBuilder(){
    companion object {
        fun getPerson(statement: String, gender : String): Person {
            val slicedStatement = statement.replace(",", "").split(" ")

            val ret = Person(slicedStatement[0], gender)
            ret.eat(slicedStatement[slicedStatement.indexOf("mananca") + 1])
            ret.drink(slicedStatement[slicedStatement.indexOf("bea") + 1])
            ret.dance(slicedStatement[slicedStatement.indexOf("danseaza") + 2])

            return ret
        }
    }
}

class GangOfPeople(){
    private val people = mutableListOf<Person>()

    fun addPerson(p : Person){
        people.add(p)
    }

    fun whatWeDo(){
        people.forEach{it.whatIdo()}
        println()
    }

    fun whoDanceWith(name : String?) : String {
        people.forEach{
            if(it.getName() == name)
                return it.getDancingPartner()
        }

        return ""
    }

    fun whatGirlsEat(){
        people.forEach{
            if(it.getGender() == "femeie")
                println(it.getName() + " mananca " + it.getFood())
        }
    }

    fun whatBoysEat(){
        people.forEach{
            if(it.getGender() == "barbat")
                println(it.getName() + " mananca " + it.getFood())
        }
    }
}

class GangAnswerer(private val gang : GangOfPeople){
    fun answer(question : String){
        val questions = mutableListOf<String>()
        val aux = question.replace("?","").split(" si ")

        aux.forEach { it.split("dar").forEach {
            questions.add(it) } }

        questions.forEach{
            println(it +"?")
            if(it.contains("u cine poate dansa")){
                val name = it.split(" ").lastOrNull()
                println(name + " poate dansa cu " + gang.whoDanceWith(name))
            }

            if(it.contains("ce pot manca")){
                val gender = it.split(" ").lastOrNull()
                if(gender == "femeile")
                    gang.whatGirlsEat()
                else
                    gang.whatBoysEat()
            }
            //de completat...
            println()
        }
    }
}

fun main(){
    val gang = GangOfPeople()
    val q_and_a = GangAnswerer(gang)

    gang.addPerson(PersonBuilder.getPerson("Ion mananca mere, bea bere si danseaza cu femei", "barbat"))
    gang.addPerson(PersonBuilder.getPerson("Vasile mananca pere, bea vodca si danseaza cu barbati", "barbat"))
    gang.addPerson(PersonBuilder.getPerson("Alex bea vin, mananca prajitui si danseaza cu sefii","barbat"))
    gang.addPerson(PersonBuilder.getPerson("Lavinia bea suc, mananca tort si danseaza cu Vlad","femeie"))

    gang.whatWeDo()

    q_and_a.answer("Cu cine poate dansa Vasile si ce pot manca barbatii dar ce pot manca femeile?")

}