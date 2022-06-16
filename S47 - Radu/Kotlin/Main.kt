fun main(){
    val A = listOf(1, 2, 3)
    val B = listOf(3, 4, 5)

    val AxB = A.flatMap { a -> B.map { b -> a to b } }// produs cartezian
    val BxB= B.flatMap { a -> B.map { b -> a to b } }

    println("AxB: " + AxB)
    println("BxB: " + BxB)

    val AxB_U_BxB = (AxB + BxB).distinct()//reuniune

    print("AxB U BxB: " +AxB_U_BxB)
}