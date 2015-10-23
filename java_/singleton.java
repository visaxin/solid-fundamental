public class JavaHungrySingleton{
    private static volatile JavaHungrySingleton uniqueInstance;

    private JavaHungrySingleton(){}

    public static JavaHungrySingleton getInstance(){
        if(uniqueInstance == null){
            synchronized(JavaHungrySingleton.class){
                if(uniqueInstance == null){

                uniqueInstance = new JavaHungrySingleton();
                }
            }
        }
        return uniqueInstance;
    }

}

/*
 * volatile make sure the thread which create instance of Singleton
 * is able to communicate other thread
 *
 * /
