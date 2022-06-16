fun main()
{
    // partea de observer
    val priceobs = PriceObserver(1000.0)
    val list = mutableListOf<Observer>(priceobs)

    var priceChange = PriceChange(0.0,list)

    // partea de proxy
    val priceLogin = PriceLogin(priceChange)

    priceLogin.login("Edi","12345")
}