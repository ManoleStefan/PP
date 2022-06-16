
fun cePoateFace(o:Om)
{
    println(o.nume + " poate dansa cu "+o.dans)
}

fun cePoateFace(persoane:List<Om>,gender:String)
{
    for(elem in persoane)
    {
        if(elem.gender.equals(gender))
        {
            println(elem.nume + " poate mananca " + elem.mancare )
        }
    }
}


fun main()
{
    val o1 = Om("ion","mere","bere","femei","male")
    val o2 = Om("vasile","pere","vodca","barbati","male")
    val o3 = Om("alex","prajituri brune","vin","sefii","male")

    val group = listOf<Om>(o1,o2,o3)
    cePoateFace(o2)
    cePoateFace(group,"male")
    cePoateFace(group,"female")
}