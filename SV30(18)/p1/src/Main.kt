import java.io.File

class Node(var key:String="", var left:Node?=null, var right: Node? = null) {
    fun insert(value: String) {
        if (value.length> this.key.length)
        {
            if(this.right == null)
            {
                this.right = Node(value)
            }
            else
            {
                this.right?.insert(value)
            }
        }
        else if(value.length < this.key.length)
        {
            if(this.left == null)
            {
                this.left = Node(value)
            }
            else
            {
                this.left?.insert(value)
            }
        }
    }

    fun find(value:String) :Node? = when{
            this.key.length > value.length -> this.left!!.find(value)
            this.key.length < value.length -> this.right!!.find(value)
            else ->  this
    }

    fun inorderPrint()
    {
        this.left?.inorderPrint()
        this.right?.inorderPrint()
        println(this.key)
    }

    fun map(f: (Node) -> Node):Node
    {
        val arbore = Node(f(this).key)
//        if(left != null) arbore.left = left?.map(f)
//        if(right != null) arbore.right = right?.map(f)
        return arbore
    }
}

//class ValueFunctor(val value:Node)
//{
//    fun map(function : (Node) -> Node): ValueFunctor{
//        return ValueFunctor(function(value))
//    }
//}

fun printSubTree(value:Node) : Node{
    value.inorderPrint()
    return value
}

fun main()
{
    val f = File("src/input.txt")
    val s = f.readText().split(" ")
    val r = Node(s[0])

    for(i in (1..s.size-1))
    {
        r.insert(s[i])
    }

    r.inorderPrint()
    println()
    val r1 = r.find("turpis")?.map(::printSubTree)
    println()

}