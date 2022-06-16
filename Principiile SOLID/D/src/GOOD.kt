interface Developer{
    fun develop()
}

class BackEndDeveloper : Developer{
    override fun develop(){
        print("Writing Java")
    }
}

class FrontEndDeveloper : Developer{
    override fun develop() {
        print("Writing Java")
    }
}


class Project(val Developer: List<Developer>){
    fun implement(){
        Developer.forEach{
            it.develop()
        }
    }
}