public class Main {
    public static void main(String[] args){
        KidPatient kp = new KidPatient("sesi");
        kp.setName("Pedrinho");
        String name = kp.getName();
        System.out.println("Everything ok, " + name);
    }
}
