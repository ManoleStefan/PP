import java.io.BufferedWriter
import java.io.File
import java.lang.Exception

class Adapter{
    val mySerializer = Serializer()

    fun AdaptToString(obj: Any) : String{
        try {
            if (obj is Int) {
                val leInt = obj.toInt()
                return leInt.toString()
            }
            if (obj is String) {
                return obj.toString()
            }
            if (obj is Collection<*>) {
                var s: String = "{ "
                obj.forEach {
                    s += it.toString() + " "
                }
                s += "}"
                return s
            }
            return obj.toString()
        }
        catch (e : Exception){
            return ""
        }
    }

    fun writeToFile(filename: String, obj:Any){
        mySerializer.SerilizeToFile(filename, AdaptToString(obj))
    }
}

class Serializer{
    fun SerilizeToFile(filename: String, content: String){
        try {
            val myFile = File(filename)
            myFile.writeText(content)
        }
        catch(e : Exception)
        {
            println("Error from writing to file!")
        }
    }
}

class MyObject(val greet:String, val name:String){
    override fun toString(): String {
        return greet + " " + name + "!"
    }
}

fun main(args: Array<String>) {
    val myAdapter = Adapter()

    val myInt = 42
    val myString = "42 as a String"
    val myCollection = listOf(42, "42 as a string in colection", listOf("element in element of colection", 32))
    val myObject = MyObject("Hello", "Vlad")

    myAdapter.writeToFile("intFile.txt", myAdapter.AdaptToString(myInt))
    myAdapter.writeToFile("stringFile.txt", myAdapter.AdaptToString(myString))
    myAdapter.writeToFile("collectionFile.txt", myAdapter.AdaptToString(myCollection))
    myAdapter.writeToFile("objectFile.txt", myAdapter.AdaptToString(myObject))
}