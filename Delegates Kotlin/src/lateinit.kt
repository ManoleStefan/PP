import kotlin.properties.Delegates

class SubiectTestare{
    fun zice(){
        println("Iar ma chinuie asta")
    }
}

class PrimulTest{
    lateinit var subiectTestare: SubiectTestare
    fun setup(){
        subiectTestare = SubiectTestare()
    }

    fun Test(){
        if(this::subiectTestare.isInitialized)
            subiectTestare.zice()
    }
}

fun main(){
    val x = PrimulTest()
    //x.setup()
    x.Test()
}