import java.io.File

interface NonSolidShape{
    fun GetArea() : Double
}

interface SolidShape{
    fun getVolume() : Double
}

interface Solids : SolidShape,NonSolidShape {
    override fun GetArea() : Double
    override fun getVolume() : Double
}

class Circle(val v : Double) : Solids{
    override fun GetArea(): Double {
        return Math.pow(v,2.0) * Math.PI
    }

    override fun getVolume(): Double {
        return (4/3) * Math.pow(v,3.0) * Math.PI
    }
}

class Square(val l : Double) : Solids{
    override fun GetArea(): Double {
        return Math.pow(l,2.0)
    }

    override fun getVolume(): Double {
        return Math.pow(l,3.0)
    }
}

class Rectangle(val size : Pair<Double,Double>) : NonSolidShape {
    override fun GetArea(): Double {
        return size.first * size.second
    }
}


interface ComputeData{
    fun Sum() : Double
}

class ComputeV(val shapes : Array<SolidShape>) : ComputeData{
    override fun Sum() : Double{
        var sum = 0.0
        shapes.forEach {
            sum += it.getVolume()
        }
        return sum
    }
}

class ComputeA(val shapes : Array<NonSolidShape>) : ComputeData{
    override fun Sum() : Double{
        var sum = 0.0
        shapes.forEach {
            sum += it.GetArea()
        }
        return sum
    }
}

class Serializer(private val compute : ComputeData, private val index : Int) {
    fun ToHTML(){ val fisier = File("output_$index.html").writer()
        fisier.write("<HTML><HEAD><TITLE>SERIALIZER</TITLE></HEAD>\n<BODY>\n")
        fisier.write("<p><h1>${compute.Sum()}</h1></p>\n")
        fisier.write("</BODY></HTML>")
        fisier.close()
    }
    fun ToJSON(){ val fisier = File("output_$index.json").writer()
        fisier.write("{\"Sum\":\"${compute.Sum()}\"}")
        fisier.close()
    }
}


fun main(args : Array<String>){
    var circles : Array<SolidShape> = arrayOf(Circle(2.0),Circle(3.0),Circle(4.1))
    var square : Array<SolidShape>  = arrayOf(Square(5.4),Square(9.2),Square(1.1))
    var rects : Array<NonSolidShape>  = arrayOf(Rectangle(Pair(2.0,3.0)),Rectangle(Pair(2.5,3.54)),Rectangle(Pair(2.2,7.0)))

    var computev = ComputeV(circles)
    println("Suma volume cercuri : ${computev.Sum()}")
    computev = ComputeV(square)
    println("Suma volume patrate : ${computev.Sum()}")

    println("\n\n")

    var computea = ComputeA(rects)
    println("Suma arii dreptunghiuri : ${computea.Sum()}")


    val serA = Serializer(computea, 1)
    val serV = Serializer(computev, 2)
    serA.ToHTML()
    serA.ToJSON()
    serV.ToHTML()
    serV.ToJSON()
}