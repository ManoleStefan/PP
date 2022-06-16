/*import java.io.File
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

interface Shape{
    fun GetArea() : Double
    fun getVolume() : Double
}

class Circle(val v : Double) : Shape{
    override fun GetArea(): Double {
        return Math.pow(v,2.0) * Math.PI
    }

    override fun getVolume(): Double {
        return (4/3) * Math.pow(v,3.0) * Math.PI
    }
}

class Square(val l : Double) : Shape{
    override fun GetArea(): Double {
        return Math.pow(l,2.0)
    }

    override fun getVolume(): Double {
        return Math.pow(l,3.0)
    }
}

class Rectangle(val size : Pair<Pair<Double,Double>,Double>) : Shape{
    override fun GetArea(): Double {
        return size.first.first * size.first.second
    }

    override fun getVolume(): Double {
        return this.GetArea() * size.second
    }
}


interface ComputeData{
    fun Sum() : Double
}

class ComputeV(val shapes : Array<Shape>) : ComputeData{
    override fun Sum() : Double{
        var sum = 0.0
        shapes.forEach {
            sum += it.getVolume()
        }
        return sum
    }
}

class ComputeA(val shapes : Array<Shape>) : ComputeData{
    override fun Sum() : Double{
        var sum = 0.0
        shapes.forEach {
            sum += it.GetArea()
        }
        return sum
    }
}

fun main(args : Array<String>){
    val circles : Array<Shape> = arrayOf(Circle(2.0),Circle(3.0),Circle(4.1))
    val square : Array<Shape>  = arrayOf(Square(5.4),Square(9.2),Square(1.1))
    val rects : Array<Shape>  = arrayOf(Rectangle(Pair(Pair(2.0,3.0),5.0)),Rectangle(Pair(Pair(3.1,9.2),7.5)),Rectangle(Pair(Pair(1.0,1.0),2.0)))

    var computev = ComputeV(circles)
    println("Suma volume cercuri : ${computev.Sum()}")
    computev = ComputeV(square)
    println("Suma volume patrate : ${computev.Sum()}")
    computev = ComputeV(rects)
    println("Suma volume dreptunghiuri : ${computev.Sum()}")

    println("\n\n")
    var computea = ComputeA(circles)
    println("Suma arii cercuri : ${computea.Sum()}")
    computea = ComputeA(square)
    println("Suma arii patrate : ${computea.Sum()}")
    computea = ComputeA(rects)
    println("Suma arii dreptunghiuri : ${computea.Sum()}")


    val serA = Serializer(computea, 1)
    val serV = Serializer(computev, 2)
    serA.ToHTML()
    serA.ToJSON()
    serV.ToHTML()
    serV.ToJSON()

}*/