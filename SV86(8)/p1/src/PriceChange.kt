class PriceChange(var state:Double, val observers:MutableList<Observer>)
{
    fun addObserver(obs:Observer)
    {
        observers.add(obs)
    }

    fun changePrice(rate_of_change:Double,filename:String)
    {
        state = rate_of_change
        notifyAll(rate_of_change,filename)
    }

    fun notifyAll(rate_of_change: Double,filename: String)
    {
        for( i in observers )
        {
            i.update(rate_of_change = rate_of_change,filename = filename)
        }
    }

}