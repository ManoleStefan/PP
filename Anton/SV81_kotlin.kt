package org.example

import java.io.FileWriter

class Adaptor(file : String){
    val fis = FileWriter(file)
    fun insert(x:Any){
        if(x is String){
            fis.write("x este string\n")
            return
        }
        if(x is Int){
            fis.write("x este int\n")
            return
        }
        if(x is Boolean){
            fis.write("x este boolean\n")
            return
        }
        if(x is MutableList<*>) {
            fis.write("x e mutable list\n")
            return
        }
        if(x is Collection<*>){
            fis.write("x e collection\n")
            return
        }
    }
    fun close(){
        fis.close()
    }
}
fun main(){
    val alfa = Adaptor("fisier.txt")
    alfa.insert(23)
    alfa.insert("altceva")
    alfa.insert(mutableListOf(1,2,3))
    alfa.close()
}