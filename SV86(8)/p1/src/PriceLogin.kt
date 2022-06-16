import java.util.*

class PriceLogin(val priceObs:PriceChange) : Manager{
    fun login(username:String,password:String){
        if(username=="Edi" && password=="12345")
        {
            var ok=1
            val s = Scanner(System.`in`)
            while(ok==1)
            {
                print("Introduceti rata de crestere a pretului: ")
                val rate = s.nextDouble()
                priceObs.changePrice(rate,"logs.txt")
                print("Doriti o noua actualizare: ")
                ok = s.nextInt()
            }
        }
        else
        {
            println("Username sau parola gresita. Se inchide sesiunea...")
        }
    }
}